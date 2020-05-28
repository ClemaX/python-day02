def ft_reduce(function_to_apply, list_of_inputs):
    result = list_of_inputs[0]
    for i in list_of_inputs[1:]:
        result = function_to_apply(result, i)
    return result
