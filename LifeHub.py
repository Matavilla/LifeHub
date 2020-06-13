"""
Данный модуль отвечает за запуск игры с предварительной инициализацией
параметров вселенной.
"""

import GUI
import src
import os
import sys
import gettext


def main():
    gettext.install("locale", os.path.dirname(sys.argv[0]), names=("ngettext",))
    wPar = GUI.WorldParameters()
    GUI.StartMenu(wPar)
    if not wPar:
        print("[ERROR]     WrongParametersWorld")
        raise SystemExit(1)
    wPar.print_in_log()
    handler = src.Handler(wPar)
    handler.create_world()
    GUI.StartGame(handler)

    
if __name__ == '__main__':
    main()
