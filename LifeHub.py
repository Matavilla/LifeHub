import GUI

wPar = GUI.WorldParameters()
GUI.StartMenu(wPar)
if not wPar.check():
    print("[ERROR]     WrongParametersWorld")
    raise SystemExit(1)
GUI.PrintParam(wPar)
GUI.StartGame(wPar)
#generate world
#construct handler and run pygame
