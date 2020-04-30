from enum import IntEnum, auto


class Color(IntEnum):
  black = 0
  red = auto()
  green = auto()
  yellow = auto()
  blue = auto()
  purple = auto()
  cyan = auto()
  white = auto()
  default = auto()


class Decoration(IntEnum):
  bold = 1
  underline = 4
  default = 9


def generate_message(txt, fg=Color.default, bg=Color.default, decoration=Decoration.default):
  output = "\033["

  if fg != Color.default:
    output += f"3{fg}"
  
  if bg != Color.default:
    output += f";4{bg}"
  
  if decoration != decoration.default:
    output += f";{decoration}"
  
  output += "m"
  output += txt
  output += "\033[m"

  return output


def format_text(header, txt, fg=Color.default, bg=Color.default, decoration=Decoration.default):
  return generate_message(f" {header} ", fg, bg, decoration) + " " + generate_message(txt)


def success(txt):
  print(format_text(header="SUCC", txt=txt, fg=Color.white, bg=Color.green, decoration=Decoration.bold))


def info(txt):
  print(format_text(header="INFO", txt=txt, fg=Color.white, bg=Color.cyan, decoration=Decoration.bold))


def warn(txt):
  print(format_text(header="WARN", txt=txt, fg=Color.white, bg=Color.yellow, decoration=Decoration.bold))


def error(txt):
  print(format_text(header="ERR!", txt=txt, fg=Color.white, bg=Color.red, decoration=Decoration.bold))


def ask(txt):
  input(format_text(header="", txt=txt, fg=Color.white, bg=Color.blue, decoration=Decoration.bold))