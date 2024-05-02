'''Посчитать комментарии в заданном коде'''

def count_elements(code):
    # переменная отслеживает состояние
    state = 'code'
    comment1, comment2, comment3, literal_strings = 0, 0, 0, 0
    i = 0
    # comment1: (* text *)
    # comment2: { text }
    # comment3: // text \n
    # literal_strings: ' литеральная строка '

    while i < len(code):
        if state == 'code':
            if code[i:i+2] == '(*':
                state = 'comment1'
                i += 1
            elif code[i] == '{':
                state = 'comment2'
            elif code[i:i+2] == '//':
                state = 'comment3'
                i += 1
            elif code[i] == "'":
                state = 'literal_strings'
        elif state == 'comment1':
            if code[i:i+2] == '*)':
                state = 'code'
                comment1 += 1
                i += 1
        elif state == 'comment2':
            if code[i] == '}':
                state = 'code'
                comment2 += 1
        elif state == 'comment3':
            if code[i] == '\n':
                state = 'code'
                comment3 += 1
        elif state == 'literal_strings':
            if code[i] == "'":
                state = 'code'
                literal_strings += 1
        i += 1

    return comment1, comment2, comment3, literal_strings

code = """
program test;
(*just for testing *)
var
(* variables
note that
// here is not comment
and (* here is
not a begin of
another comment
*)
x: integer; (* *)
begin
write('(*is not comment//');
write(' and (*here*) '
,x // y);
End. // It is comment
"""
print(count_elements(code))  # Вывод: (3, 0, 2, 2)

