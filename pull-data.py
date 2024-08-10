import sys
import json

data = json.loads(sys.argv[2])

units = [
    "unit0", 
    "unit1", 
    "unit2", 
    "unit3", 
    "unit4", 
    "unit5", 
    "unit6", 
    "unit7",
    "unit8",
    "unit9",
    "unit10",
    "unit11",
    "unit12",
    "unit13"
    ]

for u in units:
    try:
        rows = data[u]
        with open("recorded-lectures/%s_data.md" % u, "w") as f:
            file_string = ""
            for r in rows:
                row_string = "|"
                for c in r:
                    row_string = row_string + c + "|"
                row_string = row_string + "\n"
                file_string = file_string + row_string
            f.write(file_string)
            print(file_string)
        print(u + " saved")
    except KeyError:
        continue