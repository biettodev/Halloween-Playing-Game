import pyxel

import resources
import characters
import handlers

def play_music(ch0, ch1, ch2):
    if ch0:
        pyxel.play(0, 0, loop=True)
    else:
        pyxel.stop(0)

class App:
    
    def __init__(self):
        pyxel.init(52, 80, caption='Halloween Playing Game')
        
        self.gameover = False
        
        self.w = pyxel.width
        self.h = pyxel.height
        
        resources.images()
        
        resources.tilemap()
        pyxel.tilemap(0).refimg = 0
        
        resources.music()
        
        # Characters informations
        characters.skeleton(self)
        self.hh = 1
        characters.shadow(self)
        characters.kids(self)
        
        resources.ui(self)
        
        self.heart = {
            'three': [1, 1, 1],
            'two': [1, 1, 0],
            'one': [0, 0, 0]
        }
        
        play_music(True, True, True)
        
        pyxel.run(self.update, self.draw)
    
    def update(self):
        
        # Checks for Restart
        if self.gameover:
            if pyxel.btnp(pyxel.KEY_R):
                self.gameover = False
                self.skeleton['life'] = 3
                self.skeleton['posx'] = 0
                self.skeleton['posy'] = 0
                self.skeleton['key1'] = False
                self.skeleton['key2'] = False
        
        # Control general keys 
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
            
        if pyxel.btn(pyxel.KEY_LEFT):
            self.skeleton['posx'] -= self.skeleton['speed']
        
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.skeleton['posx'] += self.skeleton['speed']
            
        if pyxel.btn(pyxel.KEY_UP):
            self.skeleton['posy'] -= self.skeleton['speed']
            
        if pyxel.btn(pyxel.KEY_DOWN):
            self.skeleton['posy'] += self.skeleton['speed']
        
        # Controls display limits
        self.skeleton['posx'] = max(
            self.skeleton['posx'], 2
        )
        
        self.skeleton['posx'] = min(
            self.skeleton['posx'], (self.display['w'] + 3) - self.skeleton['width']
        )
        
        self.skeleton['posy'] = max(
            self.skeleton['posy'], 10
        )
        
        self.skeleton['posy'] = min(
            self.skeleton['posy'], (self.display['h'] + 2) - self.skeleton['height']
        ) 
        
        # Checks kid atack
        if self.skeleton['posy'] == self.kids['kid1']['posy'] and (self.skeleton['posx'] == (self.kids['kid1']['posx'] - 10) or self.skeleton['posx'] == (self.kids['kid1']['posx'] - 20)):
            self.skeleton['posx'] = self.skeleton['posy'] = 0
            self.skeleton['life'] -= 1
        
        if self.skeleton['posy'] == self.kids['kid2']['posy'] and ((self.skeleton['posx'] == self.kids['kid2']['posx'] - 5) or (self.skeleton['posx'] == self.kids['kid2']['posx'] + 5)):
            self.skeleton['posx'] = self.skeleton['posy'] = 0
            self.skeleton['life'] -= 1
        
        # Checks key capture
        if self.skeleton['posx'] == 33 and self.skeleton['posy'] == 10:
            self.skeleton['key1'] = True
        
        if self.skeleton['posx'] == self.shadow['posx'] and self.skeleton['posy'] == self.shadow['posy']:
            self.skeleton['key2'] = True
        
        # Checks Game Over
        if self.skeleton['life'] == 0:
            self.gameover = True
            
        # Check Win:
        if self.skeleton['key1'] and self.skeleton['key2']:
            self.skeleton['win'] = True
            self.gameover = True
            
    def draw(self):
        
        if not self.gameover:
            pyxel.cls(3)
            
            ######
            # UI #
            ######
            
            # Display
            pyxel.rectb(
                self.display['x'], self.display['y'], 
                self.display['w'], self.display['h'],
                7
            )
            
            # HUD
            pyxel.rect( x=2, y=2, w=48, h=8, col=3 )
            
            # Hearts sprite
            handlers.handleHearts(self.skeleton['life'])   
            
            # Keys sprites
            handlers.handleKeys(self.skeleton['key1'], (36, 3))
            handlers.handleKeys(self.skeleton['key2'], (42, 3))
            
            ####################
            # Controls sprites #
            ####################
            
            # Up
            pyxel.blt(
                x=self.up['x'], y=self.up['y'],
                img=1, 
                u=self.up['u'], v=self.up['v'],
                w=self.up['w'], h=self.up['h'],
                colkey=0
            )
            
            # Right
            pyxel.blt(
                x=self.right['x'], y=self.right['y'],
                img=1, 
                u=self.right['u'], v=self.right['v'],
                w=self.right['w'], h=self.right['h'],
                colkey=0
            )
            
            # Down
            pyxel.blt(
                x=self.down['x'], y=self.down['y'],
                img=1, 
                u=self.down['u'], v=self.down['v'],
                w=self.down['w'], h=self.down['h'],
                colkey=0
            )
            
            #Left
            pyxel.blt(
                x=self.left['x'], y=self.left['y'],
                img=1, 
                u=self.left['u'], v=self.left['v'],
                w=self.left['w'], h=self.left['h'],
                colkey=0
            )
            
            # Tilemap
            pyxel.bltm(
                x=2, y=10,
                tm=0,
                u=0, v=0,
                w=6, h=7,
                colkey=13
            )
            
            ######################
            # Characters sprites #
            ######################
            
            # Skeleton
            pyxel.blt(
                x=self.skeleton['posx'], y=self.skeleton['posy'],
                img=1, 
                u=46, v=0,
                w=5, h=6,
                colkey=0
            )
            
            # Kids sprite
            pyxel.blt(
                x=30, y=20,
                img=1, 
                u=51, v=0,
                w=6, h=8,
                colkey=0
            )
            
            pyxel.blt(
                x=14, y=50,
                img=1, 
                u=51, v=0,
                w=6, h=8,
                colkey=0
            )
            
            # Shadow sprite
            pyxel.blt(
                x=self.shadow['posx'], y=self.shadow['posy'],
                img=1, 
                u=57, v=0,
                w=5, h=6
            )
        else:
            pyxel.cls(7)
            if self.skeleton['win']:
                pyxel.text(
                    x=10, y=20,
                    s='You Win!',
                    col=11
                )
            
            else:
                pyxel.text(
                    x=8, y=20,
                    s='Game Over',
                    col=11
                )
            
            pyxel.text(
                x=9, y=50,
                s='Q - Quit',
                col=1
            )
            
            pyxel.text(
                x=5, y=60,
                s='R - Restart',
                col=1
            )
App()