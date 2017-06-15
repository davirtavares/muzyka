# -*- coding: utf-8 -*-

import sys
from urlparse import urlparse
import re
import json

from chromote import Chromote

STATUS_SELECTOR = ".player-controls .spoticon-pause-16"
ARTIST_SELECTOR = ".track-info .track-info__artists a"
TRACK_SELECTOR = ".track-info .track-info__name a"

class Py3status(object):
    def __tab_eval(self, tab, code):
        res = json.loads(tab.evaluate(code))

        if res["result"].has_key("exceptionDetails"):
            return ""

        return res["result"]["result"]["value"]

    def muzyka(self):
        chrome = Chromote()

        for tab in chrome.tabs:
            u = urlparse(tab.url)

            if re.match(r"[^.]*.spotify.com", u.netloc):
                if self.__tab_eval(tab, 'document.querySelector("' + STATUS_SELECTOR + '").getAttribute("title")') == "Pause":
                    artist_name = self.__tab_eval(tab, 'document.querySelector("' + ARTIST_SELECTOR + '").innerHTML')
                    track_name = self.__tab_eval(tab, 'document.querySelector("' + TRACK_SELECTOR + '").innerHTML')

                    return {
                        "full_text": u"♪ " + artist_name + " - " + track_name,
                        "cached_until": 1,
                    }

        return {
            "full_text": "",
            "cached_until": 1,
        }

if __name__ == "__main__":
    from py3status.module_test import module_test

    module_test(Py3status)
