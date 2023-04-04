from src.constants import *

def __init__():
    # init
    initialize_ffmpeg()
    # main
    from src.main import main
    main()
