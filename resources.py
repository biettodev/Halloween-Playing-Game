import pyxel

def images():
    
    return pyxel.image(0).load(0, 0, 'assets/hpg-tileset.png'), pyxel.image(1).load(0, 0, 'assets/sprites_bank.png')

def tilemap():
    """
        000: Ground
        001: Grass
        002: Tomb
        003: Candles
    """
    
    return pyxel.tilemap(0).set(
                0, 
                0, 
                [
                    '000002000001002000',
                    '001000001000000001',
                    '000000000000000002',
                    '000000001000000000',
                    '001003000000001002',
                    '002000000000000001',
                    '000001000001000000',
                ]
            )
            
def music():  
    
    return pyxel.sound(0).set(
            "c1 f1 a1 e1" 
            "f1 c1 e1"
            "c1 g1 e1 f1 c1 g1 c1 e1", 
            "s", 
            "4", 
            "n", 
            36
        )

def ui(f):
    
    f.display = {
            'x': 2,
            'y': 2, 
            'w': 48, 
            'h': 60
        }
        
    f.hud = {
        'heart': [0, 0],
        'key': [0, 0]
    }
    
    f.up = {
        'x': 24,
        'y': 66,
        'u': 31,
        'v': 2,
        'w': 5,
        'h': 4
    }
    
    f.right = {
        'x': 32,
        'y': 70,
        'u': 36,
        'v': 1,
        'w': 3,
        'h': 5
    }
    
    f.down = {
        'x': 24,
        'y': 74,
        'u': 38,
        'v': 2,
        'w': 5,
        'h': 4
    }
    
    f.left = {
        'x': 18,
        'y': 70,
        'u': 43,
        'v': 1,
        'w': 3,
        'h': 5
    }
    
def texts():
    pass