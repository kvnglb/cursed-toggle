import argparse
import sys
import time
import typing as t

from cursed_toggle import cursed_toggle


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

    if args.v == 0:
        print(ret)
    elif args.v == 1:
        print("{} {}".format(module_name, ret))
    elif args.v == 2:
        print("{} {} {}".format(time.strftime("%Y"), module_name, ret))
    elif args.v == 3:
        print("{} {} {}".format(time.strftime("%Y-%m"), module_name, ret))
    elif args.v == 4:
        print("{} {} {}".format(time.strftime("%Y-%m-%d"), module_name, ret))
    elif args.v == 5:
        print("{} {} {}".format(time.strftime("%Y-%m-%d %H"), module_name, ret))
    elif args.v == 6:
        print("{} {} {}".format(time.strftime("%Y-%m-%d %H:%M"), module_name, ret))
    elif args.v >= 7:
        print("{} {} {}".format(time.strftime("%Y-%m-%d %H:%M:%S"), module_name, ret))

    return 0


parser = argparse.ArgumentParser("cursed-toggle CLI application")
parser.add_argument("b", help="Boolean value `True` or `False` (case-insensitive)")
parser.add_argument("-v", action="count", default=0, help="verbose mode (multiple -v options increase the verbosity)")
args = parser.parse_args()

sys.exit(main(args))
