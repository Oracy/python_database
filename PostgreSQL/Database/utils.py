def check_dynamic_column(columns):
    columns = "*" if columns == None else columns
    return columns


def check_dynamic_condition(condition):
    condition = "1=1" if condition == None else condition
    return condition