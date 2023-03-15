#!/usr/bin/python

import json
import subprocess
import animate_text

PAUSE_MEDIA = False

process = subprocess.Popen(
        "waybar-mpris --autofocus --order TITLE".split(),
         stdout=subprocess.PIPE
    )

print(json.dumps({"class":"none","text":""}))

prev = ""
for line in iter(lambda: process.stdout.readline().decode("utf-8") if process.stdout else "", b""):
        dat = json.loads(line)
        if (not PAUSE_MEDIA):
            if "text" in dat:
                if dat["text"] == prev:
                    continue
                prev = dat["text"]
                for text in animate_text.anim(dat["text"], "mpris"):
                    dat["text"] = text
                    print(json.dumps(dat),flush=True)
            else:
                print({"class":"none","text":""})