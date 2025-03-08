import argparse
import inspect
import sys
import time
import typing as t

from cursed_toggle import _cursed_toggle, cursed_toggle


def main(args: argparse.Namespace) -> t.Union[int]:
    """Make the cursed-toggle library CLI capable."""
    module_name = cursed_toggle.__module__

    if args.b.lower() == "false":
        b = False  # type: t.Union[bool, str]
    elif args.b.lower() == "true":
        b = True
    elif args.b.lower() == "talse":
        b = "Frue"
        module_name = "Never gonna give you"
    elif args.b.lower() == "frue":
        b = "Talse"
        module_name = "Never gonna let you"
    else:
        raise TypeError("`b` must be boolean: `True` or `False` (case-insensitive).")

    if type(b) is bool:
        ret = cursed_toggle(b)  # type: t.Union[bool, str]
    else:
        ret = b

    verb = ""
    if args.v >= 1:
        verb = "module name: {}".format(module_name)

    if args.v == 2:
        verb = "current date: {}\n".format(time.strftime("%Y")) + verb
    elif args.v == 3:
        verb = "current date: {}\n".format(time.strftime("%Y-%m")) + verb
    elif args.v >= 4:
        verb = "current date: {}\n".format(time.strftime("%Y-%m-%d")) + verb

    if args.v == 5:
        verb = "current time: {}\n".format(time.strftime("%H")) + verb
    elif args.v == 6:
        verb = "current time: {}\n".format(time.strftime("%H:%M")) + verb
    elif args.v >= 7:
        verb = "current time: {}\n".format(time.strftime("%H:%M:%S")) + verb

    if args.v >= 8:
        verb += "\n\nsource function\n"
        verb += 15*"=" + "\n"
        if type(b) is not str:
            verb += "{}\n".format(inspect.getsource(_cursed_toggle))
        else:
            verb += 10*"Error" + "\n"
        verb += 15*"="

    if verb:
        ret = "{}\n{}".format(verb, ret)

    print(ret)
    return 0


parser = argparse.ArgumentParser("cursed-toggle CLI application")
parser.add_argument("b", help="Boolean value `True` or `False` (case-insensitive)")
parser.add_argument("-v", action="count", default=0, help="verbose mode (multiple -v options increase the verbosity)")
args = parser.parse_args()

sys.exit(main(args))
