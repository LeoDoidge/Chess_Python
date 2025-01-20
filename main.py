"""
The main script for the program. 

Key structure: [Reserved: 2 bits][Captured: 1 bit][Promotion: 3 bits][Moved: 1 bit][En Passant: 1 bit][Unique ID: 4 bits][Color: 1 bit][Piece Type: 3 bits]
"""


def KeyCreation(
    piece_type: str,
    color: str,
    unique_id: int,
    moved: bool = False,
    en_passant: bool = False,
    captured: bool = False,
    promotion: str = None,
) -> int:
    """
    Args:
        piece_type (str): Type of the piece (e.g., "pawn", "knight", etc.).
        color (str): Color of the piece ("white" or "black").
        unique_id (int): Unique identifier for the piece (0-15).
        moved (bool): Whether the piece has moved.
        en_passant (bool): Whether the pawn is eligible for en passant.
        captured (bool): Whether the piece has been captured.
        promotion (str): If the pawn is promoted, specify its new type (e.g., "queen").

    Returns:
        int: A 16-bit integer key.
    """
    # Map piece types to 3-bit integers
    piece_type_map = {
        "pawn": 0b000,
        "knight": 0b001,
        "bishop": 0b010,
        "rook": 0b011,
        "queen": 0b100,
        "king": 0b101,
    }

    # Map promotion types to 3-bit integers
    promotion_map = {
        None: 0b000,  # Not promoted
        "queen": 0b001,
        "rook": 0b010,
        "bishop": 0b011,
        "knight": 0b100,
    }

    # Validate inputs
    if piece_type not in piece_type_map:
        raise ValueError(f"Invalid piece type: {piece_type}")
    if color not in ["white", "black"]:
        raise ValueError(f"Invalid color: {color}")
    if not 0 <= unique_id < 16:
        raise ValueError(f"Unique ID must be between 0 and 15, got {unique_id}")
    if promotion not in promotion_map:
        raise ValueError(f"Invalid promotion type: {promotion}")

    # Encode fields
    type_bits = piece_type_map[piece_type]  # 3 bits
    color_bit = 0b1 if color == "black" else 0b0  # 1 bit
    id_bits = unique_id  # 4 bits
    moved_bit = 0b1 if moved else 0b0  # 1 bit
    en_passant_bit = 0b1 if en_passant else 0b0  # 1 bit
    captured_bit = 0b1 if captured else 0b0  # 1 bit
    promotion_bits = promotion_map[promotion]  # 3 bits

    # Combine into 16 bits
    key = (
        (0b00 << 14)
        | (captured_bit << 13)
        | (promotion_bits << 10)
        | (moved_bit << 9)
        | (en_passant_bit << 8)
        | (id_bits << 4)
        | (color_bit << 3)
        | type_bits
    )
    return key


def KeyDecoder(key: int) -> dict:

    # Map 3-bit integers to piece types
    piece_type_map = {
        0b000: "pawn",
        0b001: "knight",
        0b010: "bishop",
        0b011: "rook",
        0b100: "queen",
        0b101: "king",
    }

    # Map 3-bit integers to promotion types
    promotion_map = {
        0b000: None,
        0b001: "queen",
        0b010: "rook",
        0b011: "bishop",
        0b100: "knight",
    }

    # Extract fields
    reserved = (key >> 14) & 0b11  # Reserved bits
    captured_bit = (key >> 13) & 0b1
    promotion_bits = (key >> 10) & 0b111
    moved_bit = (key >> 9) & 0b1
    en_passant_bit = (key >> 8) & 0b1
    unique_id = (key >> 4) & 0b1111
    color_bit = (key >> 3) & 0b1
    type_bits = key & 0b111

    # Decode fields
    piece_type = piece_type_map.get(type_bits, "unknown")
    color = "black" if color_bit else "white"
    promotion = promotion_map.get(promotion_bits, None)
    moved = bool(moved_bit)
    en_passant = bool(en_passant_bit)
    captured = bool(captured_bit)

    return {
        "reserved": reserved,
        "piece_type": piece_type,
        "color": color,
        "unique_id": unique_id,
        "moved": moved,
        "en_passant": en_passant,
        "captured": captured,
        "promotion": promotion,
    }


class Board:
    def __init__(self):
        self.grid = [
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
        ]

    def PrintBoard(self):
        for row in self.grid:
            print(" | ".join(str(cell) if cell != "--" else "--" for cell in row))
        print()  # Add a blank line for better readability

    def PlacePiece(self, piece, position):
        x, y = position
        self.grid[x][y] = piece

    def DefaultSetup(self):
        # Set up white pieces
        for i in range(8):
            self.PlacePiece(Piece("pawn", "white", i), (1, i))  # White pawns in row 1
        self.PlacePiece(Piece("rook", "white", 0), (0, 0))  # White rooks
        self.PlacePiece(Piece("rook", "white", 1), (0, 7))
        self.PlacePiece(Piece("knight", "white", 0), (0, 1))  # White knights
        self.PlacePiece(Piece("knight", "white", 1), (0, 6))
        self.PlacePiece(Piece("bishop", "white", 0), (0, 2))  # White bishops
        self.PlacePiece(Piece("bishop", "white", 1), (0, 5))
        self.PlacePiece(Piece("queen", "white", 0), (0, 4))  # White queen
        self.PlacePiece(Piece("king", "white", 0), (0, 3))  # White king

        # Set up black pieces
        for i in range(8):
            self.PlacePiece(Piece("pawn", "black", i), (6, i))  # Black pawns in row 6
        self.PlacePiece(Piece("rook", "black", 0), (7, 0))  # Black rooks
        self.PlacePiece(Piece("rook", "black", 1), (7, 7))
        self.PlacePiece(Piece("knight", "black", 0), (7, 1))  # Black knights
        self.PlacePiece(Piece("knight", "black", 1), (7, 6))
        self.PlacePiece(Piece("bishop", "black", 0), (7, 2))  # Black bishops
        self.PlacePiece(Piece("bishop", "black", 1), (7, 5))
        self.PlacePiece(Piece("queen", "black", 0), (7, 4))  # Black queen
        self.PlacePiece(Piece("king", "black", 0), (7, 3))  # Black king

    def PrintPieceDetails(self, position):
        x, y = position
        piece = self.grid[x][y]
        if isinstance(piece, Piece):
            print(f"Key: {piece.id}")
            self._PrintDecodedDetails(piece.Decode())
        else:
            print("No piece at the given coordinates.")

    def _PrintDecodedDetails(self, decoded):
        print("Decoded Piece Information:")
        for key, value in decoded.items():
            print(f"  {key.capitalize()}: {value}")

    def GetPiecePositionById(self, piece_id):
        for x in range(8):
            for y in range(8):
                piece = self.grid[x][y]
                if isinstance(piece, Piece) and piece.id == piece_id:
                    return (x, y)
        return None


class Piece:
    def __init__(
        self,
        piece_type: str,
        color: str,
        unique_id: int,
        moved: bool = False,
        en_passant: bool = False,
        captured: bool = False,
        promotion: str = None,
        position: tuple = None,
    ):
        self.id = KeyCreation(
            piece_type, color, unique_id, moved, en_passant, captured, promotion
        )
        self.type = piece_type
        self.color = color
        self.moved = moved
        self.position = position

    def __str__(self):
        color_code = "w" if self.color == "white" else "b"
        return f"{color_code}{self.type[0].upper()}"

    def Decode(self):
        return KeyDecoder(self.id)

    def PawnLegalMoves(self, board: Board):
        legal_moves = []
        x, y = self.position

        # Regular forward move (1 step)
        if self.color == "white":
            if board.grid[x + 1][y] == "--":  # If the square is empty
                legal_moves.append((x + 1, y))
                # Double move if it's the first move
                if not self.moved and board.grid[x + 2][y] == "--":
                    legal_moves.append((x + 2, y))
        else:  # For black pieces
            if board.grid[x - 1][y] == "--":
                legal_moves.append((x - 1, y))
                if not self.moved and board.grid[x - 2][y] == "--":
                    legal_moves.append((x - 2, y))

        return legal_moves

    def KnightLegalMoves(self, board: Board):
        legal_moves = []
        x, y = self.position
        offsets = [
            (1, 2),
            (1, -2),
            (-1, 2),
            (-1, -2),
            (2, 1),
            (2, -1),
            (-2, 1),
            (-2, -1),
        ]

        for dx, dy in offsets:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < 8 and 0 <= new_y < 8:
                if board.grid[new_x][new_y] == "--" or board.grid[new_x][new_y].color != self.color:
                    legal_moves.append((new_x, new_y))

        return legal_moves
