# Student ID : 52721
# Course     : Survey of Programming Languages — KU-SoPL-2026
#
# ╔══════════════════════════════════════════════════════════╗
# ║  YOUR TASK                                               ║
# ║                                                          ║
# ║  Return the sum of digits at positions 3, 4, and 5 (1-indexed).║
# ║                                                          ║
# ║  - digits are extracted from your ID string              ║
# ║  - ignore the "-ex" suffix if present                    ║
# ╚══════════════════════════════════════════════════════════╝
#
# Implement solve() below and return an integer.
# Do NOT rename this file.
# Run with:  python task_52721.py


def solve(id: str) -> int:
    clean_id = id.replace("-ex", "").replace("_ex", "")
    return sum(int(clean_id[i]) for i in [2, 3, 4])

if __name__ == "__main__":
    print(solve("52721"))