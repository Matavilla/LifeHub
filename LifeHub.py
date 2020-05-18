import GUI
import src

wPar = GUI.WorldParameters()
GUI.StartMenu(wPar)
if not wPar.check():
    print("[ERROR]     WrongParametersWorld")
    raise SystemExit(1)
GUI.PrintParam(wPar)
handler = src.Handler(wPar)
handler.create_world()
GUI.StartGame(wPar, handler)
