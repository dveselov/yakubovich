import struct

SAVEFILE_SIGNATURE = b"FALLOUT SAVE FILE"
SAVEFILE_VERSION = b"\x00\x01\x00\x02"

def read_string(savefile, encoding):
    return savefile.read(31).strip(b"\x00").decode(encoding)

def read(filename, encoding):
    with open(filename, "rb") as savefile:
        signature = savefile.read(24)
        assert signature[:17] == SAVEFILE_SIGNATURE
        version = savefile.read(4)
        assert version == SAVEFILE_VERSION
        r = savefile.read(1)
        assert r == b"R"

        player_name = read_string(savefile, encoding)
        savefile_name = read_string(savefile, encoding)

        save_day, save_month, save_year = struct.unpack(">3h", savefile.read(6))
        save_time , *_ = struct.unpack(">i", savefile.read(4))
        
        ingame_month, ingame_day, ingame_year = struct.unpack(">3h", savefile.read(6))
        ingame_time , *_ = struct.unpack(">i", savefile.read(4))

        map_level, map_number = struct.unpack(">2h", savefile.read(4))
        map_name = read_string(savefile, encoding)

        return {
            "player": {
                "name": player_name,
            },
            "savefile": {
                "name": savefile_name,
                "date": (save_day, save_month, save_year, save_time),
            },
            "game": {
                "date": (ingame_day, ingame_month, ingame_year, ingame_time),
                "map": {
                    "level": map_level,
                    "number": map_number,
                    "name": map_name,
                }
            }
        }
