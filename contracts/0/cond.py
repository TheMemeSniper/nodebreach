import os

# This is a test condition for a contract involving the destruction of boot.sys at 0.0.0.0
def go():
    if os.path.exists("/terminals/0.0.0.0/filesystem/sys/boot.sys"):
        return False
        print("false...")
    else:
        return True
        print("tru")
go()
