from tkinter import *

raam = Tk()
raam.title("Malelaud")
tahvel = Canvas(raam, width=1000, height=600, background="lightgray")

# Parameetrid
RUUDU_LAIUS = 70
RUUDU_KÕRGUS = 62.5
MALELAUA_ALGU_X = 220
MALELAUA_ALGU_Y = 50

# --- 1. JOONISTAME MALELAUA RUUDUD (TAUST) ---
tahvel.create_rectangle(MALELAUA_ALGU_X, MALELAUA_ALGU_Y, 
                        MALELAUA_ALGU_X + 8 * RUUDU_LAIUS, MALELAUA_ALGU_Y + 8 * RUUDU_KÕRGUS, 
                        outline="Brown", width=3)

for rida in range(8):
    for veerg in range(8):
        if (rida + veerg) % 2 == 0:
            varv = "white"
        else:
            varv = "black"
        
        x1 = MALELAUA_ALGU_X + veerg * RUUDU_LAIUS
        y1 = MALELAUA_ALGU_Y + rida * RUUDU_KÕRGUS
        x2 = x1 + RUUDU_LAIUS
        y2 = y1 + RUUDU_KÕRGUS
        
        tahvel.create_rectangle(x1, y1, x2, y2, fill=varv, outline=varv)

# --- 2. JOONISTAME NUPUD (TERVENISTI KAETUD READ) ---

for rida in range(8):
    for veerg in range(8):
        
        nupu_varv = None

        # --- REEGILD ---
        # Me EI kontrolli enam (rida + veerg) % 2, sest sa tahad,
        # et terve rida oleks nuppe täis.

        if rida < 2:          
            # Read 1 ja 2 (indeksid 0 ja 1) -> VALGED
            nupu_varv = "white"
            
        elif rida > 5:        
            # Read 7 ja 8 (indeksid 6 ja 7) -> MUSTAD
            nupu_varv = "black"

        # (Read 3, 4, 5, 6 jäävad vahele, sest nupu_varv jääb None-iks)

        # --- JOONISTAMINE ---
        if nupu_varv is not None:
            x1 = MALELAUA_ALGU_X + veerg * RUUDU_LAIUS
            y1 = MALELAUA_ALGU_Y + rida * RUUDU_KÕRGUS
            x2 = x1 + RUUDU_LAIUS
            y2 = y1 + RUUDU_KÕRGUS
            
            padding = 10
            tahvel.create_oval(x1 + padding, y1 + padding, 
                               x2 - padding, y2 - padding, 
                               fill=nupu_varv, outline=nupu_varv)

tahvel.pack()
raam.mainloop()