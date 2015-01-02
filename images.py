#!/usr/bin/python
from json import loads
from subprocess import call
with open('images/images.json') as f:
    sets = loads(f.read())

for s in sets:
    print "Processing " + s["name"]
    for target in s["targets"]:
        data = s["targets"][target]
        if data["type"] == "scale":
            cmd = ["convert", s["source"], "-resize", data["size"], s["path"] + target]
        elif data["type"] == "scale-crop":
            w,h = int(data["size"].split("x")[0]), int(data["size"].split("x")[1])
            resize = "x" + str(h)
            if w > h:
                resize = str(w) + "x"
            cmd = ["convert", s["source"], "-resize", resize, "-gravity", "Center", "-crop", data["size"]+"+0+0", "+repage", s["path"] + target]
        elif data["type"] == "crop":
            cmd = ["convert", s["source"], "-gravity", "Center", "-crop", data["size"]+"+0+0", "+repage", s["path"] + target]

        call(cmd)
