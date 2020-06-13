import GUI
import src

def main():

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
