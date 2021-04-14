import os


def run(**args):
    print("[*] In dirlister moduler.")
    files = os.listdir(".")

    return str(files)