def solution(n):
    if n >= 10 and n <= 99:
        n_string = str(n)

        n_list = list(n_string)

    else:
        return "Error: n is not a two-digit number."


if __name__ == "__main__":
    print (solution(10))