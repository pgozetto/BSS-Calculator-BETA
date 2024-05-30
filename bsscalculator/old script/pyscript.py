import webbrowser
from time import sleep

c = 1
print(" =-=- BSS calculator -=-=")
print(" - Welcome to the BSS Calculator!")
while c <= 4:
    ui = int(input("--> What you want to ACCESS? \n I BSS Calculator [1] \n I Version [2] \n I Credits [3] \n I Exit [4] \n : "))
    # body
    if ui >= 4:
        break
    if ui == 3:
        sleep(0.5)
        print("Creator = Pedro Gozetto / pgozetto / piter")
        print(" -"*20)
        sleep(1)
    if ui == 2:
        sleep(0.5)
        print("The Aplication Version is (v.0.3.0) \n New Things in Soon...")
        print(" -"*20)
        sleep(1)
    if ui == 1:
        for p in range(1,11):
            sleep(0.5)
            print("=-"*20)
            c = int(input(" For Enzymes [1] \n For Oils [2] \n For Blue Extracts [3] \n For Red Extracts [4] \n For Tropical Drinks [5] \n For Glue [6] \n For Moon Charms(CF) [7] \n For Glitter [8] \n For SoftWaxes [9] \n For HardWaxes [10] \n For SwirledWaxes [11] \n For CausticWaxes [12] \n For Purple Potion [13] \n For Super Smoothie [14] \n For GummyDrops [15]\n : "))
            if c == 1:
                cr1 = int(input(" - Enzymes Quantity = "))
                rj = cr1*10
                pine = cr1*(50)
                print(" For {} Enzymes, you will need: \n ->     Royal Jelly = {} \n ->     PineApples = {}".format(cr1, rj, pine))
            elif c == 2:
                cr2 = int(input(" - Oils Quantity = "))
                rj = cr2*10
                sun = cr2*(50)
                print(" For {} Oils, you will need: \n ->      Royal Jelly = {} \n ->      Sunflower Seeds = {}".format(cr2, rj, sun))
            elif c == 3:
                cr3 = int(input(" - Blue Extract Quantity = "))
                rj = cr3*10
                blub = cr3*(50)
                print(" For {} Blue Extracts, you will need: \n ->      Royal Jelly = {} \n ->      BlueBerry = {}".format(cr3, rj, blub))
            elif c == 4:
                cr4 = int(input(" - Red Extract Quantity = "))
                rj = cr4*10
                straw = cr4*(50)
                print(" For {} Red Extracts, you will need: \n ->      Royal Jelly = {} \n ->      StrawBerry = {}".format(cr4, rj, straw))
            elif c == 5:
                cr5 = int(input(" - Tropical Drink Quantity = "))
                o = cr5*2
                en = cr5*2
                coco = cr5*(10)
                print(" For {} Tropical Drink, you will need: \n ->      Coconut = {} \n -> Oil      = {} \n ->      Enzymes = {}".format(cr5, coco, o, en))
            elif c == 6:
                cr6 = int(input(" - Glue Quantity = "))
                rj = cr6*10
                gum = cr6*(50)
                print(" For {} Glue, you will need: \n      -> Royal Jelly = {} \n ->      GummyDrops = {}".format(cr6, rj, gum))
            elif c == 7:
                cr7 = int(input(" - Moon Charms Quantity = "))
                rj = cr7*1
                pine = cr7*5
                gum = cr7*5
                print(" For {} Moon Charms, you will need: \n ->      Royal Jelly = {} \n ->      PineApple = {} \n ->      GummyDrops = {}".format(cr7, rj, pine, gum))
            elif c == 8:
                cr8 = int(input(" - Glitter Quantity = "))
                bean = cr8*1
                moon1 = cr8*(25)
                print(" For {} Glitter, you will need: \n ->      Magic Bean = {} \n ->      Moon Charms = {}".format(cr8, bean, moon1))
            elif c == 9:
                cr9 = int(input(" - Soft Wax Quantity = "))
                ho = cr9*5
                o = cr9*1
                en = cr9*1
                rj = cr9*33
                print(" For {} Soft Waxes, you will need: \n ->      Honey Suck = {} \n ->      Oil = {} \n ->      Enzymes = {} \n ->      Royal Jelly = {}".
                format(cr9, ho, o, en, rj))
            elif c == 10:
                cr10 = int(input(" - Hard Wax Quantity = "))
                sw = cr10*3
                en = cr10*3
                bi = cr10*33
                rj = cr10*33
                print(" For {} Hard Wax, you will need: \n ->      Soft Waxes = {} \n ->      Enzymes = {} \n ->      Bitter Berries = {} \n ->      Royal Jellys = {}".format(cr10, sw, en, bi, rj))
            elif c == 11:
                cr11 = int(input(" - Swirled Wax Quantity = "))
                hw = cr11*3
                sw = cr11*9
                pp = cr11*6
                rj = cr11*3333
                print(" For {} Swirled Wax, you will need: \n ->      Hard Waxes = {} \n ->      Soft Waxes = {} \n ->      Purple Potions = {} \n ->      Royal Jelly = {}".format(cr11, hw, sw, pp, rj))
            elif c == 12:
                cr12 = int(input(" - Caustic Wax Quantity = "))
                hw = cr12*5
                en = cr12*5
                nb = cr12*25
                rj = cr12*5252
                print(" For {} Caustic Wax, you will need: \n ->      Hard Waxes = {} \n ->      Enzymes = {} \n ->      Neon Berries = {} \n ->      Royal Jelly = {}".format(cr12, hw, sw, pp, rj))
            elif c == 13:
                cr13 = int(input(" - Purple Potion Quantity = "))
                nb = cr13*3
                rs = cr13*3
                bs = cr13*3
                gl = cr13*3
                print(" For {} Purple Potion, you will need: \n ->      Neon Berries = {} \n ->      Red Extracts = {} \n ->      Blue Extracts = {} \n ->      Glues = {}".format(cr13, nb, rs, bs, gl))
            elif c == 14:
                cr14 = int(input(" - Super Smoothie Quantity = "))
                nb = cr14*3
                st = cr14*3
                pp = cr14*3
                td = cr14*6
                print(" For {} Super Smoothie, you will need: \n ->      Neon Berries = {} \n ->      Star Jellies = {} \n ->      Purple Potions = {} \n ->      Tropical Drinks = {}".format(cr14, nb, st, pp, td))
            elif c == 15:
                cr15 = int(input(" - GummyDrops Quantity = "))
                pine = cr15*3
                straw = cr15*3
                blub = cr15*3
                print(" For {} GummyDrops, you will need: \n ->      PineApples = {} \n ->      Strawberries = {} \n ->      Blueberries = {}".format(cr15, pine, straw, blub))
print("--END--")








