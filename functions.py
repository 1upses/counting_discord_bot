def get_number(filepath: str) -> int:
    with open(filepath, "r") as f: return int(f.read().splitlines()[0])

def get_user(filepath: str) -> str:
    with open(filepath, "r") as f: return f.read().splitlines()[1]

def update_data(filepath: str, number: int, user: str) -> None:
    with open(filepath, "w") as f:
        f.write(str(number + 1) + '\n')
        f.write(user)