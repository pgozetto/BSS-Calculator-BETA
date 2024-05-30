from customtkinter import *

# start
app = CTk()
app.geometry("650x650")
app.title("BSS Calculator")
set_appearance_mode("dark")

# tabs

tab = CTkTabview(master=app, width=(650), height=(650), bg_color="#FFFF00", fg_color="#111111", text_color="#000000", border_color="#FFFF00", border_width=0.6, corner_radius=36, segmented_button_selected_color="#FFFF00", segmented_button_selected_hover_color="#FFFF00")
tab.pack()

tab1 = tab.add("BSS Calculator") 
tab2 = tab.add("Version")
tab3 = tab.add("Credits")
# tab2
blank = CTkLabel(master=tab2, text="---------->", width=(150), height=(35), fg_color="#111111", text_color="#FFFF00", corner_radius=10, font=("Arial", 30))
blank.grid(row=1, column=1, padx=10, pady=10)
cre =  CTkLabel(master=tab2, text="v(a.0.2)", width=(150), height=(35), fg_color="#111111", text_color="#FFFF00", corner_radius=10, font=("Arial", 30))
cre.grid(row=1, column=2, padx=10, pady=10)
# tab3
blank2 = CTkLabel(master=tab3, text="---------->", width=(150), height=(35), fg_color="#111111", text_color="#FFFF00", corner_radius=10, font=("Arial", 20))
blank2.grid(row=2, column=1, padx=10, pady=10)
blank = CTkLabel(master=tab3, text="---------->", width=(150), height=(35), fg_color="#111111", text_color="#FFFF00", corner_radius=10, font=("Arial", 20))
blank.grid(row=1, column=1, padx=10, pady=10)
cre =  CTkLabel(master=tab3, text="Creators", width=(150), height=(35), fg_color="#111111", text_color="#FFFF00", corner_radius=10, font=("Arial", 20))
cre.grid(row=1, column=2, padx=10, pady=10)
cre =  CTkLabel(master=tab3, text="Pedro Gozetto / pgozetto", width=(150), height=(35), fg_color="#111111", text_color="#FFFF00", corner_radius=10, font=("Arial", 20))
cre.grid(row=2, column=2, padx=10, pady=10)
# tab1

def enzy():
    def val():
        calc = int(t1.get())
        t1.configure(state="disable")
        rj =  calc*10
        pine = calc*50
        space = CTkLabel(master=tab1, text="* Result *")
        space.grid(row=7, column=0 )
        srj = CTkLabel(master=tab1,font=("Arial", 20), text="Total Royal Jellies = {}".format(rj), text_color="#FFFF00")
        srj.grid(row=8, column=0 )
        spine = CTkLabel(master=tab1,font=("Arial", 20), text="Total PineApples = {}".format(pine), text_color="#FFFF00")
        spine.grid(row=9, column=0 )
    def clear():
        t1.configure(state="normal")
        t1.delete(0, END)
    t1 = CTkEntry(master=tab1, height=(40), width=170,fg_color="#222222", corner_radius=8, border_width=3, border_color="#FFFF00", placeholder_text="Quantity (1, 10...)", placeholder_text_color="#999999",)
    t1.grid(row=6, column=0, padx=0, pady=0)
    s = CTkButton(master=tab1, text="Enviar", fg_color="#222222", corner_radius=8, border_width=3, border_color="#FFFF00", command=val)
    s.grid(row=6, column=2, padx=0, pady=0)
    c = CTkButton(master=tab1, text="Limpar", fg_color="#222222", corner_radius=8, border_width=3, border_color="#FFFF00", command=clear)
    c.grid(row=6, column=3, padx=0, pady=0)

def oil():
    def val():
        calc = int(t2.get())
        t2.configure(state="disable")
        rj =  calc*10
        ssuns = calc*50

        space = CTkLabel(master=tab1, text="* Result *")
        space.grid(row=7, column=0 )

        srj = CTkLabel(master=tab1,font=("Arial", 20), text="Total Royal Jellies = {}".format(rj), text_color="#FFFF00")
        srj.grid(row=8, column=0 )
        ssuns = CTkLabel(master=tab1,font=("Arial", 20), text="Total SunflowerSeeds = {}".format(ssuns), text_color="#FFFF00")
        ssuns.grid(row=9, column=0 )
    def clear():
        t2.configure(state="normal")
        t2.delete(0, END)
    t2 = CTkEntry(master=tab1, height=(40), width=170,fg_color="#222222", corner_radius=8, border_width=3, border_color="#FFFF00", placeholder_text="Quantity (1, 10...)", placeholder_text_color="#999999",)
    t2.grid(row=6, column=0, padx=0, pady=0)
    s = CTkButton(master=tab1, text="Enviar", fg_color="#222222", corner_radius=8, border_width=3, border_color="#FFFF00", command=val)
    s.grid(row=6, column=2, padx=0, pady=0)
    c = CTkButton(master=tab1, text="Limpar", fg_color="#222222", corner_radius=8, border_width=3, border_color="#FFFF00", command=clear)
    c.grid(row=6, column=3, padx=0, pady=0)
def bex():
    def val():
        calc = int(t2.get())
        t2.configure(state="disable")
        rj =  calc*10
        blub = calc*50

        space = CTkLabel(master=tab1, text="* Result *")
        space.grid(row=7, column=0 )

        srj = CTkLabel(master=tab1,font=("Arial", 20), text="Total Royal Jellies = {}".format(rj), text_color="#FFFF00")
        srj.grid(row=8, column=0 )
        blub = CTkLabel(master=tab1,font=("Arial", 20), text="Total Blueberries = {}".format(blub), text_color="#FFFF00")
        blub.grid(row=9, column=0 )
    def clear():
        t2.configure(state="normal")
        t2.delete(0, END)
    t2 = CTkEntry(master=tab1, height=(40), width=170,fg_color="#222222", corner_radius=8, border_width=3, border_color="#FFFF00", placeholder_text="Quantity (1, 10...)", placeholder_text_color="#999999",)
    t2.grid(row=6, column=0, padx=0, pady=0)
    s = CTkButton(master=tab1, text="Enviar", fg_color="#222222", corner_radius=8, border_width=3, border_color="#FFFF00", command=val)
    s.grid(row=6, column=2, padx=0, pady=0)
    c = CTkButton(master=tab1, text="Limpar", fg_color="#222222", corner_radius=8, border_width=3, border_color="#FFFF00", command=clear)
    c.grid(row=6, column=3, padx=0, pady=0)
def rex():
    def val():
        calc = int(t2.get())
        t2.configure(state="disable")
        rj =  calc*10
        straw = calc*50

        space = CTkLabel(master=tab1, text="* Result *")
        space.grid(row=7, column=0 )

        srj = CTkLabel(master=tab1,font=("Arial", 20), text="Total Royal Jellies = {}".format(rj), text_color="#FFFF00")
        srj.grid(row=8, column=0 )
        straw = CTkLabel(master=tab1,font=("Arial", 20), text="Strawberries = {}".format(straw), text_color="#FFFF00")
        straw.grid(row=9, column=0 )
    def clear():
        t2.configure(state="normal")
        t2.delete(0, END)
        
    t2 = CTkEntry(master=tab1, height=(40), width=170,fg_color="#222222", corner_radius=8, border_width=3, border_color="#FFFF00", placeholder_text="Quantity (1, 10...)", placeholder_text_color="#999999",)
    t2.grid(row=6, column=0, padx=0, pady=0)
    s = CTkButton(master=tab1, text="Enviar", fg_color="#222222", corner_radius=8, border_width=3, border_color="#FFFF00", command=val)
    s.grid(row=6, column=2, padx=0, pady=0)
    c = CTkButton(master=tab1, text="Limpar", fg_color="#222222", corner_radius=8, border_width=3, border_color="#FFFF00", command=clear)
    c.grid(row=6, column=3, padx=0, pady=0)
def tdk():
    def val():
        calc = int(t2.get())
        t2.configure(state="disable")
        coc =  calc*10
        enzy = calc*2
        oil = calc*2

        space = CTkLabel(master=tab1, text="* Result *")
        space.grid(row=7, column=0 )

        coc = CTkLabel(master=tab1,font=("Arial", 20), text="Total Coconuts = {}".format(coc), text_color="#FFFF00")
        coc.grid(row=8, column=0 )
        enzy = CTkLabel(master=tab1,font=("Arial", 20), text="Total Enzymes = {}".format(enzy), text_color="#FFFF00")
        enzy.grid(row=9, column=0 )
        oil = CTkLabel(master=tab1,font=("Arial", 20), text="Total Oils = {}".format(oil), text_color="#FFFF00")
        oil.grid(row=10, column=0 )
    def clear():
        t2.configure(state="normal")
        t2.delete(0, END)
    t2 = CTkEntry(master=tab1, height=(40), width=170,fg_color="#222222", corner_radius=8, border_width=3, border_color="#FFFF00", placeholder_text="Quantity (1, 10...)", placeholder_text_color="#999999",)
    t2.grid(row=6, column=0, padx=0, pady=0)
    s = CTkButton(master=tab1, text="Enviar", fg_color="#222222", corner_radius=8, border_width=3, border_color="#FFFF00", command=val)
    s.grid(row=6, column=2, padx=0, pady=0)
    c = CTkButton(master=tab1, text="Limpar", fg_color="#222222", corner_radius=8, border_width=3, border_color="#FFFF00", command=clear)
    c.grid(row=6, column=3, padx=0, pady=0)
def bex():
    def val():
        calc = int(t1.get())
        t1.configure(state="disable")
        rj =  calc*10
        blue = calc*50
        space = CTkLabel(master=tab1, text="* Result *")
        space.grid(row=7, column=0 )
        srj = CTkLabel(master=tab1,font=("Arial", 20), text="Total Royal Jellies = {}".format(rj), text_color="#FFFF00")
        srj.grid(row=8, column=0 )
        blue = CTkLabel(master=tab1,font=("Arial", 20), text="Total Blueberries = {}".format(blue), text_color="#FFFF00")
        blue.grid(row=9, column=0 )
    def clear():
        t1.configure(state="normal")
        t1.delete(0, END)
    t1 = CTkEntry(master=tab1, height=(40), width=170,fg_color="#222222", corner_radius=8, border_width=3, border_color="#FFFF00", placeholder_text="Quantity (1, 10...)", placeholder_text_color="#999999",)
    t1.grid(row=6, column=0, padx=0, pady=0)
    s = CTkButton(master=tab1, text="Enviar", fg_color="#222222", corner_radius=8, border_width=3, border_color="#FFFF00", command=val)
    s.grid(row=6, column=2, padx=0, pady=0)
    c = CTkButton(master=tab1, text="Limpar", fg_color="#222222", corner_radius=8, border_width=3, border_color="#FFFF00", command=clear)
    c.grid(row=6, column=3, padx=0, pady=0)
def glue():
    def val():
        calc = int(t1.get())
        t1.configure(state="disable")
        rj =  calc*10
        gum = calc*50
        space = CTkLabel(master=tab1, text="* Result *")
        space.grid(row=7, column=0 )
        srj = CTkLabel(master=tab1,font=("Arial", 20), text="Total GummyDrops = {}".format(rj), text_color="#FFFF00")
        srj.grid(row=8, column=0 )
        gum = CTkLabel(master=tab1,font=("Arial", 20), text="Total PineApples = {}".format(gum), text_color="#FFFF00")
        gum.grid(row=9, column=0 )
    def clear():
        t1.configure(state="normal")
        t1.delete(0, END)
    t1 = CTkEntry(master=tab1, height=(40), width=170,fg_color="#222222", corner_radius=8, border_width=3, border_color="#FFFF00", placeholder_text="Quantity (1, 10...)", placeholder_text_color="#999999",)
    t1.grid(row=6, column=0, padx=0, pady=0)
    s = CTkButton(master=tab1, text="Enviar", fg_color="#222222", corner_radius=8, border_width=3, border_color="#FFFF00", command=val)
    s.grid(row=6, column=2, padx=0, pady=0)
    c = CTkButton(master=tab1, text="Limpar", fg_color="#222222", corner_radius=8, border_width=3, border_color="#FFFF00", command=clear)
    c.grid(row=6, column=3, padx=0, pady=0)
def mc():
    def val():
        calc = int(t1.get())
        t1.configure(state="disable")
        rj =  calc*1
        pine = calc*3
        gum = calc*3
        space = CTkLabel(master=tab1, text="* Result *")
        space.grid(row=7, column=0 )
        srj = CTkLabel(master=tab1,font=("Arial", 20), text="Total Royal Jellies = {}".format(rj), text_color="#FFFF00")
        srj.grid(row=8, column=0 )
        spine = CTkLabel(master=tab1,font=("Arial", 20), text="Total PineApples = {}".format(pine), text_color="#FFFF00")
        spine.grid(row=9, column=0 )
        gum = CTkLabel(master=tab1,font=("Arial", 20), text="Total GummyDrops = {}".format(gum), text_color="#FFFF00")
        gum.grid(row=10, column=0 )
    def clear():
        t1.configure(state="normal")
        t1.delete(0, END)
    t1 = CTkEntry(master=tab1, height=(40), width=170,fg_color="#222222", corner_radius=8, border_width=3, border_color="#FFFF00", placeholder_text="Quantity (1, 10...)", placeholder_text_color="#999999",)
    t1.grid(row=6, column=0, padx=0, pady=0)
    s = CTkButton(master=tab1, text="Enviar", fg_color="#222222", corner_radius=8, border_width=3, border_color="#FFFF00", command=val)
    s.grid(row=6, column=2, padx=0, pady=0)
    c = CTkButton(master=tab1, text="Limpar", fg_color="#222222", corner_radius=8, border_width=3, border_color="#FFFF00", command=clear)
    c.grid(row=6, column=3, padx=0, pady=0)
def gli():
    def val():
        calc = int(t1.get())
        t1.configure(state="disable")
        mc =  calc*25
        mb = calc*1
        space = CTkLabel(master=tab1, text="* Result *")
        space.grid(row=7, column=0 )
        mc = CTkLabel(master=tab1,font=("Arial", 20), text="Total Moon Charms = {}".format(mc), text_color="#FFFF00")
        mc.grid(row=8, column=0 )
        mb = CTkLabel(master=tab1,font=("Arial", 20), text="Total Magic Beans(Sprouts) = {}".format(mb), text_color="#FFFF00")
        mb.grid(row=9, column=0 )
    def clear():
        t1.configure(state="normal")
        t1.delete(0, END)
    t1 = CTkEntry(master=tab1, height=(40), width=170,fg_color="#222222", corner_radius=8, border_width=3, border_color="#FFFF00", placeholder_text="Quantity (1, 10...)", placeholder_text_color="#999999",)
    t1.grid(row=6, column=0, padx=0, pady=0)
    s = CTkButton(master=tab1, text="Enviar", fg_color="#222222", corner_radius=8, border_width=3, border_color="#FFFF00", command=val)
    s.grid(row=6, column=2, padx=0, pady=0)
    c = CTkButton(master=tab1, text="Limpar", fg_color="#222222", corner_radius=8, border_width=3, border_color="#FFFF00", command=clear)
    c.grid(row=6, column=3, padx=0, pady=0)
def sw():
    def val():
        calc = int(t1.get())
        t1.configure(state="disable")
        hs =  calc*5
        oil = calc*1
        enzy = calc*1
        rj = calc*10
        space = CTkLabel(master=tab1, text="* Result *")
        space.grid(row=7, column=0 )
        hs = CTkLabel(master=tab1,font=("Arial", 20), text="Total HoneySucks = {}".format(hs), text_color="#FFFF00")
        hs.grid(row=8, column=0 )
        oil = CTkLabel(master=tab1,font=("Arial", 20), text="Total Oils = {}".format(oil), text_color="#FFFF00")
        oil.grid(row=9, column=0 )
        enzy = CTkLabel(master=tab1,font=("Arial", 20), text="Total Enzymes = {}".format(enzy), text_color="#FFFF00")
        enzy.grid(row=10, column=0 )
        rj = CTkLabel(master=tab1,font=("Arial", 20), text="Total Royal Jellies = {}".format(rj), text_color="#FFFF00")
        rj.grid(row=11, column=0 )

    def clear():
        t1.configure(state="normal")
        t1.delete(0, END)
    t1 = CTkEntry(master=tab1, height=(40), width=170,fg_color="#222222", corner_radius=8, border_width=3, border_color="#FFFF00", placeholder_text="Quantity (1, 10...)", placeholder_text_color="#999999",)
    t1.grid(row=6, column=0, padx=0, pady=0)
    s = CTkButton(master=tab1, text="Enviar", fg_color="#222222", corner_radius=8, border_width=3, border_color="#FFFF00", command=val)
    s.grid(row=6, column=2, padx=0, pady=0)
    c = CTkButton(master=tab1, text="Limpar", fg_color="#222222", corner_radius=8, border_width=3, border_color="#FFFF00", command=clear)
    c.grid(row=6, column=3, padx=0, pady=0)
def hw():
    def val():
        calc = int(t1.get())
        t1.configure(state="disable")
        sw =  calc*3
        bit = calc*33
        enzy = calc*3
        rj = calc*33
        space = CTkLabel(master=tab1, text="* Result *")
        space.grid(row=7, column=0 )
        sw = CTkLabel(master=tab1,font=("Arial", 20), text="Total SoftWaxes = {}".format(sw), text_color="#FFFF00")
        sw.grid(row=8, column=0 )
        bit = CTkLabel(master=tab1,font=("Arial", 20), text="Total BitterBerries = {}".format(bit), text_color="#FFFF00")
        bit.grid(row=9, column=0 )
        enzy = CTkLabel(master=tab1,font=("Arial", 20), text="Total Enzymes = {}".format(enzy), text_color="#FFFF00")
        enzy.grid(row=10, column=0 )
        rj = CTkLabel(master=tab1,font=("Arial", 20), text="Total Royal Jellies = {}".format(rj), text_color="#FFFF00")
        rj.grid(row=11, column=0 )

    def clear():
        t1.configure(state="normal")
        t1.delete(0, END)
    t1 = CTkEntry(master=tab1, height=(40), width=170,fg_color="#222222", corner_radius=8, border_width=3, border_color="#FFFF00", placeholder_text="Quantity (1, 10...)", placeholder_text_color="#999999",)
    t1.grid(row=6, column=0, padx=0, pady=0)
    s = CTkButton(master=tab1, text="Enviar", fg_color="#222222", corner_radius=8, border_width=3, border_color="#FFFF00", command=val)
    s.grid(row=6, column=2, padx=0, pady=0)
    c = CTkButton(master=tab1, text="Limpar", fg_color="#222222", corner_radius=8, border_width=3, border_color="#FFFF00", command=clear)
    c.grid(row=6, column=3, padx=0, pady=0)
def siw():
    def val():
        calc = int(t1.get())
        t1.configure(state="disable")
        hw =  calc*3
        sw = calc*9
        pp = calc*6
        rj = calc*3333
        space = CTkLabel(master=tab1, text="* Result *")
        space.grid(row=7, column=0 )
        hw = CTkLabel(master=tab1,font=("Arial", 20), text="Total Hard Waxes = {}".format(hw), text_color="#FFFF00")
        hw.grid(row=8, column=0 )
        sw = CTkLabel(master=tab1,font=("Arial", 20), text="Total Soft Waxes = {}".format(sw), text_color="#FFFF00")
        sw.grid(row=9, column=0 )
        pp = CTkLabel(master=tab1,font=("Arial", 20), text="Total Purple potions = {}".format(pp), text_color="#FFFF00")
        pp.grid(row=10, column=0 )
        rj = CTkLabel(master=tab1,font=("Arial", 20), text="Total Royal Jellies = {}".format(rj), text_color="#FFFF00")
        rj.grid(row=11, column=0 )

    def clear():
        t1.configure(state="normal")
        t1.delete(0, END)
    t1 = CTkEntry(master=tab1, height=(40), width=170,fg_color="#222222", corner_radius=8, border_width=3, border_color="#FFFF00", placeholder_text="Quantity (1, 10...)", placeholder_text_color="#999999",)
    t1.grid(row=6, column=0, padx=0, pady=0)
    s = CTkButton(master=tab1, text="Enviar", fg_color="#222222", corner_radius=8, border_width=3, border_color="#FFFF00", command=val)
    s.grid(row=6, column=2, padx=0, pady=0)
    c = CTkButton(master=tab1, text="Limpar", fg_color="#222222", corner_radius=8, border_width=3, border_color="#FFFF00", command=clear)
    c.grid(row=6, column=3, padx=0, pady=0)
def cw():
    def val():
        calc = int(t1.get())
        t1.configure(state="disable")
        hw =  calc*5
        neon = calc*25
        enzy = calc*1
        rj = calc*5252
        space = CTkLabel(master=tab1, text="* Result *")
        space.grid(row=7, column=0 )
        hw = CTkLabel(master=tab1,font=("Arial", 20), text="Total HardWaxes = {}".format(hw), text_color="#FFFF00")
        hw.grid(row=8, column=0 )
        neon = CTkLabel(master=tab1,font=("Arial", 20), text="Total NeonBerries = {}".format(neon), text_color="#FFFF00")
        neon.grid(row=9, column=0 )
        enzy = CTkLabel(master=tab1,font=("Arial", 20), text="Total Enzymes = {}".format(enzy), text_color="#FFFF00")
        enzy.grid(row=10, column=0 )
        rj = CTkLabel(master=tab1,font=("Arial", 20), text="Total Royal Jellies = {}".format(rj), text_color="#FFFF00")
        rj.grid(row=11, column=0 )

    def clear():
        t1.configure(state="normal")
        t1.delete(0, END)
    t1 = CTkEntry(master=tab1, height=(40), width=170,fg_color="#222222", corner_radius=8, border_width=3, border_color="#FFFF00", placeholder_text="Quantity (1, 10...)", placeholder_text_color="#999999",)
    t1.grid(row=6, column=0, padx=0, pady=0)
    s = CTkButton(master=tab1, text="Enviar", fg_color="#222222", corner_radius=8, border_width=3, border_color="#FFFF00", command=val)
    s.grid(row=6, column=2, padx=0, pady=0)
    c = CTkButton(master=tab1, text="Limpar", fg_color="#222222", corner_radius=8, border_width=3, border_color="#FFFF00", command=clear)
    c.grid(row=6, column=3, padx=0, pady=0)
def pp():
    def val():
        calc = int(t1.get())
        t1.configure(state="disable")
        neon =  calc*3
        rex = calc*3
        blux = calc*3
        glue = calc*3
        space = CTkLabel(master=tab1, text="* Result *")
        space.grid(row=7, column=0 )
        neon = CTkLabel(master=tab1,font=("Arial", 20), text="Total NeonBerries = {}".format(neon), text_color="#FFFF00")
        neon.grid(row=8, column=0 )
        rex = CTkLabel(master=tab1,font=("Arial", 20), text="Total RedExtracts = {}".format(rex), text_color="#FFFF00")
        rex.grid(row=9, column=0 )
        blux = CTkLabel(master=tab1,font=("Arial", 20), text="Total BlueExtracts = {}".format(blux), text_color="#FFFF00")
        blux.grid(row=10, column=0 )
        glue = CTkLabel(master=tab1,font=("Arial", 20), text="Total Glues = {}".format(glue), text_color="#FFFF00")
        glue.grid(row=11, column=0 )

    def clear():
        t1.configure(state="normal")
        t1.delete(0, END)
    t1 = CTkEntry(master=tab1, height=(40), width=170,fg_color="#222222", corner_radius=8, border_width=3, border_color="#FFFF00", placeholder_text="Quantity (1, 10...)", placeholder_text_color="#999999",)
    t1.grid(row=6, column=0, padx=0, pady=0)
    s = CTkButton(master=tab1, text="Enviar", fg_color="#222222", corner_radius=8, border_width=3, border_color="#FFFF00", command=val)
    s.grid(row=6, column=2, padx=0, pady=0)
    c = CTkButton(master=tab1, text="Limpar", fg_color="#222222", corner_radius=8, border_width=3, border_color="#FFFF00", command=clear)
    c.grid(row=6, column=3, padx=0, pady=0)
def ss():
    def val():
        calc = int(t1.get())
        t1.configure(state="disable")
        neon =  calc*3
        star = calc*3
        pp = calc*3
        tdk = calc*6
        space = CTkLabel(master=tab1, text="* Result *")
        space.grid(row=7, column=0 )
        neon = CTkLabel(master=tab1,font=("Arial", 20), text="Total NeonBerries = {}".format(neon), text_color="#FFFF00")
        neon.grid(row=8, column=0 )
        star = CTkLabel(master=tab1,font=("Arial", 20), text="Total Star Jellies = {}".format(star), text_color="#FFFF00")
        star.grid(row=9, column=0 )
        pp = CTkLabel(master=tab1,font=("Arial", 20), text="Total Purple Potion = {}".format(pp), text_color="#FFFF00")
        pp.grid(row=10, column=0 )
        tdk = CTkLabel(master=tab1,font=("Arial", 20), text="Total Tropical Drinks = {}".format(tdk), text_color="#FFFF00")
        tdk.grid(row=11, column=0 )

    def clear():
        t1.configure(state="normal")
        t1.delete(0, END)
    t1 = CTkEntry(master=tab1, height=(40), width=170,fg_color="#222222", corner_radius=8, border_width=3, border_color="#FFFF00", placeholder_text="Quantity (1, 10...)", placeholder_text_color="#999999",)
    t1.grid(row=6, column=0, padx=0, pady=0)
    s = CTkButton(master=tab1, text="Enviar", fg_color="#222222", corner_radius=8, border_width=3, border_color="#FFFF00", command=val)
    s.grid(row=6, column=2, padx=0, pady=0)
    c = CTkButton(master=tab1, text="Limpar", fg_color="#222222", corner_radius=8, border_width=3, border_color="#FFFF00", command=clear)
    c.grid(row=6, column=3, padx=0, pady=0)
def gd():
    def val():
        calc = int(t2.get())
        t2.configure(state="disable")
        straw =  calc*3
        blub = calc*3
        pine = calc*3

        space = CTkLabel(master=tab1, text="* Result *")
        space.grid(row=7, column=0 )

        straw = CTkLabel(master=tab1,font=("Arial", 20), text="Total StrawBerries = {}".format(straw), text_color="#FFFF00")
        straw.grid(row=8, column=0 )
        blub = CTkLabel(master=tab1,font=("Arial", 20), text="Total BlueBerries = {}".format(blub), text_color="#FFFF00")
        blub.grid(row=9, column=0 )
        pine = CTkLabel(master=tab1,font=("Arial", 20), text="Total PineApples = {}".format(pine), text_color="#FFFF00")
        pine.grid(row=10, column=0 )
    def clear():
        t2.configure(state="normal")
        t2.delete(0, END)
    t2 = CTkEntry(master=tab1, height=(40), width=170,fg_color="#222222", corner_radius=8, border_width=3, border_color="#FFFF00", placeholder_text="Quantity (1, 10...)", placeholder_text_color="#999999",)
    t2.grid(row=6, column=0, padx=0, pady=0)
    s = CTkButton(master=tab1, text="Enviar", fg_color="#222222", corner_radius=8, border_width=3, border_color="#FFFF00", command=val)
    s.grid(row=6, column=2, padx=0, pady=0)
    c = CTkButton(master=tab1, text="Limpar", fg_color="#222222", corner_radius=8, border_width=3, border_color="#FFFF00", command=clear)
    c.grid(row=6, column=3, padx=0, pady=0)

enzy =  CTkButton(master=tab1, text="Enzy", width=(150), height=(35), fg_color="#FFFF00", text_color="#000000", corner_radius=10, command=enzy, state="normal")
enzy.grid(row=0, column=0, padx=20, pady=10)

oil =  CTkButton(master=tab1, text="Oil", width=(150), height=(35), fg_color="#FFFF00", text_color="#000000", corner_radius=10, command=oil, state="normal")
oil.grid(row=0, column=2, padx=20, pady=10)

bex =  CTkButton(master=tab1, text="Blue Extracts", width=(150), height=(35), fg_color="#FFFF00", text_color="#000000", corner_radius=10, command=bex)
bex.grid(row=0, column=3, padx=20, pady=10)

rex =  CTkButton(master=tab1, text="Red Extracts", width=(150), height=(35), fg_color="#FFFF00", text_color="#000000", corner_radius=10, command=rex)
rex.grid(row=4, column=0, padx=20, pady=10)

tdk =  CTkButton(master=tab1, text="Tropical Drink", width=(150), height=(35), fg_color="#FFFF00", text_color="#000000", corner_radius=10, command=tdk)
tdk.grid(row=1, column=0, padx=20, pady=10)

glue =  CTkButton(master=tab1, text="Glue", width=(150), height=(35), fg_color="#FFFF00", text_color="#000000", corner_radius=10, command=glue)
glue.grid(row=1, column=2, padx=20, pady=10)

mc =  CTkButton(master=tab1, text="Moon Charm", width=(150), height=(35), fg_color="#FFFF00", text_color="#000000", corner_radius=10, command=mc)
mc.grid(row=1, column=3, padx=20, pady=10)

gli =  CTkButton(master=tab1, text="Glitter", width=(150), height=(35), fg_color="#FFFF00", text_color="#000000", corner_radius=10, command=gli)
gli.grid(row=4, column=2, padx=20, pady=10)

sw =  CTkButton(master=tab1, text="Soft Wax", width=(150), height=(35), fg_color="#FFFF00", text_color="#000000", corner_radius=10, command=sw)
sw.grid(row=2, column=0, padx=20, pady=10)

hw =  CTkButton(master=tab1, text="HardWax", width=(150), height=(35), fg_color="#FFFF00", text_color="#000000", corner_radius=10, command=hw)
hw.grid(row=2, column=2, padx=20, pady=10)

siw =  CTkButton(master=tab1, text="Swirled Wax", width=(150), height=(35), fg_color="#FFFF00", text_color="#000000", corner_radius=10, command=siw)
siw.grid(row=2, column=3, padx=20, pady=10)

cw =  CTkButton(master=tab1, text="Caustic Wax", width=(150), height=(35), fg_color="#FFFF00", text_color="#000000", corner_radius=10, command=cw)
cw.grid(row=4, column=3, padx=20, pady=10)

pp =  CTkButton(master=tab1, text="Purple Potion", width=(150), height=(35), fg_color="#FFFF00", text_color="#000000", corner_radius=10, command=pp)
pp.grid(row=3, column=0, padx=20, pady=10)

ss =  CTkButton(master=tab1, text="Super Smoothie", width=(150), height=(35), fg_color="#FFFF00", text_color="#000000", corner_radius=10, command=ss)
ss.grid(row=3, column=2, padx=20, pady=10)

gd =  CTkButton(master=tab1, text="GummyDrops", width=(150), height=(35), fg_color="#FFFF00", text_color="#000000", corner_radius=10, command=gd)
gd.grid(row=3, column=3, padx=20, pady=10)
# end
app.mainloop()