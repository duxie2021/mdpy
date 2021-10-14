

statement_list = []


def push(statement):
    statement_list.append(statement)


def pop(statement):
    assert(statement_list[-1] == statement)
    return statement_list.pop()


def peak():
    return statement_list[-1]
