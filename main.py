import json
import fileinput
from os import getcwd, path, makedirs, listdir, rmdir
import pathlib
import re
from shutil import rmtree


def executeReplace(match: re.Match[str]):
    key = match.group(0)[1:-1]
    return values[key]


def replaceStr(inStr: str):
    return re.sub(regex, executeReplace, inStr)


def processTemplate(filename: str):
    templatepath = path.join(getcwd(), "templates", filename)
    template = open(templatepath)
    templateContents = template.read()
    template.close()
    outfile = open(
        path.join(
            outDir, ("_historybuilder." + modname + "." + filename[0:-14] + ".json")
        ),
        "x",
    )
    outfile.write(replaceStr(templateContents))
    outfile.close()


def loopFiles():
    for i in listdir(path.join(getcwd(), "templates")):
        processTemplate(i)


def main():
    global regex
    global values
    global outDir
    global modname
    regex = re.compile(r"\{[A-Z1-9_]+?\}")
    args: str = ""
    for line in fileinput.input(encoding="utf-8"):
        modname = fileinput.filename().split(".")[0]
        args += line + "\n"
    global values
    values = json.loads(args)
    cwd = getcwd()
    rmtree(path.join(cwd, "_" + modname), ignore_errors=True)
    makedirs(path.join(cwd, "_" + modname), exist_ok=True)
    outDir = path.join(cwd, "_" + modname)
    loopFiles()


if __name__ == "__main__":
    main()
