define e = Character('Eileen', color="#c8ffc8")
define m = Character('Me', color="#c8c8ff")
image bg beached = "images/beached.jpg"
image Eileen:
    "images/eileen.png"
    zoom 1.3

label start:
    
    scene bg beached
    show Eileen

    e "Hey, can you go try and shoot some people for me."
    
    m "Sure I will be right back."
    
    call begin_hunt
    
    scene bg beached
    show Eileen
    
    if targets_hit == 0:
        e "You didn't hit anyone, I am going to find someone else."
        scene black with dissolve
        "and the hero died alone with no-one to love him."
    if targets_hit > 0:
        e "[targets_hit] of your shots ended up killing someone.  Lets get married"
        scene black with dissolve
        "and they lived happily ever after"
    

    "Game Over"

    return
