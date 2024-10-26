import sys
from math import lcm

if __name__ == "__main__":
    if len(sys.argv) != 4:
        f, c, b = int(input("Front: ")), int(input("Center: ")), int(input("Back: "))
    else: 
        f, c, b = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
        print(f"Using:\tFront = {f}, Center = {c}, Back = {b}\n\tlcm={lcm(f, c, b)}")

    a_f, a_c, a_b = [int((1/i) * lcm(f, c, b)) for i in [f, c, b]]

    print(f"\n=== COPY AND PASTE BELOW ===")
    print(f"{a_f}f1 + {a_f}f2 + {a_f}f3 + {a_f}f4  -  {a_c}c1 - {a_c}c2 - {a_c}c3 - {a_c}c4 = 0;  /* F vs C */")
    print(f"{a_f}f1 + {a_f}f2 + {a_f}f3 + {a_f}f4  -  {a_b}b1 - {a_b}b2 - {a_b}b3 - {a_b}b4 = 0;  /* F vs B */")
    print(f"{a_b}b1 + {a_b}b2 + {a_b}b3 + {a_b}b4  -  {a_c}c1 - {a_c}c2 - {a_c}c3 - {a_c}c4 = 0;  /* B vs C */")
