import random

def plr_hp(plr1_list, plr2_list, plr1_lv, plr2_lv, plr1_hp, plr2_hp, plr1_num, plr2_num):
    print("\n" + plr2_list[plr2_num][0] + ": lv " + str(plr2_lv[plr2_num]) + "\nHP: " + str(int(round(plr2_hp[plr2_num], 0))) + "/" + str(plr2_list[plr2_num][7]))
    print("\n" + plr1_list[plr1_num][0] + ": lv " + str(plr1_lv[plr1_num]) + "\nHP: " + str(int(round(plr1_hp[plr1_num], 0))) + "/" + str(plr1_list[plr1_num][7]))
##function to format the pkmn and hp on screen

def lv_sys(pkmn_lv_list, plr_pkmn_list):
    pkmn_num = len(plr_pkmn_list)
    for u in plr_pkmn_list:
        if u == "-":
            pkmn_num -= 1
    for i in range(pkmn_num):
        pkmn_lv_list.append(plr_pkmn_list[i][6])
##function logs all the levels of each pkmn into a single list for each plr

def hp_sys(pkmn_hp_list, plr_pkmn_list):
    pkmn_num = len(plr_pkmn_list)
    for u in plr_pkmn_list:
        if u == "-":
            pkmn_num -= 1
    for i in range(pkmn_num):
        pkmn_hp_list.append(plr_pkmn_list[i][7])
##function logs all the hp of each pkmn into a single list for each plr
        
def pp_sys(pkmn_pp_list, plr_pkmn_list):
    pkmn_num = len(plr_pkmn_list)
    for u in plr_pkmn_list:
        if u == "-":
            pkmn_num -= 1
    for c in range(pkmn_num):
        for i in range(4):
            if plr_pkmn_list[c][8 + i] != "":
                pkmn_pp_list[c].append(plr_pkmn_list[c][8 + i][2])
##function logs all the pp of each pkmn move into a single list for each plr

def move_type(n, plr1_pkmn_list, plr2_pkmn_list, crit_con, sp_eff_con, fail_con, plr1_num, plr2_num):
    sp_eff = 1
    stab = 1
    crit = 1
    ##base stats for crit stab and sp_eff
    if fail_con == True:
        dmg = 0
        ##to skip any effects of move usage
    elif plr1_pkmn_list[plr1_num][8 + n][8] == "Physical":   ##detect if move causes dmg or status eff
        usr_atk = (2 * plr1_pkmn_list[plr1_num][6] + 10) * plr1_pkmn_list[plr1_num][12] * plr1_pkmn_list[plr1_num][8 + n][1]
        opp_def = 250 * plr2_pkmn_list[plr2_num][13]
##      sp_eff =
        ##sp_eff function to be created ltr
        if plr1_pkmn_list[plr1_num][8 + n][0] == plr1_pkmn_list[plr1_num][1]:
            stab = 1.5
            ##enables stab if pkmn and move type are same (mutiplyer)
        if crit_con == True:
            pkmn_lv = plr1_pkmn_list[plr1_num][6]
            crit = (2 * pkmn_lv + 5)/(pkmn_lv + 5)
            ##enables crit based on boolean (crit_con) (multiplyer)
        dmg = (usr_atk/opp_def + 2) * sp_eff * stab * crit
        ##calculation of total dmg
    elif plr1_pkmn_list[plr1_num][8 + n][8] == "Status":   ##detect if move causes dmg or status eff
        dmg = 0
        if plr1_pkmn_list[plr1_num][8 + n][6] > 0:  ##atk dn
            plr2_pkmn_list[plr2_num][12] = plr2_pkmn_list[plr2_num][12] * plr1_pkmn_list[plr1_num][8 + n][6]
        elif plr1_pkmn_list[plr1_num][8 + n][7] > 0:  ##def dn
            plr2_pkmn_list[plr2_num][13] = plr2_pkmn_list[plr2_num][13] * plr1_pkmn_list[plr1_num][8 + n][7]
    return dmg

def move_result(n, plr1_pkmn, plr2_pkmn, plr1_pkmn_pp, plr2_pkmn_pp, plr2_pkmn_hp, plr1_num, plr2_num, plr_title, u_1, u_2):
    if plr1_pkmn[plr1_num][8 + n][8] == "Physical":  ##detect if move causes dmg or status eff
        plr1_pkmn_pp[plr1_num][i] -= 1
        if random.randint(1, 256) == 93:
            fail_bool = True
        else:
            fail_bool = False
        ##run a randnum to see if fail is true
        if random.randint(1, 256) == 28:
            crit_bool = True
        else:
            crit_bool = False
        ##run a randnum to see if fail is true
        sp_eff_bool = False  ##temp false since no sp_eff moves
        move_dmg = move_type(n, plr1_pkmn, plr2_pkmn, crit_bool, sp_eff_bool, fail_bool, plr1_num, plr2_num)
        plr2_pkmn_hp[plr2_num] -= move_dmg  ##minus dmg fro opp hp
        input("\n" + title[u_1] + plr1_pkmn[plr1_num][0] + " used " + plr1_pkmn[plr1_num][2 + n] + "!")
        if fail_bool == True:
            input("But it missed!") ##msg for fail
        elif crit_bool == True:
            input("Critical hit!")  ##msg for crit
    elif plr1_pkmn[plr1_num][8 + n][8] == "Status":  ##detect if move causes dmg or status eff
        plr1_pkmn_pp[plr1_num][n] -= 1
        if random.randint(1, 256) == 93:
            fail_bool = True
        else:
            fail_bool = False
        ##run a randnum to see if fail is true
        crit_bool = False
        sp_eff_bool = False
        ##crit and sp_eff have no use for stat change moves so auto false
        move_dmg = move_type(n, plr1_pkmn, plr2_pkmn, crit_bool, sp_eff_bool, fail_bool, plr1_num, plr2_num)
        input("\n" + plr1_pkmn[plr1_num][0] + " used " + plr1_pkmn[plr1_num][2 + n] + "!")  ##msg for move used and by who
        if fail_bool == True:
            input("But it failed!")  ##msg for fail
        if plr1_pkmn[plr1_num][8 + n][6] > 0:
            input(plr_title[u_2] + plr2_pkmn[plr2_num][0] + "'s attack fell!") ##msg for atk dn
        elif plr1_pkmn[plr1_num][8 + n][7] > 0:
            input(plr_title[u_2] + plr2_pkmn[plr2_num][0] + "'s defense fell!")  ##msg for def dn
        
scratch = ["Normal", 40, 35, 100, 0, 0, 0, 0, "Physical"]
growl = ["Normal", 0, 40, 100, 0, 0, 2/3, 0, "Status"]
tackle = ["Normal", 35, 35, 100, 0, 0, 0, 0, "Physical"]
tail_whip = ["Normal", 0, 30, 100, 0, 0, 0, 2/3, "Status"]

##move = [move type, power, pp, accuracy, atk_up, def_up, atk_dn, def_dn, phy/sta]

red_pkmn_1 = ["Charmander", "Fire", "Scratch", "Growl", "", "", 5, 20, scratch, growl, "", "", 1, 1]

red_pkmn_2 = ["Bulbasaur", "Grass", "Tackle", "Growl", "", "", 5, 20, tackle, growl, "", "", 1, 1]

##pkmn = [name, type, move 1, move 2, move 3, move 4, level, hp, move 1 list, move 2 list, move 3 list, move 4 list, atk stat, def stat]

red_pkmn = [red_pkmn_1, red_pkmn_2, "-", "-", "-", "-"]
##pkmn list for plr (can add more pkmn ltr)

blue_pkmn_1 = ["Squirtle", "Water", "Tackle", "Tail Whip", "", "", 5, 20, tackle, tail_whip, "", "", 1, 1]

blue_pkmn = [blue_pkmn_1, "-", "-", "-", "-", "-"]
##pkmn list for usr (can add more pkmn ltr)

##usr pkmn denoted by "red" while opp pkmn denoted by "blue"

red_lose = False
turn_loop = True

input("Blue wants to fight!")
input("Blue sent out " + blue_pkmn[0][0] + "!")
input("Go! " + red_pkmn[0][0] + "!")

red_num = 0
prev_num = red_num
fight_input = "0"
red_pkmn_lv = []
red_pkmn_hp = []

red_pkmn1_pp = []
red_pkmn2_pp = []
red_pkmn3_pp = []
red_pkmn4_pp = []
red_pkmn5_pp = []
red_pkmn6_pp = []

red_pkmn_pp = [red_pkmn1_pp, red_pkmn2_pp, red_pkmn3_pp, red_pkmn4_pp, red_pkmn5_pp, red_pkmn6_pp]
##puts the pp of diff pkmn moves from the difff pkmn into diff lists before putting it in red_pkmn_pp

lv_sys(red_pkmn_lv, red_pkmn)
hp_sys(red_pkmn_hp, red_pkmn)
pp_sys(red_pkmn_pp, red_pkmn)

##diff hp, lvl and pp lists for user

blue_num = 0
blue_pkmn_lv = []
blue_pkmn_hp = []

blue_pkmn1_pp = []
blue_pkmn2_pp = []
blue_pkmn3_pp = []
blue_pkmn4_pp = []
blue_pkmn5_pp = []
blue_pkmn6_pp = []

blue_pkmn_pp = [blue_pkmn1_pp, blue_pkmn2_pp, blue_pkmn3_pp, blue_pkmn4_pp, blue_pkmn5_pp, blue_pkmn6_pp]
##puts the pp of diff pkmn moves from the difff pkmn into diff lists before putting it in blue_pkmn_pp

lv_sys(blue_pkmn_lv, blue_pkmn)
hp_sys(blue_pkmn_hp, blue_pkmn)
pp_sys(blue_pkmn_pp, blue_pkmn)

##diff hp, lvl and pp lists for opp

title = ["", "Enemy "]
##this is to identify usr and opp pkmn in text

while turn_loop == True:
    plr_hp(red_pkmn, blue_pkmn, red_pkmn_lv, blue_pkmn_lv, red_pkmn_hp, blue_pkmn_hp, red_num, blue_num)
    print("\nWhat will " + red_pkmn[red_num][0] + " do?")
    print("1. Fight \n2. Pokémon \n3. Item \n4. Run")
    menu_input = input("Enter your input here: ")
    ##formating of menu

    if menu_input == "1":  ##move menu
        print("\nWhat will " + red_pkmn[red_num][0] + " use?")
        for i in range(4):
            if red_pkmn[red_num][8 + i] == "":
                break
            else:
                print(str(i + 1) + ". Type: " + red_pkmn[red_num][8 + i][0] + "\n   " + red_pkmn[red_num][2 + i] + " " + str(red_pkmn_pp[red_num][i]) + "/" + str(red_pkmn[red_num][8 + i][2]))
        fight_input = input("Enter your input here: ")
        ##formatting of move menu
        u1_num = 0
        u2_num = 1
        if fight_input == "0":
            turn_loop = True
            ##to skip other functions and return to main menu (does not allow opp to atk)
        if fight_input == "1":  ##move 1
            i = 0
            move_result(i, red_pkmn, blue_pkmn, red_pkmn_pp, blue_pkmn_pp, blue_pkmn_hp, red_num, blue_num, title, u1_num, u2_num)
        elif fight_input == "2":  ##move 2
            i = 1
            tr_num = 1
            move_result(i, red_pkmn, blue_pkmn, red_pkmn_pp, blue_pkmn_pp, blue_pkmn_hp, red_num, blue_num, title, u1_num, u2_num)

    elif menu_input == "2":  ##pkmn menu
        print("\nChoose a Pokémon.")
        for i in range(6):
            if red_pkmn[i] == "-":
                print(str(i + 1) + ". " + red_pkmn[i][0])
            else:
                print(str(i + 1) + ". " + red_pkmn[i][0] + "\n   HP: " + str(int(round(red_pkmn_hp[i], 0))) + "/" + str(red_pkmn[i][7]))
        pkmn_input = int(input("Enter your input here: "))
        ##formatting of pkmn menu
        prev_num = red_num
        red_num = pkmn_input - 1
        if pkmn_input == 0:
            fight_input = "0"
            ##to skip other functions and return to main menu (does not allow opp to atk)
            red_num = prev_num
            ##keeps pkmn the same
        elif red_pkmn_hp[red_num] == 0:
            fight_input = "0"
            input("\n" + red_pkmn[red_num][0] + " is unable to battle!")
            ##checks if chosen pkmn hp is 0 and sends appropriate msg if true
            red_num = prev_num
            ##keeps pkmn the same
        elif prev_num != red_num:
            red_num = pkmn_input - 1
            ##changes the pkmn num
            input("\n" + red_pkmn[prev_num][0] + " come back!")
            input("Go! " + red_pkmn[red_num][0] + "!")
            ##text for pkmn switch out

    elif menu_input == "3":  ##bag menu (to be added)
        input("\nYou have no items.")
        fight_input = "0" ##skip opp atk

    elif menu_input == "4":  ##run (does not work in trainer btl)
        input("\nNo! There\'s no running from a Trainer Battle!")
        fight_input = "0"  #skip opp atk

    if fight_input != "0":  ##allows for one to return to main menu without allowing opp to atk
        blue_move_num = 0
        for i in range(4):
            if blue_pkmn[blue_num][8 + i] == "":
                break
            else:
                blue_move_num += 1
        blue_move = random.randint(1, blue_move_num)  ##picks a move at random
        u1_num = 1
        u2_num = 0
        if red_pkmn[red_num][12] < 1 or red_pkmn[red_num][13] < 1:
            blue_move = 1                                         ## will create more sophisticated system for checking status effects later
        if blue_move == 1:
            i = 0
            move_result(i, blue_pkmn, red_pkmn, blue_pkmn_pp, red_pkmn_pp, red_pkmn_hp, blue_num, red_num, title, u1_num, u2_num)
        elif blue_move == 2:
            i = 1
            move_result(i, blue_pkmn, red_pkmn, blue_pkmn_pp, red_pkmn_pp, red_pkmn_hp, blue_num, red_num, title, u1_num, u2_num)

    if red_pkmn_hp[red_num] <= 0:
        red_pkmn_hp[red_num] = 0
        plr_hp(red_pkmn, blue_pkmn, red_pkmn_lv, blue_pkmn_lv, red_pkmn_hp, blue_pkmn_hp, red_num, blue_num)
        for i in range(len(red_pkmn_hp)):
            if red_pkmn_hp[i] > 0:
                input("\n" + red_pkmn[red_num][0] + " fainted!")
                red_num = i
                input("Go! " + red_pkmn[red_num][0] + "!")
                ##auto swap out sys for fainted pkmn

        if red_pkmn_hp[red_num] <= 0:
            red_lose = True
            turn_loop = False
            
        elif blue_pkmn_hp[blue_num] <= 0:
            turn_loop = False
        ##checks if usr lost or won based on all pkmn hp (red_pkmn_hp)

    elif blue_pkmn_hp[blue_num] <= 0:
        blue_pkmn_hp[blue_num] = 0
        plr_hp(red_pkmn, blue_pkmn, red_pkmn_lv, blue_pkmn_lv, red_pkmn_hp, blue_pkmn_hp, red_num, blue_num)
        for i in range(len(blue_pkmn_hp)):
            if blue_pkmn_hp[i] > 0:
                input("\n Enemy" + blue_pkmn[blue_num][0] + " fainted!")
                red_num = i
                input("Blue sent out " + blue_pkmn[blue_num][0] + "!")
                ##auto swap out sys for fainted pkmn

        if red_pkmn_hp[red_num] <= 0:
            red_lose = True
            turn_loop = False
            
        elif blue_pkmn_hp[blue_num] <= 0:
            turn_loop = False
        ##checks if usr lost or won based on all pkmn hp (red_pkmn_hp)
            
if red_lose == False:
    input("\nEnemy " + blue_pkmn[blue_num][0] + " fainted!")
    input("Red defeated Blue!")
    input("Blue: What? Unbelievable! I picked the wrong Pokémon!")
    input("Red got ₽175 for winning!")
    ##text for winning
elif red_lose == True:
    input("\n" + red_pkmn[red_num][0] + " fainted!")
    input("Blue defeated Red!")
    input("Blue: Yeah! Am I great or what?")
    ##text for losing


##do not enter any input besides 1, 2 or 0 for move and pkmn menu, main menu only 1, 2, 3 and 4 or else will break (will fix data validation ltr)
