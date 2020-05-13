import GUI

wPar = GUI.WorldParameters()
GUI.StartMenu(wPar)
if not wPar.check():
   raise WrongParametersWorld
GUI.PrintParam(wPar)
#generate world
#construct handler and run pygame
