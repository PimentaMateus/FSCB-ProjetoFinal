def som(): # decibeis 
    return 120


def led(): # ai liga on/off no cayanne
    if som() > 100:
        return 'ON'
    else:
        return 'OFF'
