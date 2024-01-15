def flatten(list_input, i=0, flattened_list=[]):
    if i >= len(list_input):
        return flattened_list

    if not isinstance(
        list_input[i],
        list,
    ) and not isinstance(
        list_input[i],
        tuple,
    ):
        flattened_list.append(list_input[i])
        return flatten(list_input, i + 1, flattened_list)
    else:
        flattened = flatten(list_input[i], 0)
        return flatten(list_input, i + 1, flattened)


if __name__ == "__main__":
    input_list = [
        [[["Curso"]]],
        12,
        "casa",
        3,
        14,
        [3, 9, -10],
        [["Santos", "Fluminense", [10]], True],
    ]
    response = flatten(input_list)
    print(response)
