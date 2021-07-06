import random
from my_moduler import get_module_logger
import card_setting
import Player_Ability_setting
import card_setting
mylogger = get_module_logger(__name__)
from util_ability import *
from my_enum import *
import util_ability

def creature_ability_001(field, player, opponent, virtual, target, itself):
    field.restore_player_life(player=player, num=2, virtual=virtual)


def creature_ability_002(field, player, opponent, virtual, target, itself):
    if itself.active_enhance_code[0]:
        get_damage_to_player(opponent, virtual, num=3)


def creature_ability_003(field, player, opponent, virtual, target, itself):
    draw_cards(player, virtual, num=1)


def creature_ability_004(field, player, opponent, virtual, target, itself):
    if target is not None and field.get_can_be_targeted(player_num=player.player_num) != []:
        get_damage_to_creature(field, opponent, virtual, target, num=1)


def creature_ability_005(field, player, opponent, virtual, target, itself):
    if field.get_can_be_targeted(player_num=player.player_num) != []:
        if target is None:
            raise Exception()
        get_damage_to_creature(field, opponent, virtual, target, num=4)


def creature_ability_006(field, player, opponent, virtual, target, itself):
    if not virtual:
        mylogger.info("All other creatures  are destroyed")

    for j in range(2):
        side_num = (player.player_num + j) % 2
        # side=field.get_creature_location()[side_num]
        side = field.card_location[side_num]
        for thing in side:
            # thing=field.card_location[side_num][i]
            if thing != itself and KeywordAbility.CANT_BE_DESTROYED_BY_EFFECTS.value not in thing.ability:
                thing.is_in_field = False
                thing.is_in_graveyard = True
    field.check_death(player_num=player.player_num, virtual=virtual)


def creature_ability_007(field, player, opponent, virtual, target, itself):
    if not virtual:
        mylogger.info("Give +1/+1 to all other allied creatures")

    for creature in field.card_location[player.player_num]:
        if itself != creature and creature.card_category == "Creature":
            buff_creature(creature, params=[1, 1])


def creature_ability_008(field, player, opponent, virtual, target, itself):
    """
    Summon Otohime's Bodyguards until your area is full
    """
    summon_creature(field, player, virtual, name="Otohime's Bodyguard", num=4)


def creature_ability_009(field, player, opponent, virtual, target, itself):
    """
    Gain +1/+0 for each enemy follower in play. If there are at least 3,
    gain resistance to targeted enemy spells and effects.
    """

    num = len(field.card_location[opponent.player_num])
    # itself.power+=num
    # itself.buff[0]+=num
    buff_creature(itself, params=[num, 0])
    if virtual == False:
        mylogger.info("{} get +{}/0".format(itself.name, num))
    if num >= 3:
        # itself.ability.append(KeywordAbility.CANT_BE_TARGETED.value)
        add_ability_to_creature(field, player, itself, virtual, add_ability=[KeywordAbility.CANT_BE_TARGETED.value])


def creature_ability_010(field, player, opponent, virtual, target, itself):
    summon_creature(field, player, virtual, name="Steelclad Knight")


def creature_ability_011(field, player, opponent, virtual, target, itself):
    """
    Summon Knight
    """
    summon_creature(field, player, virtual, name="Knight")


def creature_ability_012(field, player, opponent, virtual, target, itself):
    summon_creature(field, player, virtual, name="Steelclad Knight")
    summon_creature(field, player, virtual, name="Knight")


def creature_ability_013(field, player, opponent, virtual, target, itself):
    """
    At the end of your turn, restore 4 defense to your leader.
    At the end of your turn, deal 4 damage to the enemy leader.
    """
    if field.turn_player_num == player.player_num:
        if not itself.evolved:
            field.restore_player_life(player=player, num=4, virtual=virtual)

        else:
            get_damage_to_player(opponent, virtual, num=4)


def creature_ability_014(field, player, opponent, virtual, target, itself):
    if field.get_can_be_targeted(player_num=player.player_num) != []:
        get_damage_to_creature(field, opponent, virtual, target, num=3)


def creature_ability_015(field, player, opponent, virtual, target, itself):
    gain_max_pp(field, player, num=1, virtual=virtual)


def creature_ability_016(field, player, opponent, virtual, target, itself):
    buff_creature(itself, params=[itself.spellboost, itself.spellboost])
    if not virtual:
        mylogger.info("{[0]} get +{[1]}/{[1]}".format(itself.name, itself.spellboost))


def creature_ability_017(field, player, opponent, virtual, target, itself):
    get_damage_to_player(player, virtual, num=1)
    get_damage_to_player(opponent, virtual, num=1)


def creature_ability_018(field, player, opponent, virtual, target, itself):
    if player.check_vengeance():
        buff_creature(itself, params=[1, 1])


def creature_ability_019(field, player, opponent, virtual, target, itself):
    get_damage_to_player(player, virtual, num=2)


def creature_ability_020(field, player, opponent, virtual, target, itself):
    if player.check_vengeance():
        add_ability_to_creature(field, player, itself, virtual, add_ability=[KeywordAbility.STORM.value])
        # itself.ability.append(KeywordAbility.STORM.value)


def creature_ability_021(field, player, opponent, virtual, target, itself):
    # Wardrobe Raider's evolve ability
    if target is not None:
        assert target in field.get_regal_targets(itself, target_type=0, player_num=player.player_num), \
            "illigal target error"
        get_damage_to_creature(field, opponent, virtual, target, num=2)
    field.restore_player_life(player=player, num=2, virtual=virtual)


def creature_ability_022(field, player, opponent, virtual, target, itself):
    if not player.check_vengeance():
        get_damage_to_player(player, virtual, num=2)


def creature_ability_023(field, player, opponent, virtual, target, itself):
    get_damage_to_enemy(field, opponent, virtual, target, num=5)
    """
    if target == -1:
        get_damage_to_player(opponent, virtual, num=5)
    elif field.get_can_be_targeted(player_num=player.player_num) != []:
        get_damage_to_creature(field, opponent, virtual, target, num=5)
    """
    field.restore_player_life(player=player, num=5, virtual=virtual)


def creature_ability_024(field, player, opponent, virtual, target, itself):
    if player.check_vengeance():
        add_ability_to_creature(field, player, itself, virtual,
                                add_ability=[KeywordAbility.BANE.value, KeywordAbility.DRAIN.value])

        if not virtual:
            mylogger.info("{} get bane and drain".format(itself.name))


def creature_ability_025(field, player, opponent, virtual, target, itself):
    condition = lambda card: card.trait.name == "COMMANDER"
    search_cards(player, condition, virtual, num=1)


def creature_ability_026(field, player, opponent, virtual, target, itself):
    if target is not None and target < len(field.card_location[opponent.player_num]):
        #if itself.target_regulation(field.card_location[opponent.player_num][target]):
        if card_setting.creature_target_regulation[itself.target_regulation](field.card_location[opponent.player_num][target],itself):
            destroy_opponent_creature(field, opponent, virtual, target)
    elif target is not None:
        able_targets = field.get_regal_targets(itself, target_type=1, player_num=player.player_num)
        mylogger.info("target_id:{} not in {}".format(target, able_targets))
        field.show_field()
        mylogger.info("{} vs {}".format(player.policy.name, opponent.policy.name))
        assert False


def creature_ability_027(field, player, opponent, virtual, target, itself):
    """
    Fanfare: Give +1/+0 to a 1-play point allied follower.
    """
    if target is not None:
        target_creature = field.card_location[player.player_num][target]
        if not card_setting.creature_target_regulation[itself.target_regulation](target_creature,itself):
            #if not itself.target_regulation(target_creature):
            mylogger.info("target_id:{}".format(target))
            field.show_field()
            assert False
        if not virtual:
            mylogger.info("{} get +1/0".format(target_creature.name))
        buff_creature(target_creature, params=[1, 0])


def creature_ability_028(field, player, opponent, virtual, target, itself):
    destroy_random_creature(field, opponent, virtual)


def creature_ability_029(field, player, opponent, virtual, target, itself):
    if target is not None:
        destroy_opponent_creature(field, player, virtual, target)
        draw_cards(player, virtual, num=2)


def creature_ability_030(field, player, opponent, virtual, target, itself):
    if necromancy(field, player, num=1, virtual=virtual):
        if not virtual:
            mylogger.info("{} get +1/+1".format(itself.name))
        buff_creature(itself, params=[1, 1])


def creature_ability_031(field, player, opponent, virtual, target, itself):
    # Ghost's end-of-turn  and removed-from-field-ability
    if field.turn_player_num == player.player_num:
        flg = itself in field.card_location[player.player_num]
        if not flg:
            mylogger.info("Player_num:{}".format(player.player_num))
            field.show_field()
            raise Exception("Error")
        location = [player.player_num, field.card_location[player.player_num].index(itself)]
        field.banish_card(location, virtual=virtual)


def creature_ability_032(field, player, opponent, virtual, target, itself):
    """
    Evolve: Give all of the followers in your hand Last Words: Draw a card.
    Last Words: Draw a card.
    """
    if not virtual:
        mylogger.info("Player{}'s followers in hand get Last Words: Draw a card.".format(player.player_num + 1))
    for card in player.hand:
        if card.card_category == "Creature":
            #card.lastword_ability.append(creature_ability_003)
            card.lastword_ability.append(3)


def creature_ability_033(field, player, opponent, virtual, target, itself):
    get_damage_to_random_creature(field, opponent, virtual, num=1)


def creature_ability_034(field, player, opponent, virtual, target, itself):
    # Lady Grey's evolve ability
    reanimate(field, player, virtual, num=2)


def creature_ability_035(field, player, opponent, virtual, target, itself):
    get_damage_to_player(opponent, virtual, num=2)


def creature_ability_036(field, player, opponent, virtual, target, itself):
    summon_creature(field, player, virtual, name="Mordecai the Duelist")


def creature_ability_037(field, player, opponent, virtual, target, itself):
    power_list = []
    max_power = -1
    for creature_id in field.get_creature_location()[opponent.player_num]:
        if field.card_location[opponent.player_num][creature_id].power > max_power:
            max_power = field.card_location[opponent.player_num][creature_id].power
            power_list = []
        if max_power == field.card_location[opponent.player_num][creature_id].power:
            power_list.append(creature_id)
    if power_list != []:
        target_id = random.choice(power_list)
        destroy_opponent_creature(field, opponent, virtual, target_id)
        field.restore_player_life(player=player, num=max_power, virtual=virtual)


def creature_ability_038(field, player, opponent, virtual, target, itself):
    while len(field.card_location[player.player_num]) < field.max_field_num:
        if necromancy(field, player, num=3, virtual=virtual):
            summon_creature(field, player, virtual, name="Zombie")
        else:
            break
    if not virtual:
        mylogger.info("Give all other allied followers +2/+0 and Rush until the end of the turn")
    count = 0
    for thing in field.card_location[player.player_num]:
        count += 1
        if thing.card_category == "Creature" and thing != itself:
            buff_creature_until_end_of_turn(thing, params=[2, 0])
            if KeywordAbility.RUSH.value not in thing.ability:
                add_ability_until_end_of_player_turn(field, player, thing, virtual,
                                                     add_ability=[KeywordAbility.RUSH.value])

            #    thing.ability.append(4)
            # thing.turn_end_ability.append(ability_until_end_of_turn)


def creature_ability_039(field, player, opponent, virtual, target, itself):
    field.graveyard.shadows[player.player_num] += 1
    if not virtual:
        mylogger.info("Gain 1 shadow")


def creature_ability_040(field, player, opponent, virtual, target, itself):
    field.restore_player_life(player=player, num=3, virtual=virtual)
    draw_cards(player, virtual, num=1)


def creature_ability_041(field, player, opponent, virtual, target, itself):
    field.restore_player_life(player=player, num=2, virtual=virtual)


def creature_ability_042(field, player, opponent, virtual, target, itself):
    set_amulet(field, player, virtual, name="Elana's Prayer")


def creature_ability_043(field, player, opponent, virtual, target, itself):
    put_card_in_hand(field, player, virtual, name="Earth Essence", card_category="Amulet")


def creature_ability_044(field, player, opponent, virtual, target, itself):
    condition = lambda card: card.is_earth_rite is True
    search_cards(player, condition, virtual, num=1)


def creature_ability_045(field, player, opponent, virtual, target, itself):
    if earth_rite(field, player, virtual):
        summon_creature(field, player, virtual, name="Magic Illusionist")


def creature_ability_046(field, player, opponent, virtual, target, itself):
    if earth_rite(field, player, virtual):
        buff_creature(itself, params=[1, 1])
        add_ability_to_creature(field, player, itself, virtual, add_ability=[7])


def creature_ability_047(field, player, opponent, virtual, target, itself):
    if earth_rite(field, player, virtual):
        get_damage_to_enemy(field, opponent, virtual, target, num=3)
        """
        if target == -1:
            get_damage_to_player(opponent, virtual, num=3)
        elif target in field.get_can_be_targeted(player_num=player.player_num):
            get_damage_to_creature(field, opponent, virtual, target, num=3)
        """


def creature_ability_048(field, player, opponent, virtual, target, itself):
    if not earth_rite(field, player, virtual):
        get_damage_to_enemy(field, opponent, virtual, target, num=3)
        """
        if target == -1:
            get_damage_to_player(opponent, virtual, num=3)
        elif field.get_can_be_targeted(player_num=player.player_num) != []:
            get_damage_to_creature(field, opponent, virtual, target, num=3)
        """
    else:
        get_damage_to_player(opponent, virtual, num=3)
        card_id = 0
        while card_id < len(field.card_location[opponent.player_num]):
            if field.card_location[opponent.player_num][card_id].card_category == "Creature":
                before = len(field.card_location[opponent.player_num])
                get_damage_to_creature(field, opponent, virtual, card_id, num=3)
                after = before = len(field.card_location[opponent.player_num])
                card_id += int(before == after)
            else:
                card_id += 1


def creature_ability_049(field, player, opponent, virtual, target, itself):
    count = 0
    while True:
        if earth_rite(field, player, virtual):
            count += 1
        else:
            break
    if count >= 1:
        summon_creature(field, player, virtual, name="Clay Golem")
    if count >= 2:
        get_damage_to_random_creature(field, opponent, virtual, num=3)
    if count >= 3:
        add_ability_to_creature(field, player, itself, virtual, add_ability=[1])
    if count >= 4:
        buff_creature(itself, params=[3, 3])


def creature_ability_050(field, player, opponent, virtual, target, itself):
    put_card_in_hand(field, player, virtual, name="Fairy", card_category="Creature")


def creature_ability_051(field, player, opponent, virtual, target, itself):
    put_card_in_hand(field, player, virtual, name="Fairy", card_category="Creature", num=2)


def creature_ability_052(field, player, opponent, virtual, target, itself):
    buff_creature_until_end_of_turn(itself, params=[field.players_play_num, 0])


def creature_ability_053(field, player, opponent, virtual, target, itself):
    i = 0
    count = 0
    while True:
        target_object = field.card_location[player.player_num][i]
        if i == len(field.card_location[player.player_num]) or target_object == itself:
            break
        if target_object.card_category == "Creature":
            return_card_to_hand(field, [player.player_num, i], virtual)
            count += 1
        else:
            i += 1

    if count > 0:
        if not virtual:
            mylogger.info("{0} get +{1}/+{1}".format(itself.name, count))
        buff_creature(itself, params=[count, count])


def creature_ability_054(field, player, opponent, virtual, target, itself):
    length = len(player.hand)
    faires = put_card_in_hand(field, player, virtual, name="Fairy", card_category="Creature", num=2)
    faires[0].cost = 0
    faires[1].cost = 0


def creature_ability_055(field, player, opponent, virtual, target, itself):
    if field.players_play_num >= 2 and field.get_can_be_targeted(player_num=player.player_num) != []:
        get_damage_to_creature(field, opponent, virtual, target, num=2)


def creature_ability_056(field, player, opponent, virtual, target, itself):
    creature = summon_creature(field, player, virtual, name="Crystalia Eve")
    if field.players_play_num >= 2 and creature is not None:
        field.auto_evolve(creature, virtual=virtual)
        add_ability_to_creature(field, player, creature, virtual, add_ability=[3])


def creature_ability_057(field, player, opponent, virtual, target, itself):
    if player.check_overflow():
        add_ability_to_creature(field, player, itself, virtual, add_ability=[1])


#
def creature_ability_058(field, player, opponent, virtual, target, itself):
    if player.check_overflow() and target is not None:
        if target >= len(field.card_location[player.player_num]):
            regal_targets = field.get_regal_targets(itself, target_type=0, player_num=player.player_num)
            assert False, "out-of-range({} not in regal_targets:{})".format(target, regal_targets)
        target_creature = field.card_location[player.player_num][target]
        add_ability_to_creature(field, player, target_creature, virtual, add_ability=[KeywordAbility.STORM.value])


def creature_ability_059(field, player, opponent, virtual, target, itself):
    if field.current_turn[player.player_num] >= 5:
        gain_max_pp(field, player, num=1, virtual=virtual)


def creature_ability_060(field, player, opponent, virtual, target, itself):
    if field.turn_player_num == player.player_num:
        if player.check_overflow():
            field.restore_player_life(player=player, num=3, virtual=virtual)


def creature_ability_061(field, player, opponent, virtual, target, itself):
    get_damage_to_enemy(field, opponent, virtual, target, num=3)
    """
    if target == -1:
        get_damage_to_player(opponent, virtual, num=3)
    elif field.get_can_be_targeted(player_num=player.player_num != []):
        get_damage_to_creature(field, opponent, virtual, target, num=3)
    """


def creature_ability_062(field, player, opponent, virtual, target, itself):
    field.restore_player_life(player=player, num=3, virtual=virtual)
    put_card_in_hand(field, player, virtual, name="Ouroboros", card_category="Creature", num=1)


def creature_ability_063(field, player, opponent, virtual, target, itself):
    if field.turn_player_num == player.player_num:
        num = field.remain_cost[player.player_num]
        if not virtual:
            mylogger.info("{} get +{}/0".format(itself.name, num))
        buff_creature(itself, params=[num, 0])


def creature_ability_064(field, player, opponent, virtual, target, itself):
    if itself.active_enhance_code[0]:
        count = 0
        while count < 4:
            get_damage_to_player(opponent, virtual, num=1)
            for creature_id in field.get_creature_location()[opponent.player_num]:
                get_damage_to_creature(field, opponent, virtual, creature_id, num=1)
            if field.check_game_end():
                return
            field.check_death(player_num=player.player_num, virtual=virtual)
            count += 1


def creature_ability_065(field, player, opponent, virtual, target, itself):
    if target is not None:
        #creature = player.hand.pop(target)
        creature = player.hand[target]
        if creature.card_category != "Creature":
            mylogger.info("target_id:{} name:{}".format(target, creature.name))
            mylogger.info("type:{}".format(player.policy.type))
            mylogger.info("real")
            mylogger.info("hand_regal_targets:{}".format(field.get_regal_target_dict(player,opponent)))
            player.show_hand()
            field.show_field()
            mylogger.info("last")
            sim_field = player.policy.last_node.field
            sim_player = sim_field.players[player.player_num]
            sim_opponent = sim_field.players[opponent.player_num]
            mylogger.info("hand_regal_targets:{}".format(sim_field.get_regal_target_dict(sim_player, sim_opponent)))
            sim_player = sim_field.players[player.player_num]
            sim_player.show_hand()
            sim_field.show_field()

            assert False,"non-follower-error"
        if not virtual:
            mylogger.info("Player{} put {} to field from hand".format(player.player_num + 1, creature.name))
        creature = player.hand.pop(target)
        field.set_card(creature, player.player_num, virtual=virtual)
        add_ability_to_creature(field, player, creature, virtual, add_ability=[4])
        #creature.turn_end_ability.append(creature_ability_066)
        creature.turn_end_ability.append(66)


def creature_ability_066(field, player, opponent, virtual, target, itself):
    target_location = [player.player_num, field.card_location[player.player_num].index(itself)]
    return_card_to_hand(field, target_location, virtual)


def creature_ability_067(field, player, opponent, virtual, target, itself):
    field.restore_player_life(player=player, num=4, virtual=virtual)


def creature_ability_068(field, player, opponent, virtual, target, itself):
    if itself.active_enhance_code[0]:
        buff_creature(itself, params=[3, 3])


def creature_ability_069(field, player, opponent, virtual, target, itself):
    set_amulet(field, player, virtual, name="Earth Essence", num=2)
    new_cards = put_card_in_hand(field, player, virtual, name="Orichalcum Golem", card_category="Creature", num=1)
    new_cards[0].cost = 7
    if not virtual:
        mylogger.info("{}'s cost is changed to 7".format(itself.name))


def creature_ability_070(field, player, opponent, virtual, target, itself):
    """
    Evolve: Gain +1/+0 and Ward if there are at least 4 allied Swordcraft followers in play.
    """
    count = 0
    for card in field.card_location[player.player_num]:
        if card.card_class.value == LeaderClass.SWORD.value:
            count += 1
    if count >= 4:
        buff_creature(itself, params=[1, 0])
        add_ability_to_creature(field, player, itself, virtual, add_ability=[KeywordAbility.WARD.value])


def creature_ability_071(field, player, opponent, virtual, target, itself):
    """
    Fanfare: Gain Storm if an allied Commander card is in play.
    """
    for card in field.card_location[player.player_num]:
        if card.trait.value == Trait.COMMANDER.value:
            add_ability_to_creature(field, player, itself, virtual, add_ability=[KeywordAbility.STORM.value])
            return


def creature_ability_072(field, player, opponent, virtual, target, itself):
    """
    Evolve: Destroy an enemy follower if an allied Neutral follower is in play.
    """

    if target is None: return
    # if virtual:
    ##    mylogger.info("first:{},turn_player_num:{}".format(first,field.turn_player_num))
    for card in field.card_location[player.player_num]:
        if card.card_class.value == LeaderClass.NEUTRAL.value:
            if not virtual:
                mylogger.info("hit")
            destroy_opponent_creature(field, opponent, virtual, target)
            return


def creature_ability_073(field, player, opponent, virtual, target, itself):
    """
    Fanfare: Enhance (9) - Can attack 2 times per turn. Reduce damage to 0 until the end of the turn.
    """
    if itself.active_enhance_code[0]:
        itself.can_attack_num = 2
        if not virtual:
            mylogger.info("{} get 'can attack 2 times per turn' ".format(itself.name))
        add_ability_until_end_of_player_turn(field, player, itself, virtual,
                                             add_ability=[KeywordAbility.REDUCE_DAMAGE_TO_ZERO.value])


def creature_ability_074(field, player, opponent, virtual, target, itself):
    """
    Fanfare: Summon a Kunoichi Trainee.
    """

    summon_creature(field, player, virtual, name="Kunoichi Trainee", num=1)


def creature_ability_075(field, player, opponent, virtual, target, itself):
    """
    Fanfare: Draw a card if Overflow is active for you.
    """
    if player.check_overflow() == True:
        draw_cards(player, virtual, num=1)


def creature_ability_076(field, player, opponent, virtual, target, itself):
    """
    Fanfare: Put a random Dragoncraft follower from your deck into your hand.
    """
    condition = lambda card: card.card_class.name == "DRAGON" and card.card_category == "Creature"
    search_cards(player, condition, virtual, num=1)


def creature_ability_077(field, player, opponent, virtual, target, itself):
    """
    Fanfare: Put a Fire Lizard into your hand.
    """
    put_card_in_hand(field, player, virtual, name="Fire Lizard", card_category="Creature")


def creature_ability_078(field, player, opponent, virtual, target, itself):
    """
    Fanfare: Destroy a follower, and then put a copy of that follower into play.
    """
    if target is None: return
    card_index = target
    target_creature = field.card_location[card_index[0]][card_index[1]]
    card_name = target_creature.name
    destroy_opponent_creature(field, field.players[card_index[0]], virtual, card_index[1])
    # ability_resolution(self,virtual=False,player_num=0)
    summon_creature(field, field.players[card_index[0]], virtual, name=card_name)


def creature_ability_079(field, player, opponent, virtual, target, itself):
    """
    At the start of your turn, restore 2 defense to your leader.
    """
    if field.turn_player_num == player.player_num:
        field.restore_player_life(player=player, num=2, virtual=virtual)


def creature_ability_080(field, player, opponent, virtual, target, itself):
    """
    Fanfare: Gain Ambush until the end of your opponent's turn.
    """
    add_ability_until_end_of_opponent_turn(field, player, itself, virtual, add_ability=[KeywordAbility.AMBUSH.value])


def creature_ability_081(field, player, opponent, virtual, target, itself):
    """
    Fanfare: Necromancy (4) - Destroy an evolved enemy follower.
    """
    if target is None: return
    if necromancy(field, player, num=4, virtual=virtual):
        if target not in field.get_creature_location()[opponent.player_num]:
            mylogger.info("target_id:{}".format(target))
            field.show_field()
            assert False
        target_creature = field.card_location[opponent.player_num][target]
        if card_setting.creature_target_regulation[itself.target_regulation](target_creature,itself) == False:
        #if itself.target_regulation(target_creature) == False:
            mylogger.info("illigal target error(target={})".format(target))
            field.show_field()
            assert False
        destroy_opponent_creature(field, opponent, virtual, target)


def creature_ability_082(field, player, opponent, virtual, target, itself):
    """
    Fanfare: Give all allied followers Last Words - Summon a Skeleton.
    """



    if not virtual:
        mylogger.info("All Player{}'s follower get Last Words - Summon a Skeleton".format(player.player_num + 1))
    for card in field.card_location[player.player_num]:
        if card.card_category == "Creature":
            card.lastword_ability.append(-3)


def creature_ability_083(field, player, opponent, virtual, target, itself):
    """
    Last Words: Summon 2 Skeletons.
    """
    summon_creature(field, player, virtual, name="Skeleton", num=2)


def creature_ability_084(field, player, opponent, virtual, target, itself):
    """
    Fanfare: Gain +1/+1 and Ward if at least 2 other cards were played this turn.
    """
    if field.players_play_num >= 2:

        buff_creature(itself, params=[1, 1])
        if not virtual:
            mylogger.info("{} get +1/+1".format(itself.name))
        add_ability_to_creature(field, player, itself, virtual,
                                add_ability=[KeywordAbility.WARD.value])


def creature_ability_085(field, player, opponent, virtual, target, itself):
    """
    Fanfare: Gain +2/+2 if at least 2 other cards were played this turn.
    """
    if field.players_play_num >= 2:
        buff_creature(itself, params=[2, 2])
        if not virtual:
            mylogger.info("{} get +2/+2".format(itself.name))


def creature_ability_086(field, player, opponent, virtual, target, itself):
    """
    Fanfare: Deal 1 damage to a random enemy follower 2 times.
    """
    get_damage_to_random_creature(field, opponent, virtual, num=1)
    get_damage_to_random_creature(field, opponent, virtual, num=1)


def creature_ability_087(field, player, opponent, virtual, target, itself):
    """
    Fanfare: Give +1/+1 to all allied followers
    if at least 2 other cards were played this turn.
    """
    if field.players_play_num >= 2:
        for card in field.card_location[player.player_num]:
            if card.card_category == "Creature" and card != itself:
                buff_creature(card, params=[1, 1])
                if not virtual:
                    mylogger.info("{} get +1/+1".format(card.name))


def creature_ability_088(field, player, opponent, virtual, target, itself):
    """
    Fanfare: Give +2/+0 to an allied Officer follower.
    """
    if target is None:
        return
    assert target < len(field.card_location[player.player_num]), "Out-of-range!"
    target_creature = field.card_location[player.player_num][target]
    assert card_setting.creature_target_regulation[itself.target_regulation](target_creature,itself), "invalid target!(name:{})".format(target_creature.name)
    #assert itself.target_regulation(target_creature), "invalid target!(name:{})".format(target_creature.name)
    buff_creature(target_creature, params=[2, 0])
    if not virtual:
        mylogger.info("{} get +2/0".format(target_creature.name))


def creature_ability_089(field, player, opponent, virtual, target, itself):
    """
    Fanfare: Both players draw a card.
    """
    draw_cards(player, virtual)
    if field.check_game_end():
        return
    draw_cards(opponent, virtual)


def creature_ability_090(field, player, opponent, virtual, target, itself):
    """
    Fanfare: Necromancy (4) - Summon a Zombie.
    """
    if necromancy(field, player, num=4, virtual=virtual):
        summon_creature(field, player, virtual, name="Zombie")


def creature_ability_091(field, player, opponent, virtual, target, itself):
    """
    Fanfare: Gain 2 shadows.
    """
    field.graveyard.shadows[player.player_num] += 2
    if not virtual:
        mylogger.info("Gain 2 shadow")


def creature_ability_092(field, player, opponent, virtual, target, itself):
    """
    Last Words: Summon a Zombie.
    """
    summon_creature(field, player, virtual, name="Zombie")


def creature_ability_093(field, player, opponent, virtual, target, itself):
    """
    Last Words: Give Ward to a random allied follower.
    """
    length = len(field.get_creature_location()[player.player_num])
    if length > 0:
        target_id = random.randint(0, length - 1)
        target_creature = field.card_location[player.player_num][target_id]
        add_ability_to_creature(field, player, target_creature, virtual, add_ability=[KeywordAbility.WARD.value])


def creature_ability_094(field, player, opponent, virtual, target, itself):
    """
    Last Words: Summon 2 Zombies.
    """
    summon_creature(field, player, virtual, name="Zombie", num=2)


def creature_ability_095(field, player, opponent, virtual, target, itself):
    """
    Fanfare: Gain +2/+0 if Vengeance is active for you.
    """
    if player.check_vengeance():
        buff_creature(itself, params=[2, 0])


def creature_ability_096(field, player, opponent, virtual, target, itself):
    """
    Fanfare: Deal 5 damage to an enemy follower if Vengeance is active for you.
    """
    if target is None:
        return
    if player.check_vengeance():
        assert target < len(field.card_location[opponent.player_num]), "Out-of-range"
        get_damage_to_creature(field, opponent, virtual, target, num=5)


def creature_ability_097(field, player, opponent, virtual, target, itself):
    """
    Fanfare: Restore 5 defense to an ally.
    """
    assert target is not None, "non-target-error"
    if target == -1:
        field.restore_player_life(player=player, num=5, virtual=virtual)
    else:
        assert target in field.get_creature_location()[player.player_num], \
            "illegal target error {} not in {}".format(target, field.get_creature_location()[player.player_num])
        target_follower = field.card_location[player.player_num][target]
        field.restore_follower_toughness(follower=target_follower, num=5, virtual=virtual)


def creature_ability_098(field, player, opponent, virtual, target, itself):
    """
    Evolve: Put a Puppet into your hand. Give a random Puppet in your hand Bane.
    """
    put_card_in_hand(field, player, virtual, name="Puppet", card_category="Creature")
    target_ids = []
    for card_id, card in enumerate(player.hand):
        if card.name == "Puppet":
            target_ids.append(card_id)
    if len(target_ids) > 0:
        target_id = random.choice(target_ids)
        target_follower = player.hand[target_id]
        add_ability_to_creature(field, player, target_follower, virtual,
                                add_ability=[KeywordAbility.BANE.value])


def creature_ability_099(field, player, opponent, virtual, target, itself):
    """
    Fanfare: If Resonance is active for you, gain Rush.
    """
    if player.check_resonance():
        add_ability_to_creature(field, player, itself, virtual,
                                add_ability=[KeywordAbility.RUSH.value])


def creature_ability_100(field, player, opponent, virtual, target, itself):
    """
    Fanfare: Put 2 Analyzing Artifacts into your deck.
    """
    cards = [card_setting.Creature(card_setting.creature_name_to_id["Analyzing Artifact"]),
             card_setting.Creature(card_setting.creature_name_to_id["Analyzing Artifact"])]
    #cards.append(card_setting.Creature(card_setting.creature_name_to_id["Analyzing Artifact"]))
    #cards.append(card_setting.Creature(card_setting.creature_name_to_id["Analyzing Artifact"]))
    put_cards_into_deck(field, player, cards, virtual)


def creature_ability_101(field, player, opponent, virtual, target, itself):
    """
    Put a Puppet into your hand.
    """
    put_card_in_hand(field, player, virtual, name="Puppet", card_category="Creature")


def creature_ability_102(field, player, opponent, virtual, target, itself):
    """
    Put 2 Radiant Artifacts into your deck.
    """
    cards = [card_setting.Creature(card_setting.creature_name_to_id["Radiant Artifact"]),
             card_setting.Creature(card_setting.creature_name_to_id["Radiant Artifact"])]
    #cards.append(card_setting.Creature(card_setting.creature_name_to_id["Radiant Artifact"]))
    #cards.append(card_setting.Creature(card_setting.creature_name_to_id["Radiant Artifact"]))
    put_cards_into_deck(field, player, cards, virtual)


def creature_ability_103(field, player, opponent, virtual, target, itself):
    """
    Put a random Artifact card from your deck into your hand.
    """
    condition = lambda card: card.trait.name == "ARTIFACT"
    search_cards(player, condition, virtual)


def creature_ability_104(field, player, opponent, virtual, target, itself):
    """
    Fanfare: Summon a Heavy Knight.
    """
    summon_creature(field, player, virtual, name="Heavy Knight")


def creature_ability_105(field, player, opponent, virtual, target, itself):
    if target is not None and field.get_can_be_targeted(player_num=player.player_num) != []:
        get_damage_to_creature(field, opponent, virtual, target, num=2)


def creature_ability_106(field, player, opponent, virtual, target, itself):
    """
    Fanfare: Recover 10 play points.
    Fanfare: Earth Rite - Banish all cards in your hand, then draw 9 cards.
    """
    field.resotre_pp(player_num=player.player_num, num=10, virtual=virtual)
    if earth_rite(field, player, virtual):
        if not virtual:
            mylogger.info("Banish all cards in Player{}'s hand, then draw 9 cards.".format(player.player_num + 1))
        player.hand.clear()
        draw_cards(player, virtual, num=9)


"""
def restore_1_defense_to_all_allies(field, player, virtual, state_log=None):
    if state_log[0] != State_Code.END_OF_TURN.value:
        return
    if state_log[1] != player.player_num:
        return
    if not virtual:
        mylogger.info("De La Fille, Gem Princess's leader effect is actived")
    field.restore_player_life(player=player, num=1, virtual=virtual)
    for follower in field.card_location[player.player_num]:
        if follower.card_category == "Creature":
            field.restore_follower_toughness(follower=follower, num=1, virtual=virtual, at_once=True)
"""


def creature_ability_107(field, player, opponent, virtual, target, itself):
    """
    Fanfare: Give your leader the following effect - At the end of your turn,
    restore 1 defense to all allies. (This effect is not stackable and lasts for the rest of the match.)
    """

    #if all(ability.name != "restore_1_defense_to_all_allies" for ability in field.player_ability[player.player_num]):
    if all(ability_id != 2 for ability_id in field.player_ability[player.player_num]):
        if not virtual:
            mylogger.info("Give Player{} the following effect - At the end of your turn,restore 1 defense to all allies. "
                          .format(player.player_num + 1)+\
                          "(This effect is not stackable and lasts for the rest of the match.)")

        #field.player_ability[player.player_num].append(Player_Ability_setting.restore_1_defense_to_all_allies())
        field.player_ability[player.player_num].append(Player_Ability_setting.restore_1_defense_to_all_allies().ability_id)
        if field.player_ability[player.player_num].count(2) > 1:
            mylogger.info("player_ability:{}".format(field.player_ability))
            #mylogger.info("names:{}".format([ability.name for ability in field.player_ability[player.player_num]]))
            assert False


def creature_ability_108(field, player, opponent, virtual, target, itself):
    """
    Fanfare: Restore 1 defense to all allies.
    Enhance (7): Gain +4/+4 and restore 4 defense instead.
    """
    value = 1
    if itself.active_enhance_code[0]:
        value = 4
        buff_creature(itself, params=[4, 4])
    if not virtual:
        mylogger.info("Restore {} defense to all allies.".format(value))
    field.restore_player_life(player=player, num=value, virtual=virtual)
    for follower in field.card_location[player.player_num]:
        if follower.card_category == "Creature":
            field.restore_follower_toughness(follower=follower, num=value, virtual=virtual, at_once=True)


def creature_ability_109(field, player, opponent, virtual, target, itself):
    """
    Evolve: Spellboost the cards in your hand 2 times.
    """
    field.spell_boost(player.player_num)
    field.spell_boost(player.player_num)


def creature_ability_110(field, player, opponent, virtual, target, itself):
    """
    Fanfare: Deal a pool of 3 damage divided between all enemies.
    First deal damage to the earliest-played enemy follower.
    (If there is enough damage in the pool, deal damage equal to that follower's defense.)
    Then deal damage to other enemy followers in the order they were played.
    If any damage is left in the pool afterward, deal it to the enemy leader.
    Spellboost: Deal 1 more damage.
    """
    amount = 3 + itself.spell_boost
    for i,follower in enumerate(field.card_location[opponent.player_num]):
        if follower.card_category == "Creature":
            damage = min(amount,follower.get_current_toughness())
            get_damage_to_creature(field,opponent,virtual,i,num=damage)
            amount -= damage
            if amount <=0:
                assert amount == 0
                return
    get_damage_to_player(opponent,virtual,num=amount)


def creature_ability_111(field, player, opponent, virtual, target, itself):
    """
    Fanfare: Restore X defense to your leader. X equals the number of other cards in your hand.
    """
    restore_player_life(player,virtual,num=len(player.hand))


def creature_ability_112(field, player, opponent, virtual, target, itself):
    """
    Can only attack the enemy leader and followers with Ward.
    Last Words: Summon a Lich.
    """
    summon_creature(field,player,virtual,name="Lich")


def creature_ability_113(field, player, opponent, virtual, target, itself):
    """
    Fanfare: Deal 2 damage to a random enemy follower. Then give +2/+0 to another random allied follower.
    """
    get_damage_to_random_creature(field,opponent,virtual,num=2)
    target_ids = field.get_creature_location()[player.player_num]
    target_ids.pop(-1)
    if target_ids == []:
        return
    target_id = random.choice(target_ids)
    follower = field.card_location[player.player_num][target_id]
    buff_creature(follower,params=[2,0])


def creature_ability_114(field, player, opponent, virtual, target, itself):
    """
    Fanfare: Summon a Ghost if an evolved allied follower is in play.
    """
    if any(follower.card_category == "Creature" and
           follower.evolved for follower in field.card_location[player.player_num]):
        summon_creature(field,player,virtual,name="Ghost")


def creature_ability_115(field, player, opponent, virtual, target, itself):
    """
    Deal 1 damage to an enemy.(Angel of the word,etc...)
    """
    get_damage_to_enemy(field,opponent,virtual,target,num=1)
    """
    if target == -1:
        get_damage_to_player(opponent,virtual,num=1)
    else:
        get_damage_to_creature(field,opponent,virtual,target,num=1)
    """


def creature_ability_116(field, player, opponent, virtual, target, itself):
    """
    Fanfare: Put Coco and Mimi into your hand.
    """
    put_card_in_hand(field,player,virtual,name="Mimi",card_category="Spell")
    put_card_in_hand(field, player, virtual, name="Coco", card_category="Spell")


def creature_ability_117(field, player, opponent, virtual, target, itself):
    """
    Evolve: Give +1/+1 to all other allied Neutral followers.
    """
    for follower in field.card_location[player.player_num]:
        if follower.card_category != "Creature":
            continue
        if follower.card_class.value == LeaderClass.NEUTRAL.value and follower is not itself:
            buff_creature(follower,params=[1,1])


def creature_ability_118(field, player, opponent, virtual, target, itself):
    """
    Fanfare: Put a random Bloodcraft follower whose attack is 5 and over from your deck into your hand.
    Enhance (5): Then subtract 3 from the cost of the card in your hand.
    """
    condition = lambda follower:follower.card_category == "Creature" \
                                and follower.card_class.value == LeaderClass.BLOOD.value \
                                    and follower.power >= 5
    searched_card = search_cards(player,condition,virtual)
    if searched_card is not None and itself.active_enhance_code[0]:
        searched_card[0].cost = max(searched_card[0].cost - 3,0)
        if not virtual:
            mylogger.info("3 is subtracted from {}'s cost".format(searched_card[0].name))

def creature_ability_119(field, player, opponent, virtual, target, itself):
    """
    Summon a Goblin at the end of your turn.
    """
    if field.turn_player_num == player.player_num:
        summon_creature(field,player,virtual,name="Goblin")

def creature_ability_120(field, player, opponent, virtual, target, itself):
    """
    Fanfare: Give +1/+1 to all other allied Neutral followers in your hand and in play.
    """
    creature_ability_117(field,player,opponent,virtual,target,itself)
    for hand_card in player.hand:
        if hand_card.card_category != "Creature":
            continue
        if hand_card.card_class.value == LeaderClass.NEUTRAL.value:
            buff_creature(hand_card, params=[1, 1])

def creature_ability_121(field, player, opponent, virtual, target, itself):
    """
    Fanfare: Destroy an enemy follower with 3 defense or less.
    Deal 2 damage to your leader if Vengeance is not active for you.
    """
    if target is not None:
        destroy_opponent_creature(field,opponent,virtual,target)
    if not player.check_vengeance():
        get_damage_to_player(player,virtual,num=2)


def creature_ability_122(field, player, opponent, virtual, target, itself):
    """
    Fanfare: Deal 2 damage to an enemy. Then restore 2 defense to your leader.
    """
    get_damage_to_enemy(field,opponent,virtual,target,num=2)
    restore_player_life(player,virtual,num=2)


def creature_ability_123(field, player, opponent, virtual, target, itself):
    """
    Fanfare: Restore 4 defense to your leader if Vengeance is active for you.
    """
    if player.check_vengeance():
        restore_player_life(player,virtual,num=4)


def creature_ability_124(field, player, opponent, virtual, target, itself):
    """
    Fanfare: Destroy an enemy follower or amulet. Gain Storm if Vengeance is active for you.
    """
    destroy_opponent_card(field,opponent,virtual,target)
    if player.check_vengeance():
        add_ability_to_creature(field,player,itself,virtual,add_ability=[KeywordAbility.STORM.value])


def creature_ability_125(field, player, opponent, virtual, target, itself):
    """
    Last Words: Deal 6(8) damage to the enemy leader if Ambush is active for this follower.
    """
    if KeywordAbility.AMBUSH.value in itself.ability:
        get_damage_to_player(opponent,virtual,num=6+int(itself.evolved)*2)

def token_creature_ability_001(field, player, opponent, virtual, target, itself):
    """
    Last Words: If it is your turn, then put a random Artifact card from your deck into your hand.
    If it is your opponent's turn, draw a card.
    """
    if field.turn_player_num == player.player_num:
        condition = lambda card: card.trait.name == "ARTIFACT"
        search_cards(player, condition, virtual)
    else:
        draw_cards(player, virtual)


def token_creature_ability_002(field, player, opponent, virtual, target, itself):
    """
    At the end of your opponent's turn, destroy this follower.
    """
    if field.turn_player_num == opponent.player_num:
        itself_index = field.card_location[player.player_num].index(itself)
        destroy_opponent_creature(field, player, virtual, itself_index)
        # field.remove_card([player.player_num,itself_index],virtual)

def token_creature_ability_003(field, player, opponent, virtual, target, itself):
    """
    summon skelton
    """
    summon_creature(field, player, virtual, name="Skeleton", num=1)


creature_ability_dict = {
    0: None, 1: creature_ability_001, 2: creature_ability_002, 3: creature_ability_003,
    4: creature_ability_004, 5: creature_ability_005, 6: creature_ability_006,
    7: creature_ability_007, 8: creature_ability_008,
    9: creature_ability_009, 10: creature_ability_010, 11: creature_ability_011,
    12: creature_ability_012, 13: creature_ability_013,
    14: creature_ability_014, 15: creature_ability_015, 16: creature_ability_016,
    17: creature_ability_017, 18: creature_ability_018,
    19: creature_ability_019, 20: creature_ability_020, 21: creature_ability_021,
    22: creature_ability_022, 23: creature_ability_023,
    24: creature_ability_024, 25: creature_ability_025, 26: creature_ability_026,
    27: creature_ability_027, 28: creature_ability_028,
    29: creature_ability_029, 30: creature_ability_030, 31: creature_ability_031,
    32: creature_ability_032, 33: creature_ability_033,
    34: creature_ability_034, 35: creature_ability_035, 36: creature_ability_036,
    37: creature_ability_037, 38: creature_ability_038,
    39: creature_ability_039, 40: creature_ability_040, 41: creature_ability_041,
    42: creature_ability_042, 43: creature_ability_043,
    44: creature_ability_044, 45: creature_ability_045, 46: creature_ability_046,
    47: creature_ability_047, 48: creature_ability_048,
    49: creature_ability_049, 50: creature_ability_050, 51: creature_ability_051,
    52: creature_ability_052, 53: creature_ability_053,
    54: creature_ability_054, 55: creature_ability_055, 56: creature_ability_056,
    57: creature_ability_057, 58: creature_ability_058,
    59: creature_ability_059, 60: creature_ability_060, 61: creature_ability_061,
    62: creature_ability_062, 63: creature_ability_063,
    64: creature_ability_064, 65: creature_ability_065, 66: creature_ability_066,
    67: creature_ability_067, 68: creature_ability_068,
    69: creature_ability_069, 70: creature_ability_070, 71: creature_ability_071,
    72: creature_ability_072, 73: creature_ability_073,
    74: creature_ability_074, 75: creature_ability_075, 76: creature_ability_076,
    77: creature_ability_077, 78: creature_ability_078,
    79: creature_ability_079, 80: creature_ability_080, 81: creature_ability_081,
    82: creature_ability_082, 83: creature_ability_083, 84: creature_ability_084,
    85: creature_ability_085, 86: creature_ability_086, 87: creature_ability_087,
    88: creature_ability_088, 89: creature_ability_089, 90: creature_ability_090,
    91: creature_ability_091, 92: creature_ability_092, 93: creature_ability_093,
    94: creature_ability_094, 95: creature_ability_095, 96: creature_ability_096,
    97: creature_ability_097, 98: creature_ability_098, 99: creature_ability_099,
    100: creature_ability_100, 101: creature_ability_101, 102: creature_ability_102,
    103: creature_ability_103, 104: creature_ability_104, 105: creature_ability_105,
    106: creature_ability_106, 107: creature_ability_107, 108: creature_ability_108,
    109: creature_ability_109, 110: creature_ability_110, 111: creature_ability_111,
    112: creature_ability_112, 113: creature_ability_113, 114: creature_ability_114,
    115: creature_ability_115, 116: creature_ability_116, 117: creature_ability_117,
    118: creature_ability_118, 119: creature_ability_119, 120: creature_ability_120,
    121: creature_ability_121, 122: creature_ability_122, 123: creature_ability_123,
    124: creature_ability_124, 125: creature_ability_125,
    -1: token_creature_ability_001, -2: token_creature_ability_002,-3: token_creature_ability_003,
    "ability_until_end_of_opponent_turn":util_ability.ability_until_end_of_opponent_turn,
    "ability_until_end_of_player_turn":util_ability.ability_until_end_of_player_turn}
