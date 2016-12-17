import cx_Freeze

executables = [cx_Freeze.Executable("RockRace.py")]

cx_Freeze.setup(
    name= "Rock Race",
    options={"build_exe":{"packages": ["pygame"],
                          "include_files":["racecar.png", "rock.png", "BG.jpg", "shift.wav","crash.wav"]}},
    executables = executables
    )
