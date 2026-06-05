# Student ID : 52670
# Course     : Survey of Programming Languages — KU-SoPL-2026
#
# ╔══════════════════════════════════════════════════════════╗
# ║  YOUR TASK                                               ║
# ║                                                          ║
# ║  Return the count of digits divisible by 5 (i.e., 0 or 5).║
# ║                                                          ║
# ║  - digits are extracted from your ID string              ║
# ║  - ignore the "-ex" suffix if present                    ║
# ╚══════════════════════════════════════════════════════════╝
#
# Implement solve() below and return an integer.
# Do NOT rename this file.
# Run with:  python task_52670.py


def solve(id: str) -> int:
    clean = id.replace("-ex", "").replace("_ex", "")
    return sum(1 for ch in clean if ch in "05")


if __name__ == "__main__":
    print(solve("52670"))
