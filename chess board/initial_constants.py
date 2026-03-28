
initial = { 11: "brook1", 21: "bknight1", 31: "bbishop1", 41: "bqueen", 51: "bking", 61: "bbishop2", 71: "bknight2", 81: "brook2",
            12: "bpawn1", 22: "bpawn2", 32: "bpawn3", 42: "bpawn4", 52: "bpawn5", 62: "bpawn6", 72: "bpawn7", 82: "bpawn8",
            13: None, 23: None, 33: None, 43: None, 53: None, 63: None, 73: None, 83: None,
            14: None, 24: None, 34: None, 44: None, 54: None, 64: None, 74: None, 84: None,
            15: None, 25: None, 35: None, 45: None, 55: None, 65: None, 75: None, 85:None,
            16: None ,26:None ,36:None ,46:None ,56:None ,66:None ,76:None ,86:None ,
            17: "wpawn1", 27: "wpawn2", 37: "wpawn3", 47: "wpawn4", 57: "wpawn5", 67: "wpawn6", 77: "wpawn7", 87: "wpawn8",
            18: "wrook1", 28: "wknight1", 38: "wbishop1", 48: "wqueen", 58: "wking", 68: "wbishop2", 78: "wknight2", 88: "wrook2"}

palette = {
    #code:  dark square  light square  dark piece   light piece]
    "A"  : ["#5C4033", "#CDBA76", "#1E110B", "#FFF8E7"],
    "B"  : ["#8B5A2B", "#E8D8C3", "#2F2F2F", "#F5F5F5"],
    "C"  : ["#2C2F33", "#D6D9DC", "#1B263B", "#F0F3F4"],
    "D"  : ["#8C2F2F", "#F7E7CE", "#1C1C1C", "#C3A33A"],
    "E"  : ["#3B5D3B", "#95A48B", "#222222", "#D6D4CE"]
}

# Selected palette name moved here to avoid circular imports
palette_name = "A"

x_no_to_pos = {1 : "a", 2 : "b", 3 : "c", 4 : "d", 5 : "e", 6 : "f", 7 : "g", 8 : "h"}
y_no_to_pos = {1 : "1", 2 : "2", 3 : "3", 4 : "4", 5 : "5", 6 : "6", 7 : "7", 8 : "8"}