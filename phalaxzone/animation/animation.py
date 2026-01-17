import subprocess
from termcolor import colored
import time

def call_fig() -> str:
    """Call external script and return its output as text."""
    try:
        result = subprocess.run(
            ["./phx.sh"],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout
    except (FileNotFoundError, subprocess.CalledProcessError, OSError):
        return "PhalaxZone"
    
def animated_banner(text):
    eagle = r'''
           ///,        ////
           \  /,      /  >.
            \  /,   _/  /.
             \_  /_/   /.
              \__/_   <
              /<<< \_\_
             /,)^>>_._ \
             (/   \\ /\\\
                  // ````
                 ((`    
    '''
    for line in text.splitlines():
        print(colored(line, 'grey', attrs=['bold']))
        time.sleep(0.04)
    for line in eagle.splitlines():
        print(colored(line, 'grey', attrs=['blink']))
        time.sleep(0.04)
    author_text = "Author: @cyb2rS2c"
    for char in author_text:
        print(colored(char, 'red'), end='', flush=True)
        time.sleep(0.03)
    print("\n")
