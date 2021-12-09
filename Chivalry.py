# Go to Spirituality and put at least 1000 tithing points
# Wear a 100 LRC suit
# Run without a loop


while True:
    if Player.Mana < 30: # meditation removing armor and putting it back
        calca = Player.GetItemOnLayer('Pants')
        peitoral = Player.GetItemOnLayer('InnerTorso')
        Player.UnEquipItemByLayer('Pants')
        Misc.Pause(1000)
        Player.UnEquipItemByLayer('InnerTorso')
        Misc.Pause(1000)
        Player.UseSkill("Meditation")
        Misc.Pause(20000)
        Player.EquipItem(calca)
        Misc.Pause(1000)
        Player.EquipItem(peitoral)
        Misc.Pause(1000)
        
    else: # Spells raising
        Chivalry = Player.GetSkillValue('Chivalry')
        if Chivalry < 45 :
            Spells.CastChivalry('Consecrate Weapon')
            Misc.Pause(4500)
        
        elif Chivalry < 60:
            Spells.CastChivalry('Divine Fury')
            Misc.Pause(2000)   
   
        elif Chivalry < 70 :
            Spells.CastChivalry('Enemy Of One')
            Misc.Pause(3000)  

        elif Chivalry < 90 :
            Spells.CastChivalry('Holy Light')
            Misc.Pause(3000) 
        
        elif Chivalry != Player.GetSkillCap('Chivalry'):
            Spells.CastChivalry('Noble Sacrifice')
            Misc.Pause(6000)         
   
        elif Chivalry == Player.GetSkillCap('Chivalry'): #you got it!
            Misc.ScriptStop('Chivalry Trainer.py')