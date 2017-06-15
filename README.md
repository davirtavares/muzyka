# muzyka
py3status module for showing the currently playing song on Spotify Web Player

This module uses Chrome DevTools Protocol to detect if there are any songs being played on Spotify Web Player, and can also be extended to support other players.

## Installation

Clone/download this repository and place the main Python module (muzyka.py) on $HOME/.i3/py3status/ (or other place you use to put your py3status modules), and activate it on your i3status config file:

```
order += "muzyka"
```

## Current limitations

- You cannot format the output (always: artis - track name)
- Requires Chrome running with remote debug enabled (google-chrome --remote-debugging-port=9222)
- Only supports Spotify Web Player for now
