import pyxel

def handleKeys(key, pos):
    if key:
        pyxel.blt(
            x=pos[0], y=pos[1],
            img=1, 
            u=26, v=0,
            w=5, h=6,
            colkey=0
        )
    else:
        pyxel.blt(
            x=pos[0], y=pos[1],
            img=1, 
            u=21, v=0,
            w=5, h=6,
            colkey=0
        )

def handleHearts(life):
    if life > 1:
        if life < 3:
            pyxel.blt(
                x=2, y=3,
                img=1, 
                u=0, v=0,
                w=7, h=6,
                colkey=0
            )
            
            pyxel.blt(
                x=9, y=3,
                img=1, 
                u=0, v=0,
                w=7, h=6,
                colkey=0
            )
            
            pyxel.blt(
                x=16, y=3,
                img=1, 
                u=14, v=0,
                w=7, h=6,
                colkey=0
            )
        
        else:
            pyxel.blt(
                x=2, y=3,
                img=1, 
                u=0, v=0,
                w=7, h=6,
                colkey=0
            )
            
            pyxel.blt(
                x=9, y=3,
                img=1, 
                u=0, v=0,
                w=7, h=6,
                colkey=0
            )
            
            pyxel.blt(
                x=16, y=3,
                img=1, 
                u=0, v=0,
                w=7, h=6,
                colkey=0
            )
        
    else:
        pyxel.blt(
            x=2, y=3,
            img=1, 
            u=0, v=0,
            w=7, h=6,
            colkey=0
        )
        
        pyxel.blt(
            x=9, y=3,
            img=1, 
            u=14, v=0,
            w=7, h=6,
            colkey=0
        )
        
        pyxel.blt(
            x=16, y=3,
            img=1, 
            u=14, v=0,
            w=7, h=6,
            colkey=0
        )