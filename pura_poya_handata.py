# python
import sys
import time
from typing import List, Union, Tuple

CYAN = '\033[36m'
RESET = '\033[0m'

TARGET_INDEX = 10        # zero-based index after which to pause
POST_LINE_DELAY = 12  # seconds to sleep after that line ends


print(CYAN + "Pura Poya Hadata Lyrics!" + RESET)

# Each item can be:
# - a plain string -> uses the default per-character delay
# - a tuple/list (line_text, delay_seconds) -> uses that per-character delay for the whole line
# python
lyrics = [
    ("මුතු මාල පොටක් ගෙලේ බදින දා", 0.15),
    ("සිත කොල සිතුම් එබී බලන දා", 0.18),
    ("රෑ නින්ද නැතිව හීන දුටුව දා", 0.18),
    ("හිත ආදරයක බැඳුනි ද මන්දා", 0.2),
    ("                         ", 0.04),


    ("පුර පෝය හඳට පෙමින් බැඳුනු තාරකා ළඳුන්", 0.15),
    ("ගී හඬින් කියන පෙම් කතාව අසාගෙන වරෙන්", 0.15),
    ("නීල වළාවේ", 0.2),
    ("ඇගෙ පෙම් කතාව අසාගෙන වරෙන්", 0.2)
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
