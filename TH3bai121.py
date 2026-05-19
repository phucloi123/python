# ─────────────────────────────────────────────────────────────
# Strobogrammatic Number Generator
# ─────────────────────────────────────────────────────────────

# Pairs valid when rotated 180°: 0↔0, 1↔1, 6↔9, 8↔8, 9↔6
STROBO_PAIRS = [('0', '0'), ('1', '1'), ('6', '9'), ('8', '8'), ('9', '6')]
STROBO_DIGITS = ['0', '1', '6', '8', '9']


# ─────────────────────────────────────────────────────────────
# PART A: Pure strobogrammatic — rotated 180° = itself
# Outside-in recursion (đệ quy từ ngoài vào trong)
# ─────────────────────────────────────────────────────────────
def get_strobogrammatic(n: int, total: int = None) -> list[str]:
    if total is None:
        total = n

    # Base cases
    if n == 0: return [""]
    if n == 1: return ["0", "1", "8"]

    inner_results = get_strobogrammatic(n - 2, total)
    result = []

    for inner in inner_results:
        for left, right in STROBO_PAIRS:
            # Skip leading zero at outermost layer
            if n == total and left == '0':
                continue
            result.append(f"{left}{inner}{right}")

    return result


# ─────────────────────────────────────────────────────────────
# PART B: Extended strobogrammatic — digits ∈ {0,1,6,8,9},
#         rotated result is still a valid number (no leading zero)
# Left-to-right backtracking (quay lui từ trái sang phải)
# ─────────────────────────────────────────────────────────────
def get_extended_strobogrammatic(n: int) -> list[str]:
    result = []

    def backtrack(position: int, buffer: list[str]):
        if position == n:
            result.append("".join(buffer))
            return

        for digit in STROBO_DIGITS:
            # No leading zero
            if position == 0 and digit == '0':
                continue
            # Last digit can't be '0': when rotated → becomes leading zero
            if position == n - 1 and digit == '0':
                continue

            buffer.append(digit)
            backtrack(position + 1, buffer)
            buffer.pop()  # backtrack

    backtrack(0, [])
    return result


# ─────────────────────────────────────────────────────────────
# Helper: Print formatted grid
# ─────────────────────────────────────────────────────────────
def print_results(label: str, numbers: list[str], columns: int = 10):
    print(f"\n{label} ({len(numbers)} numbers):")
    print("─" * 55)
    for i, num in enumerate(numbers, 1):
        print(f"{num:>8}", end="")
        if i % columns == 0:
            print()
    if len(numbers) % columns != 0:
        print()


# ─────────────────────────────────────────────────────────────
# Main
# ─────────────────────────────────────────────────────────────
def main():
    try:
        n = int(input("Enter n (2 <= n <= 10): "))
        if not (2 <= n <= 10):
            raise ValueError
    except ValueError:
        print("Invalid input. n must be an integer between 2 and 10.")
        return

    part_a = get_strobogrammatic(n)
    print_results(f"Part a — Pure Strobogrammatic ({n} digits)", part_a)

    part_b = get_extended_strobogrammatic(n)
    print_results(f"Part b — Extended Strobogrammatic ({n} digits)", part_b)


if __name__ == "__main__":
    main()