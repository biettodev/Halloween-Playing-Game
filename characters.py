import pyxel

def skeleton(f):
    
    f.skeleton = {
        'posx': 0,
        'posy': 0,
        'width': 6, 
        'height': 6,
        'life': 3,
        'speed': 1,
        'key1': False,
        'key2': False,
        'win': False
    }
    
def shadow(f):
    
    f.shadow = {
        'posx': 30,
        'posy': 50,
        'u': 57,
        'v': 0,
        'width': 5, 
        'height': 6,
    }

def kids(f):
    
    f.kids = {
        'kid1':{
            'posx': 20,
            'posy': 20,
            'width': 6, 
            'height': 8,
            'speed': 1
        },
        
        'kid2': {
            'posx': 40,
            'posy': 50,
            'width': 6, 
            'height': 8,
            'speed': 1
        }
        
    }