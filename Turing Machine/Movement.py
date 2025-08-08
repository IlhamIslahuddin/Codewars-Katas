def read(tape, head, moves):
    if len(moves) == 0:
        return ""
    position = head
    output = tape[head]
    for i in range(len(moves)-1):
        if moves[i] == ">":
            head += 1
        else:
            head -= 1
        output += tape[head]
    return output
