import GUI
import src

wPar = GUI.WorldParameters()
GUI.StartMenu(wPar)
if not wPar:
    print("[ERROR]     WrongParametersWorld")
    raise SystemExit(1)
wPar.print_in_log()
handler = src.Handler(wPar)
handler.create_world()
GUI.StartGame(handler)
