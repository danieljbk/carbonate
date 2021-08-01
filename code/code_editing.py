# convert problematic characters to lookalike unicode characters: https://unicode-table.com/en/
def replace_problematic_characters(code):
    # for " and ', can't do replace() because the beginning and end quote should be differentiated
    code = list(code)
    while '"' in code:
        for i in range(len(code)): # look for beginning quote first
            if code[i] == '"':
                code[i] = '“'
                break
        for i in range(len(code)): # then look for end quote
            if code[i] == '"':
                code[i] = '”'
                break
    while "'" in code:
        for i in range(len(code)):  # look for beginning quote first
            if code[i] == "'":
                code[i] = "‘"
                break
        for i in range(len(code)):  # then look for end quote
            if code[i] == "'":
                code[i] = "’"
                break
    code = ''.join(code)

    # replacing lots of characters with unicode lookalikes
    code = code.replace('{', '❴')
    code = code.replace('}', '❵')
    code = code.replace('(', '❪')
    code = code.replace(')', '❫')
    code = code.replace(')', '❫')
    # https://unicode-table.com/en/blocks/box-drawing/
    code = code.replace('/', '󠀠╱')
    # https://unicode-table.com/en/blocks/box-drawing/, greek letter nu could be useful
    code = code.replace('\\n', '╲n') # doing this to preserve actual typed newlines ('\n') inside code
    code = code.replace("\r", "\\r")
    code = code.replace("\n", "\\n")
    while list(code)[:2] == ['\\', 'n']: # automatically get rid of empty lines in the beginning
        code = "".join(list(code)[2:])
    if list(code)[-2:] != ['\\', 'n', '\\', 'n', ]: # automatically add an empty line in the end
        code += '\\n'

    return code
