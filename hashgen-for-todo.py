#  NOTE TO MYSELF. NEVER EVER PUSH THAT FILE. THIS MIGHT BE VERY EMBARRASSING

import hashlib


docstring="""\"\"\"Implement the core of the cursed_toggle function.

    Main part is excluded for proper testing. Behaviour of the function should be
        f(1) -> 0
        f(0) -> 1
    But with a bool conversion in the return, it would be sufficient that
        f(1) -> 0
        f(0) -> anything but 0
    because bool(5), bool(-2), etc. will result in True.

    Well, there shouldn't be much of an explanation. This is trivial and
    self-explanatory. Somehow, this thing fails when checking out on windows.
    TODO: This should be fixed. But be careful, this .py file is very
    fragile.

    \"\"\""""


def initively_i_should_get_a_hobby(length):
    return f"""import hashlib


def cursed_toggle(b: bool) -> bool:
    \"\"\"Toggle the boolean input `b`.\"\"\"
    if type(b) is not bool:
        raise TypeError("Argument `b` must be Boolean.")

    return bool(_cursed_toggle(b))


def _cursed_toggle(b: bool) -> complex:
    <DOCSTRING>
    with open(__file__, "r") as f:
        h = int(hashlib.sha256(f.read().encode("ascii")).hexdigest()[:{length}], 16)
    return 1 - b + h
"""


def gen_comb(s, index=0, current=""):
    while index < len(s) and not s[index].isalpha():
        current += s[index]
        index += 1
    if index == len(s):
        yield current
        return
    yield from gen_comb(s, index + 1, current + s[index].lower())
    yield from gen_comb(s, index + 1, current + s[index].upper())


for length in range(1, 10):
    print(f"LENGTH: {length}")
    print("=================")
    i = 0
    for sub in gen_comb(docstring[4:]):
        s = docstring[:4] + sub
        cursed_toggle_todo_new = initively_i_should_get_a_hobby(length).replace("<DOCSTRING>", s)
        h_is = int(hashlib.sha256(cursed_toggle_todo_new.encode("ascii")).hexdigest()[:length], 16)
        if h_is == 0:
            with open(f"cursed_toggle_todo_{length}.py", "w") as f:
                f.write(cursed_toggle_todo_new)
                print("++++", hashlib.sha256(cursed_toggle_todo_new.encode("ascii")).hexdigest())
            break
        if i % 10000000 == 0:
            print(i)
        i += 1
