import random
import card_setting
from my_moduler import get_module_logger
mylogger = get_module_logger(__name__)
from util_ability import *
import util_ability
from my_enum import *
"""
class trigger_ability_001:
    def __call__(self,field,player,opponent,virtual,target,itself,state_log=None):
        if itself.is_in_field==False:return
        if state_log!=None and state_log[0]==State_Code.SET.value and state_log[1][0]==opponent.player_num:
            get_damage_to_player(opponent,virtual,num=1)
"""
def trigger_ability_001(field,player,opponent,virtual,target,itself,state_log=None):
    #mylogger.info("Ability:1")
    if itself.is_in_field == False: return
    if state_log is not None and state_log[0] == State_Code.SET.value and state_log[1][0] == opponent.player_num:
        get_damage_to_player(opponent, virtual, num=1)
"""
class trigger_ability_002:
    def __init__(self):
        mylogger.info("trigger:2")
    def __call__(self,field,player,opponent,virtual,target,itself,state_log=None):
        if not itself.is_in_field:return
        if state_log is not None and state_log[0]==State_Code.RESTORE_PLAYER_LIFE.value and state_log[1]==player.player_num:
            if not virtual:
                mylogger.info("Elana's Prayer's trigger ability is actived")
            for creature_id in field.get_creature_location()[player.player_num]:
                creature=field.card_location[player.player_num][creature_id]
                buff_creature(creature,params=[1,1])
                if not virtual:
                    mylogger.info("player{}'s {:<20} get +1/+1".format(player.player_num+1,creature.name))
"""
def trigger_ability_002(field,player,opponent,virtual,target,itself,state_log=None):
    #mylogger.info("Ability:2")
    if not itself.is_in_field: return
    if state_log is not None and state_log[0] == State_Code.RESTORE_PLAYER_LIFE.value and state_log[
        1] == player.player_num:
        if not virtual:
            mylogger.info("Elana's Prayer's trigger ability is actived")
        for creature_id in field.get_creature_location()[player.player_num]:
            creature = field.card_location[player.player_num][creature_id]
            buff_creature(creature, params=[1, 1])
            if not virtual:
                mylogger.info("player{}'s {:<20} get +1/+1".format(player.player_num + 1, creature.name))
"""
class trigger_ability_003:
    def __init__(self):
        mylogger.info("trigger:3")
    def __call__(self,field,player,opponent,virtual,target,itself,state_log=None):
        if not itself.is_in_field:return
        if state_log is not None and state_log[0]==State_Code.RESTORE_PLAYER_LIFE.value and state_log[1]==player.player_num:
            if not virtual:
                mylogger.info("Whitefang Temple's trigger ability is actived")
            itself.down_count(num=1,virtual=virtual)
"""

def trigger_ability_003(field,player,opponent,virtual,target,itself,state_log=None):
    #mylogger.info("Ability:3")
    if not itself.is_in_field: return
    if state_log is not None and state_log[0] == State_Code.RESTORE_PLAYER_LIFE.value and state_log[
        1] == player.player_num:
        if not virtual:
            mylogger.info("Whitefang Temple's trigger ability is actived")
        itself.down_count(num=1, virtual=virtual)
"""
class trigger_ability_004:
    def __init__(self):
        mylogger.info("trigger:4")
    def __call__(self,field,player,opponent,virtual,target,itself,state_log=None):
        if not itself.is_in_field:return
        if state_log is not None and state_log[0]==State_Code.RESTORE_PLAYER_LIFE.value and state_log[1]==player.player_num:
            if not virtual:
                mylogger.info("Holy Bowman Kel's trigger ability is actived")
            get_damage_to_player(opponent,virtual,num=2)
"""

def trigger_ability_004(field,player,opponent,virtual,target,itself,state_log=None):
    #mylogger.info("Ability:4")
    if not itself.is_in_field: return
    if state_log is not None and state_log[0] == State_Code.RESTORE_PLAYER_LIFE.value and state_log[
        1] == player.player_num:
        if not virtual:
            mylogger.info("Holy Bowman Kel's trigger ability is actived")
        get_damage_to_player(opponent, virtual, num=2)
"""     
class trigger_ability_005:
    def __call__(self,field,player,opponent,virtual,target,itself,state_log=None):
        if not itself.is_in_field:return
        if state_log is not None and state_log[0]==State_Code.RESTORE_PLAYER_LIFE.value and state_log[1]==player.player_num:
            damage=1+int(itself.evolved)
            if not virtual:
                mylogger.info("Kel, Holy Marksman's trigger ability is actived")
            get_damage_to_all_enemy_follower(field, opponent, virtual, num=damage)
            #for creature_id in field.get_creature_location()[opponent.player_num]:
            #    get_damage_to_creature(field,opponent,virtual,creature_id,num=damage)
"""

def trigger_ability_005(field,player,opponent,virtual,target,itself,state_log=None):
    #mylogger.info("Ability:5")
    if not itself.is_in_field: return
    if state_log is not None and state_log[0] == State_Code.RESTORE_PLAYER_LIFE.value and state_log[
        1] == player.player_num:
        damage = 1 + int(itself.evolved)
        if not virtual:
            mylogger.info("Kel, Holy Marksman's trigger ability is actived")
        get_damage_to_all_enemy_follower(field, opponent, virtual, num=damage)
        # for creature_id in field.get_creature_location()[opponent.player_num]:
        #    get_damage_to_creature(field,opponent,virtual,creature_id,num=damage)
"""
class trigger_ability_006:
    def __call__(self,field,player,opponent,virtual,target,itself,state_log=None):
        if not itself.is_in_field:return
        if state_log is not None and state_log[0]==State_Code.SET.value and state_log[1][0]==player.player_num:

            if state_log[1][1]=="Creature":
                if card_setting.creature_list[state_log[1][2]][4][-1]==1:
                    buff_creature_until_end_of_turn(itself,params=[1,0])
            elif state_log[1][1]=="Amulet":
                if card_setting.amulet_list[state_log[1][2]][2][-1]==1:
                    buff_creature_until_end_of_turn(itself,params=[1,0])
"""

def trigger_ability_006(field,player,opponent,virtual,target,itself,state_log=None):
    if not itself.is_in_field: return
    if state_log is not None and state_log[0] == State_Code.SET.value and state_log[1][0] == player.player_num:

        if state_log[1][1] == "Creature":
            if card_setting.creature_list[state_log[1][2]][4][-1] == 1:
                buff_creature_until_end_of_turn(itself, params=[1, 0])
        elif state_log[1][1] == "Amulet":
            if card_setting.amulet_list[state_log[1][2]][2][-1] == 1:
                buff_creature_until_end_of_turn(itself, params=[1, 0])

"""          
class trigger_ability_007:
    def __call__(self,field,player,opponent,virtual,target,itself,state_log=None):
        
        #Whenever an enemy follower is destroyed, gain +1/+0.
        
        if not itself.is_in_field:return
        if state_log is None: return
        if state_log[0]==State_Code.DESTROYED.value and state_log[1][0]==opponent.player_num:
            if not virtual:
                mylogger.info("{} get +1/0({})".format(itself.name,State_Code(state_log[0]).name))
            buff_creature(itself,params=[1,0])
        #if not virtual:
        #    mylogger.info("state_log:{}".format(state_log))

"""
def trigger_ability_007(field,player,opponent,virtual,target,itself,state_log=None):
    if not itself.is_in_field: return
    if state_log is None: return
    if state_log[0] == State_Code.DESTROYED.value and state_log[1][0] == opponent.player_num:
        if not virtual:
            mylogger.info("{} get +1/0({})".format(itself.name, State_Code(state_log[0]).name))
        buff_creature(itself, params=[1, 0])
    # if not virtual:
    #    mylogger.info("state_log:{}".format(state_log))
"""
class trigger_ability_008:
    def __call__(self,field,player,opponent,virtual,target,itself,state_log=None):
        
        #Whenever another allied follower attacks, give that follower +1/+0 until the end of the turn.
        
        if not itself.is_in_field:return
        if state_log is not None and (state_log[0]==State_Code.ATTACK_TO_FOLLOWER.value or state_log[0]==State_Code.ATTACK_TO_PLAYER.value):
            if state_log[1]==player.player_num and state_log[2]!=itself:
                attacking_creature=state_log[2]
                util_ability.buff_creature_until_end_of_turn(attacking_creature,params=[1,0])
                #buff_creature_until_end_of_turn(attacking_creature,params=[1,0])
                if not virtual:
                    mylogger.info("{} get +1/0 until end of turn".format(attacking_creature.name))
"""

def trigger_ability_008(field,player,opponent,virtual,target,itself,state_log=None):
    if not itself.is_in_field: return
    if state_log is not None and (
            state_log[0] == State_Code.ATTACK_TO_FOLLOWER.value or state_log[0] == State_Code.ATTACK_TO_PLAYER.value):
        if state_log[1] == player.player_num and state_log[2] != itself:
            attacking_creature = state_log[2]
            util_ability.buff_creature_until_end_of_turn(attacking_creature, params=[1, 0])
            # buff_creature_until_end_of_turn(attacking_creature,params=[1,0])
            if not virtual:
                mylogger.info("{} get +1/0 until end of turn".format(attacking_creature.name))
"""
class trigger_ability_009:
    def __call__(self,field,player,opponent,virtual,target,itself,state_log=None):
        
        #Whenever an allied follower is destroyed, subtract 1 from this amulet's Countdown.

        #self.state_log.append([State_Code.DESTROYED.value,(location[0],tmp.card_category,tmp.card_id)])#3は破壊されたとき
        
        if itself.is_in_field==False:return
        if state_log!=None and state_log[0]==State_Code.DESTROYED.value and state_log[1][0]==player.player_num and state_log[1][1]=="Creature":
            itself.down_count(num=1,virtual=virtual)
"""
def trigger_ability_009(field,player,opponent,virtual,target,itself,state_log=None):
    # Whenever an allied follower is destroyed, subtract 1 from this amulet's Countdown.

    # self.state_log.append([State_Code.DESTROYED.value,(location[0],tmp.card_category,tmp.card_id)])#3は破壊されたとき

    if itself.is_in_field == False: return
    if state_log != None and state_log[0] == State_Code.DESTROYED.value and state_log[1][0] == player.player_num and \
            state_log[1][1] == "Creature":
        itself.down_count(num=1, virtual=virtual)
"""
class trigger_ability_010:
    def __call__(self,field,player,opponent,virtual,target,itself,state_log=None):
        
        #Whenever an allied Dragoncraft follower that originally costs 3 play points or less comes into play,
        #deal 2 damage to a random enemy follower and 1 damage to the enemy leader if Overflow is active for you.

        #self.state_log.append([State_Code.SET.value,(player_num,card.card_category,card.card_id)])
        
        if player.check_overflow()==False or itself.is_in_field==False:return
        if state_log!=None and state_log[0]==State_Code.SET.value and state_log[1][0]==player.player_num:
            if not virtual:
                mylogger.info("state_log:{} time_stamp:{}".format(state_log,itself.time_stamp))
            if state_log[1][1]=="Creature":
                if card_setting.creature_list[state_log[1][2]][-2][0]==LeaderClass.DRAGON.value and card_setting.creature_list[state_log[1][2]][0]<=3:
                    get_damage_to_random_creature(field,opponent,virtual,num=2)
                    get_damage_to_player(player,virtual,num=1)
                elif not virtual:
                     mylogger.info("Class:{} Cost:{}".format(LeaderClass(card_setting.creature_list[state_log[1][2]][-2][0]),\
                         card_setting.creature_list[state_log[1][2]][0]))
"""

def trigger_ability_010(field,player,opponent,virtual,target,itself,state_log=None):
    # Whenever an allied Dragoncraft follower that originally costs 3 play points or less comes into play,
    # deal 2 damage to a random enemy follower and 1 damage to the enemy leader if Overflow is active for you.

    # self.state_log.append([State_Code.SET.value,(player_num,card.card_category,card.card_id)])

    if player.check_overflow() == False or itself.is_in_field == False: return
    if state_log != None and state_log[0] == State_Code.SET.value and state_log[1][0] == player.player_num:
        if not virtual:
            mylogger.info("state_log:{} time_stamp:{}".format(state_log, itself.time_stamp))
        if state_log[1][1] == "Creature":
            if card_setting.creature_list[state_log[1][2]][-2][0] == LeaderClass.DRAGON.value and \
                    card_setting.creature_list[state_log[1][2]][0] <= 3:
                get_damage_to_random_creature(field, opponent, virtual, num=2)
                get_damage_to_player(opponent, virtual, num=1)
            elif not virtual:
                mylogger.info("Class:{} Cost:{}".format(LeaderClass(card_setting.creature_list[state_log[1][2]][-2][0]),
                                                        card_setting.creature_list[state_log[1][2]][0]))
"""
class trigger_ability_011:
    def __call__(self,field,player,opponent,virtual,target,itself,state_log=None):
        #
        #Whenever another allied follower is destroyed, gain +1/+1.
        #
        if not itself.is_in_field:return
        if state_log is not None and state_log[0]==State_Code.DESTROYED.value and state_log[1][0]==player.player_num:
            if not virtual:
                mylogger.info("{} get +1/+1".format(itself.name))
            buff_creature(itself,params=[1,1])
"""
def trigger_ability_011(field,player,opponent,virtual,target,itself,state_log=None):
    # Whenever an allied follower is destroyed, subtract 1 from this amulet's Countdown.
    if not itself.is_in_field: return
    if state_log is not None and state_log[0] == State_Code.DESTROYED.value and state_log[1][0] == player.player_num:
        if not virtual:
            mylogger.info("{} get +1/+1".format(itself.name))
        buff_creature(itself, params=[1, 1])

"""     
class trigger_ability_012:
    def __call__(self,field,player,opponent,virtual,target,itself,state_log=None):
        
        Whenever another allied follower comes into play, gain +1/+0.
        
        if not itself.is_in_field:return
        if state_log is None:
            return
        if state_log[0] != State_Code.SET.value:
            return
        if state_log[1][0] != player.player_num:
            return
        if state_log[1][1] != "Creature":
            return

        if not virtual:
            mylogger.info("{} get +1/0".format(itself.name))
        buff_creature(itself,params=[1,0])
"""

def trigger_ability_012(field,player,opponent,virtual,target,itself,state_log=None):
    if not itself.is_in_field: return
    if state_log is None:
        return
    if state_log[0] != State_Code.SET.value:
        return
    if state_log[1][0] != player.player_num:
        return
    if state_log[1][1] != "Creature":
        return

    if not virtual:
        mylogger.info("{} get +1/0".format(itself.name))
    buff_creature(itself, params=[1, 0])
"""
class trigger_ability_013:
    def __call__(self,field,player,opponent,virtual,target,itself,state_log=None):

        #Evolved:
        #Whenever an allied Puppet comes into play, give it +1/+0.
        
        if not itself.evolved:
            return
        if state_log is not None and state_log[0]==State_Code.SET.value and state_log[1][0] == player.player_num:
            for card in field.card_location[player.player_num]:
                if id(card) == state_log[1][3] and card.name == "Puppet":
                    buff_creature(card,params=[1,0])
                    if not virtual:
                        mylogger.info("Puppet get +1/0")
                    break
"""
def trigger_ability_013(field,player,opponent,virtual,target,itself,state_log=None):
    if not itself.evolved:
        return
    if state_log is not None and state_log[0] == State_Code.SET.value and state_log[1][0] == player.player_num:
        for card in field.card_location[player.player_num]:
            if id(card) == state_log[1][3] and card.name == "Puppet":
                buff_creature(card, params=[1, 0])
                if not virtual:
                    mylogger.info("Puppet get +1/0")
                break

class trigger_ability_014:
    def __call__(self,field,player,opponent,virtual,target,itself,state_log=None):

        #When another allied Neutral follower comes into play, this follower loses Can't_Attack and gains Rush.

        if self not in itself.trigger_ability :
            return
        if state_log is not None and state_log[0]==State_Code.SET.value and state_log[1][0] == player.player_num:
            if state_log[1][1] == "Creature" and \
                card_setting.creature_list[state_log[1][2]][-2][0] == LeaderClass.NEUTRAL.value:
                assert KeywordAbility.CANT_ATTACK.value in itself.ability, "{} don't have {},{}"\
                    .format(itself.ability,KeywordAbility.CANT_ATTACK.value,itself.trigger_ability)
                itself.ability.remove(KeywordAbility.CANT_ATTACK.value)
                add_ability_to_creature(field,player,itself,virtual,add_ability=[KeywordAbility.RUSH.value])
                assert self in itself.trigger_ability,"{}".format(itself.trigger_ability)
                itself.trigger_ability.remove(self)
                if not virtual:
                    mylogger.info("{} loses {} and gains {}".format(itself.name,KeywordAbility.CANT_ATTACK.name,
                                                                    KeywordAbility.RUSH.name))

def trigger_ability_014(field,player,opponent,virtual,target,itself,state_log=None):
    if state_log is not None and state_log[0] == State_Code.SET.value and state_log[1][0] == player.player_num:
        if state_log[1][1] == "Creature" and \
                card_setting.creature_list[state_log[1][2]][-2][0] == LeaderClass.NEUTRAL.value:
            if KeywordAbility.CANT_ATTACK.value in itself.ability:
                itself.ability.remove(KeywordAbility.CANT_ATTACK.value)
                add_ability_to_creature(field, player, itself, virtual, add_ability=[KeywordAbility.RUSH.value])
                if not virtual:
                    mylogger.info("{} loses {} and gains {}".format(itself.name, KeywordAbility.CANT_ATTACK.name,
                                                                    KeywordAbility.RUSH.name))
"""
class special_trigger_ability_001:
    def __init__(self):
        self.done_flg = False

    def __call__(self,field,player,opponent,virtual,target,itself,state_log=None):
        
        #Gain +2/+0 if Overflow is active for you.
        
        if not self.done_flg and player.check_overflow():
            buff_creature(itself,params=[2,0])
            self.done_flg = True
        elif self.done_flg and not player.check_overflow():
            buff_creature(itself,params=[-2,0])
            self.done_flg = False

"""
def special_trigger_ability_001(field,player,opponent,virtual,target,itself,state_log=None):
    if player.check_overflow():
        if itself.buff != [2,0]:
            buff_creature(itself, params=[2, 0])
    elif itself.buff == [2,0]:
        buff_creature(itself, params=[-2, 0])

            



        

trigger_ability_dict={
    1:trigger_ability_001,2:trigger_ability_002,3:trigger_ability_003,4:trigger_ability_004,5:trigger_ability_005,
    6:trigger_ability_006,7:trigger_ability_007,8:trigger_ability_008,9:trigger_ability_009,10:trigger_ability_010,
    11:trigger_ability_011,12:trigger_ability_012,13:trigger_ability_013,14:trigger_ability_014,



                    -1:special_trigger_ability_001}


