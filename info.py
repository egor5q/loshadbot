class Lobby(object):
    def __init__(self):
        self.game={}
        
     
class S_me4nik(object):
    def __init__(self):
        self.name='Скелет-мечник'
        self.hp=65
        self.mana=30
        self.damage=55
        self.cost=30
        self.type='dead'
        self.fromelectrodmg=0.7
        self.frombiodmg=1.5
        self.fromghostdmg=0.9
        self.fromdeaddmg=1.0
        self.fromfiredmg=1.0
        self.skill=None
        
        
class Pyos(object):
    def __init__(self):
        self.name='Pyos'
        self.hp=300
        self.mana=30
        self.damage=50
        self.cost=75
        self.type='bio'
        self.fromelectrodmg=1.3
        self.frombiodmg=1.0
        self.fromghostdmg=0.8
        self.fromdeaddmg=1.1
        self.fromfiredmg=1.5
        self.skill=None
        
class Phoenix(object):
    def __init__(self):
        self.name='Феникадзе'
        self.hp=25
        self.mana=30
        self.damage=200
        self.cost=60
        self.type='fire'
        self.fromelectrodmg=0.5
        self.frombiodmg=0.7
        self.fromghostdmg=1.5
        self.fromdeaddmg=1.2
        self.fromfiredmg=1.0
        self.skill=None
        
        
class Electromagnit(object):
    def __init__(self):
        self.name='Электромагнитень'
        self.hp=180
        self.mana=80
        self.damage=60
        self.cost=65
        self.type='electro'
        self.fromelectrodmg=1.0
        self.frombiodmg=1.1
        self.fromghostdmg=0.8
        self.fromdeaddmg=1.5
        self.fromfiredmg=0.5
        self.skill=None
        
        
class Manoed(object):
    def __init__(self):
        self.name='Маноед'
        self.hp=135
        self.mana=30
        self.damage=45
        self.cost=45
        self.type='ghost'
        self.fromelectrodmg=1.5
        self.frombiodmg=0.75
        self.fromghostdmg=1.0
        self.fromdeaddmg=0.75
        self.fromfiredmg=0.9
        self.skill=None
        
        
class Tiranozavr(object):  
    def __init__(self):
        self.name='Тиранозавр'
        self.hp=260
        self.mana=30
        self.damage=120
        self.cost=100
        self.type='bio'
        self.fromelectrodmg=1.3
        self.frombiodmg=1.0
        self.fromghostdmg=0.8
        self.fromdeaddmg=1.1
        self.fromfiredmg=1.5
        self.skill=None
        

class S4upakabra(object):
    def __init__(self):
        self.name='Чупакабра'
        self.hp=75
        self.mana=55
        self.damage=90
        self.cost=50
        self.type='dead'
        self.fromelectrodmg=0.7
        self.frombiodmg=1.5
        self.fromghostdmg=0.9
        self.fromdeaddmg=1.0
        self.fromfiredmg=1.0
        self.skill=None
        
        
class Golem(object):
    def __init__(self):
        self.name='Пылающий голем'
        self.hp=600
        self.mana=100
        self.damage=100
        self.cost=165
        self.type='fire'
        self.fromelectrodmg=0.5
        self.frombiodmg=0.7
        self.fromghostdmg=1.5
        self.fromdeaddmg=1.2
        self.fromfiredmg=1.0
        self.skill=None



        
        
class Vsadnik(object):
    def __init__(self):
        self.name='Всадник без коня'
        self.hp=200
        self.mana=50
        self.damage=70
        self.cost=70
        self.type='ghost'
        self.fromelectrodmg=1.5
        self.frombiodmg=0.75
        self.fromghostdmg=1.0
        self.fromdeaddmg=0.75
        self.fromfiredmg=0.9
        self.skill=None
        
        
       
class Soulcatcher(object):
    def __init__(self):
        self.name='Пожиратель душ'
        self.hp=110
        self.mana=50
        self.damage=75
        self.cost=70
        self.type='dead'
        self.fromelectrodmg=0.7
        self.frombiodmg=1.5
        self.fromghostdmg=0.9
        self.fromdeaddmg=1.0
        self.fromfiredmg=1.0
        self.skill=None
        
        
        
class Zombie(object):
    def __init__(self):
        self.name='Зомби'
        self.hp=230
        self.mana=50
        self.damage=25
        self.cost=65
        self.type='dead'
        self.fromelectrodmg=0.7
        self.frombiodmg=1.5
        self.fromghostdmg=0.9
        self.fromdeaddmg=1.0
        self.fromfiredmg=1.0
        self.skill=None
    
    
    
    
    

        
        
        



zombie=Zombie()
soulcatcher=Soulcatcher()
vsadnik=Vsadnik()
golem=Golem()
s4upakabra=S4upakabra()        
tiranozavr=Tiranozavr()        
manoed=Manoed()        
electromagnit=Electromagnit()
phoenix=Phoenix()        
pyos=Pyos()       
s_me4nik=S_me4nik()        
lobby = Lobby()
