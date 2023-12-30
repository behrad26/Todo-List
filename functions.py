def add(filepath: str, item: str) -> None:
    with open(filepath, "a") as file:
        file.write("\n" + item)


def remove(filepath: str, index: int) -> None:
    with open(filepath, "r") as file:
        todos = file.read().split("\n")
    todos.remove(todos[index])
    with open(filepath, "w") as file:
        file.write("\n".join(todos))


def edit(filepath: str, index: int, item: str) -> None:
    with open(filepath, "r") as file:
        todos = file.read().split("\n")
    todos[index] = item
    with open(filepath, "w") as file:
        file.write("\n".join(todos))


def complete(filepath: str, index: int) -> str:
    with open(filepath, "r") as file:
        todos = file.read().split("\n")
    removing_item = todos[index]
    todos.remove(todos[index])
    with open(filepath, "w") as file:
        file.write("\n".join(todos))
    return removing_item


def read(filepath: str) -> list[str]:
    with open(filepath, "r") as file:
        return file.read().split("\n")[1:]


def numeric_generator_iter(main: list[str], start: int = 0, prefix: str = " ") -> iter:
    for i in range(start, len(main) + start):
        yield f"{i}{prefix}{main[i - start]}"


def numeric_generator_list(main: list, start: int = 0, prefix: str = " ") -> list[str]:
    new_list = []
    for i in range(start, len(main) + start):
        new_list.append(f"{i}{prefix}{main[i - start]}")
    return new_list


def date_check(date1: str, date2: str) -> bool:
    date1 = date1.split("/")
    date2 = date2.split("/")

    new_day = False
    if int(date1[2]) > int(date2[2]):
        new_day = True
    elif int(date1[0]) > int(date2[0]):
        new_day = True
    elif int(date1[1]) > int(date2[1]):
        new_day = True

    return new_day


if __name__ == "__main__":
    print("please don't run this script directly.")
    print("This is a third party package to use in another script.")
