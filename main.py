def define(word):
    word = word.lower()
    if word == "zenith":
        return "the highest point of something"
    elif word == "zealot":
        return "a fervent and even militant proponent of something"
    elif word == "yearn":
        return "desire strongly or persistently"
    elif word == "yawner":
        return "a person who yawns"
    elif word == "xenophobia":
        return "a fear of foreighners or strangers"
    elif word == "x-axis":
        return "the horizontal axis in a plane coordinate system"
    elif word == "wonky":
        return "turned or twisted toward one side"
    elif word == "wanton":
        return "a lewd or immoral person" 
    elif word == "vermillion":
        return "of a vivid red to reddish-orange color"
    elif word == "vague":
        return "lacking clarity or distinctness"
    else:
        return "that word is not in our dictionary"
print(define("zenith"))
print(define("pizza"))