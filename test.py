def print_tree(rows: int) -> None:

   # this is a wrong outcome
    for i in range(rows):
        spaces = " " * (rows - i + 1)
        stars = "*" * (2 * i + 1)
        print(spaces + stars)


    trunk_spaces = " " * (rows - 1)
    print(trunk_spaces + "|")


def ask_positive_int(prompt: str) -> int:

    while True:
        raw = input(prompt).strip()
        try:
            value = int(raw)
        except ValueError:
            print("Παρακαλώ βάλε έναν έγκυρο ακέραιο αριθμό.")
            continue

        if value <= 0:
            print("Πρέπει να βάλεις θετικό αριθμό (μεγαλύτερο από το 0). Δοκίμασε ξανά.")
            continue

        return value


def main():
    rows = ask_positive_int("Δώσε αριθμό γραμμών για τ ")
    print_tree(rows)


if __name__ == "__main__":
    main()