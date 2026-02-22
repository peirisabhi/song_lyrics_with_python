# python
import sys
import time
from typing import List, Union, Tuple

CYAN = '\033[36m'
RESET = '\033[0m'

TARGET_INDEX = 10        # zero-based index after which to pause
POST_LINE_DELAY = 12  # seconds to sleep after that line ends


print(CYAN + "Saiyaara Lyrics!" + RESET)

# Each item can be:
# - a plain string -> uses the default per-character delay
# - a tuple/list (line_text, delay_seconds) -> uses that per-character delay for the whole line
# python
lyrics = [
    ("Tu paas hai, mere paas hai aise", 0.2),
    ("Mera koi ehsaas hai jaise", 0.2),
    ("Tu paas hai, mere paas hai aise", 0.2),
    ("Mera koi ehsaas hai jaise", 0.2),
    ("                         ", 0.04),


    ("Haaye, main mar hee jaaun", 0.15),
    ("jo tujhko na paaun", 0.15),
    ("Baaton mein teri main raatein bitaun", 0.15),
    ("Hothon pe lamha-lamha hai", 0.15),
    ("naam tera, haaye", 0.15),
    ("Tujhko hee gaaun main, tujhko pukaarun", 0.19),
    ("                         ", 0),

    ("Saiyaara, tu to badla nahi hai", 0.23),
    ("Mausam zara sa rootha hua hai", 0.23),
    ("Saiyaara, tu to badla nahi hai", 0.23),
    ("Mausam zara sa rootha hua hai (Hai)", 0.23),
]

DEFAULT_DELAY = 0.21

def display_lyrics(line: str, delay: float = DEFAULT_DELAY, callback=None):
    for char in line:
        sys.stdout.write(CYAN + char + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('\n')
    if callback:
        callback()

def sing_song(lines: List[Union[str, Tuple[str, float]]], current_line: int = 0):
    if current_line >= len(lines):
        return

    item = lines[current_line]
    if isinstance(item, (list, tuple)) and len(item) >= 2:
        line_text = str(item[0])
        try:
            line_delay = float(item[1])
        except Exception:
            line_delay = DEFAULT_DELAY
    else:
        line_text = str(item)
        line_delay = DEFAULT_DELAY

    def _next():
        if current_line == TARGET_INDEX:
            time.sleep(POST_LINE_DELAY)
        sing_song(lines, current_line + 1)

    display_lyrics(
        line_text,
        delay=line_delay,
        callback=_next
    )

sing_song(lyrics)
