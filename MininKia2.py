#initial definitions
backpack = 0x4046ACAB
bagofholding = 0x4046ACB1
dirtbook = [0x408117DE] #Lista de Livros (teste com apenas 1)

#location = (7, 13, 19, 25, 31, 37, 43, 49, 55, 61, 67, 73, 79, 85, 91, 97) #PosicaoDoRunebook??
location = (7, 13, 19, 25, 31, 37) #PosicaoDoRunebook??
a = len(dirtbook)
#b = len(location)
b=5 #if you want to start from a specific rune marker
maxtry = 8
diggingtime=3000

def gumpcheck():
    if Gumps.HasGump( ):
        Misc.Beep( )


def pack():
    if Items.FindByID(0x19B9,-1,backpack,False,False):
        #Misc.SendMessage("found some ORE", 21)
        soil = Items.FindByID(0x19B9,-1,backpack,False,False)
        Items.Move(soil, bagofholding, -1)
        Misc.Pause(500)
    if Items.FindByID(0x19B8,-1,backpack,False,False):
        #Misc.SendMessage("Found some coal",21)
        coal = Items.FindByID(0x19B8,-1,backpack,False,False)
        Items.Move(coal, bagofholding, -1)
        Misc.Pause(500)
    Misc.Pause(500)   
    
    
def move():
    global a
    global b
    if b == len(location):
        b = 1
        if a == len(dirtbook):
            a = 1
        else:
            a = a + 1
    else:
        b = b + 1
    Gumps.CloseGump(1431013363)
    Items.UseItem(dirtbook[a-1])
    Gumps.WaitForGump(1431013363, 10000)
    Gumps.SendAction(1431013363, location[b-1])
    Misc.Pause(4000)
    target = Player.Position
    if Target.HasTarget( ):
        Target.Cancel( )
    Misc.ClearIgnore( ) 
    
    
    
def dig1():
    Misc.ClearIgnore( )
    Target.Cancel( ) 
    i=0
    while i<maxtry:
        gumpcheck()
        shovel = Items.FindByID(0x0F39, 0x0000, -1)
        Items.UseItem(shovel);
        Target.WaitForTarget(1000, False)
        target = Player.Position
        tiles = Statics.GetStaticsTileInfo(target.X, target.Y, Player.Map) #read map files to find target as static
        if len(tiles) != 0 and tiles[0].StaticID != 0: #if tile is not id 0
            Target.TargetExecute(target.X, target.Y, tiles[0].StaticZ, tiles[0].StaticID) #target tile
        else:
            Misc.SendMessage("TILES PROBLEM", 21)
        Misc.IgnoreObject(shovel)
        Misc.Pause(150)
        Target.Cancel( )
        i=i+1

        
def dig2():
    Misc.ClearIgnore( )
    Target.Cancel( )
    i=0
    while i<maxtry:
        gumpcheck()
        shovel = Items.FindByID(0x0F39, 0x0000, -1)
        Items.UseItem(shovel);
        Target.WaitForTarget(1000, False)
        target = Player.Position
        tiles = Statics.GetStaticsTileInfo(target.X+1, target.Y, Player.Map) #read map files to find target as static
        if len(tiles) != 0 and tiles[0].StaticID != 0: #if tile is not id 0
            Target.TargetExecute(target.X + 1, target.Y, tiles[0].StaticZ, tiles[0].StaticID) #target tile
        else:
            Misc.SendMessage("TILES PROBLEM", 21)
        Misc.Pause(150)
        Target.Cancel( )
        i=i+1
        

def dig3():
    Misc.ClearIgnore( )
    Target.Cancel( )
    i=0
    while i<maxtry:
        gumpcheck()
        shovel = Items.FindByID(0x0F39, 0x0000, -1)
        Items.UseItem(shovel);
        Target.WaitForTarget(1000, False)
        target = Player.Position
        tiles = Statics.GetStaticsTileInfo(target.X, target.Y+1, Player.Map) #read map files to find target as static
        if len(tiles) != 0 and tiles[0].StaticID != 0: #if tile is not id 0
            Target.TargetExecute(target.X, target.Y + 1, tiles[0].StaticZ, tiles[0].StaticID) #target tile
        else:
            Misc.SendMessage("TILES PROBLEM", 21)
        Misc.IgnoreObject(shovel)
        Misc.Pause(150)
        Target.Cancel( )
        i=i+1        
        

def dig4():
    Misc.ClearIgnore( )
    Target.Cancel( )  
    i=0
    while i<maxtry:
        gumpcheck()
        shovel = Items.FindByID(0x0F39, 0x0000, -1)
        Items.UseItem(shovel);
        Target.WaitForTarget(1000, False)
        target = Player.Position
        tiles = Statics.GetStaticsTileInfo(target.X+1, target.Y+1, Player.Map) #read map files to find target as static
        if len(tiles) != 0 and tiles[0].StaticID != 0: #if tile is not id 0
            Target.TargetExecute(target.X + 1, target.Y+1, tiles[0].StaticZ, tiles[0].StaticID) #target tile
        else:
            Misc.SendMessage("TILES PROBLEM", 21)
        Misc.IgnoreObject(shovel)
        Misc.Pause(150)
        Target.Cancel( )
        i=i+1  
  
        
   
    
while True:
    Misc.ClearIgnore( )  
    pack()
    move()
    Journal.Clear() #Make sure journal is not reading ahead of when this started.
    while Journal.Search("There is no metal here to mine.") == False: #do under until this message happens.
            Journal.Clear() #clear message as to not get confused.
            dig1()
            Misc.Pause(100)
            pack()
            Misc.Pause(diggingtime)
    Misc.SendMessage("Finished Q1", 21)
    Misc.Pause(500)
    Misc.ClearIgnore( ) 
    Journal.Clear() #Make sure journal is not reading ahead of when this started.
    while Journal.Search("There is no metal here to mine.") == False: #do under until this message happens.
            Journal.Clear() #clear message as to not get confused.
            dig2()
            Misc.Pause(100)
            pack()
            Misc.Pause(diggingtime)
    Misc.SendMessage("Finished Q2", 21)
    Misc.Pause(500)
    Misc.ClearIgnore( ) 
    Journal.Clear() #Make sure journal is not reading ahead of when this started.
    while Journal.Search("There is no metal here to mine.") == False: #do under until this message happens.
            Journal.Clear() #clear message as to not get confused.
            dig3()
            Misc.Pause(100)
            pack()
            Misc.Pause(diggingtime)
    Misc.SendMessage("Finished Q3", 21)
    Misc.Pause(500)
    Misc.ClearIgnore( ) 
    Journal.Clear() #Make sure journal is not reading ahead of when this started.
    while Journal.Search("There is no metal here to mine.") == False: #do under until this message happens.
            Journal.Clear() #clear message as to not get confused.
            dig4()
            Misc.Pause(100)
            pack()
            Misc.Pause(diggingtime)
    Misc.SendMessage("Finished Q4", 21)
    Misc.Pause(500)
    Misc.ClearIgnore( ) 
    #Misc.SendMessage("Pausing 2 seconds.", 21)
   
    Misc.Pause(2000)
   
      
    
    
    