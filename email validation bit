def email_validation(x):
    a=0
    y=len(x)
    dot=x.find(".")
    at=x.find("@")
    for i in range (0,at):
        if ('a' <= x[i] <= 'z') or ('A' <= x[i] <= 'Z'):
            a = a+1
    if a > 0 and at > 0 and (dot - at) > 0 and (dot + 1) < y:
        return True
    else:
        return False


def FileCheck(fn):
    try:
      open(fn, "r")
      return True
    except IOError:
      return False
