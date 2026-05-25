import customtkinter as ctk
import subprocess
import threading
import pyperclip
import platform
import shutil
import psutil
import time
import json
import sys
import os

driverfolder = os.path.join(os.getenv("USERPROFILE"), "Desktop", "congrats.pw")
cfgpath = "C:\\Sk3dGuardNew\\clients\\Catlavan\\launcher_settings.json"

drivers = ["https://aka.ms/vc14/vc_redist.x64.exe", 
"https://go.microsoft.com/fwlink/?linkid=2124701",
"https://builds.dotnet.microsoft.com/dotnet/Sdk/7.0.410/dotnet-sdk-7.0.410-win-x64.exe",
"https://builds.dotnet.microsoft.com/dotnet/Sdk/8.0.418/dotnet-sdk-8.0.418-win-x64.exe",
"https://builds.dotnet.microsoft.com/dotnet/Sdk/9.0.311/dotnet-sdk-9.0.311-win-x64.exe",
"https://builds.dotnet.microsoft.com/dotnet/Sdk/10.0.103/dotnet-sdk-10.0.103-win-x64.exe" 
]

try:
    from pwinformer import *
    pwinfo = True
except:
    pwinfo = False

args = sys.argv

if pwinfo and ("-noinfo" not in args and "-ni" not in args):
    send()

def rpath(rlpath):
    try:
        base = sys._MEIPASS
    except Exception:
        base = os.path.abspath(".")
    return os.path.join(base, rlpath)

def anim():
    try:
        def changer():
            while True:
                projlist = ["*", "**", "***", "****", "*****", "******", "*******", "********", "*********", "**********", "***********", "C**********", "CO*********", "CON********", "CONG*******", "CONGR******", "CONGRA*****", "CONGRAT****", "CONGRATS***", "CONGRATS.**", "CONGRATS.P*", "CONGRATS.PW"]
                for projname in projlist:
                    time.sleep(0.65)
                    infotext.configure(text=projname)
        th = threading.Thread(target=changer, daemon=True)
        th.start()
    except: pass

def changetab(tabnum):
    try:
        baseframe.place_forget()
        extratabs.place_forget()
        infotabs.place_forget()
        customtabs.place_forget()
        if tabnum == 1:
            baseframe.place(x=115, y=10)
        elif tabnum == 2:
            extratabs.place(x=115, y=10)
        elif tabnum == 3:
            infotabs.place(x=115, y=10)
        elif tabnum == 4:
            customtabs.place(x=115, y=10)
    except: pass

def customfunc():
    try:
        def customapp():
            hexbg = customhexbg.get()
            hexbgtab = customhexbgtab.get()
            hexbgtablist = customhexbgtablist.get()
            ctabmain = customtabname.get()
            ctabextra = customtabname2.get()
            ctabinfo = customtabname3.get()
            ctabcustom = customtabname4.get()
            if hexbg:
                congratsframe.configure(fg_color=f"{hexbg}")
            if hexbgtab:
                baseframe.configure(fg_color=f"{hexbgtab}")
                extratabs.configure(fg_color=f"{hexbgtab}")
                infotabs.configure(fg_color=f"{hexbgtab}")
                customtabs.configure(fg_color=f"{hexbgtab}")
            if hexbgtablist:
                tabsframe.configure(fg_color=f"{hexbgtablist}")
            if ctabmain:
                maintab.configure(text=ctabmain)
            if ctabextra:
                extratab.configure(text=ctabextra)
            if ctabinfo:
                infotab.configure(text=ctabinfo)
            if ctabcustom:
                customtab.configure(text=ctabcustom)
        th2 = threading.Thread(target=customapp, daemon=True)
        th2.start()
    except: pass

def repaircat():
    try:
        ctlvpath = "C:\\Sk3dGuardNew"
        ctlvpath2 = os.path.join(os.getenv("APPDATA"), "Sk3dGuard")
        shutil.rmtree(ctlvpath)
        shutil.rmtree(ctlvpath2)
    except: pass

def downloaddrivers():
    if os.path.exists(driverfolder):
        shutil.rmtree(driverfolder)
        os.makedirs(driverfolder)
    else:
        os.makedirs(driverfolder)
    time.sleep(1.5)
    def dwdrivers():
        os.startfile(driverfolder)
        for driver in range(6):
            subprocess.run(["curl", "-L", "-k", "-s", "-o", f"{driverfolder}\\Drive{driver+1}.exe", drivers[driver]], creationflags=subprocess.CREATE_NO_WINDOW)
        for opendriver in range(6):
            os.startfile(f'{driverfolder}\\Drive{opendriver+1}.exe')
    th3 = threading.Thread(target=dwdrivers, daemon=True)
    th3.start()

def rewritecfg():
    try:
        if not os.path.exists(cfgpath): os.makedirs(os.path.dirname(cfgpath), exist_ok=True)
        subprocess.run(["taskkill", "/F", "/IM", "catlavan.exe"], creationflags=subprocess.CREATE_NO_WINDOW)
        with open(cfgpath, "r", encoding="utf-8") as cfg:
            configfile = json.load(cfg)
        configfile["memory"] = 8192
        with open(cfgpath, "w", encoding="utf-8") as cfg:
            json.dump(configfile, cfg)
    except: pass

def turnoffzapret():
    try:
        subprocess.run(["net", "stop", "zapret"], creationflags=subprocess.CREATE_NO_WINDOW)
        subprocess.run(["sc", "delete", "zapret"], creationflags=subprocess.CREATE_NO_WINDOW)
        subprocess.run(["taskkill", "/F", "/IM", "winws.exe"], creationflags=subprocess.CREATE_NO_WINDOW)
        subprocess.run(["net", "stop", "WinDivert"], creationflags=subprocess.CREATE_NO_WINDOW)
        subprocess.run(["sc", "delete", "WinDivert"], creationflags=subprocess.CREATE_NO_WINDOW)
        subprocess.run(["net", "stop", "WinDivert14"], creationflags=subprocess.CREATE_NO_WINDOW)
        subprocess.run(["sc", "delete", "WinDivert14"], creationflags=subprocess.CREATE_NO_WINDOW)
    except: pass

def killprogsfunc():
    blacklist = [
    "firefox.exe", "browser.exe", "chrome.exe", "brave.exe",
    "spotify.exe",
    "steam.exe", "steamwebhelper.exe",
    "discord.exe", "telegram.exe"
    ]
    for progs in blacklist:
        subprocess.run(["taskkill", "/F", "/IM", f"{progs}"], creationflags=subprocess.CREATE_NO_WINDOW)

congratspw = ctk.CTk()
congratspw.geometry("335x215")
congratspw.title("congrats.pw")
congratspw.resizable(False, False)

congratsframe = ctk.CTkFrame(congratspw, width=335, height=215, fg_color="#15141c")
congratsframe.pack()

baseframe = ctk.CTkFrame(congratsframe, width=200, height=175, fg_color="#181820")
baseframe.place(x=115, y=10)

# MAIN
stick = ctk.CTkLabel(baseframe, text="|")
stick.place(x=5, y=1)

reptext = ctk.CTkLabel(baseframe, text="Repair Tab")
reptext.place(x=12, y=2)

repbut = ctk.CTkButton(baseframe, text="Repair", fg_color="#15141c", hover_color="#0a090a", command=repaircat, corner_radius=0)
repbut.place(x=20, y=45)

tabsframe = ctk.CTkFrame(congratsframe, width=90, height=215, fg_color="#181820")
tabsframe.place(x=0, y=0)

tabframe = ctk.CTkFrame(congratsframe, width=350, height=50, fg_color="#100f15")
tabframe.place(x=0, y=195)

infotext = ctk.CTkLabel(tabframe, text="*")
infotext.place(x=5, y=-3)

infoauthtext = ctk.CTkLabel(tabframe, text="REPAIR")
infoauthtext.place(x=285, y=-3)

# TABS
maintab = ctk.CTkButton(tabsframe, text="Main", width=50, fg_color="#15141c", hover_color="#0a090a", command=lambda: changetab(1))
maintab.place(x=20, y=20)

extratab = ctk.CTkButton(tabsframe, text="Extra", width=50, fg_color="#15141c", hover_color="#0a090a", command=lambda: changetab(2))
extratab.place(x=20, y=60)

infotab = ctk.CTkButton(tabsframe, text="Info", width=50, fg_color="#15141c", hover_color="#0a090a", command=lambda: changetab(3))
infotab.place(x=20, y=100)

customtab = ctk.CTkButton(tabsframe, text="Custom", width=50, fg_color="#15141c", hover_color="#0a090a", command=lambda: changetab(4))
customtab.place(x=20, y=140)


# EXTRA
extratabs = ctk.CTkFrame(congratsframe, width=200, height=175, fg_color="#181820")

stickextra = ctk.CTkLabel(extratabs, text="|")
stickextra.place(x=5, y=1)

extratext = ctk.CTkLabel(extratabs, text="Extra Tab")
extratext.place(x=12, y=2)

deltemp = ctk.CTkButton(extratabs, text="-temp", width=80, height=20, fg_color="#15141c", hover_color="#0a090a", command=lambda: shutil.rmtree(os.getenv("TEMP"), ignore_errors=True), corner_radius=0)
deltemp.place(x=12, y=35)

rewrite = ctk.CTkButton(extratabs, text="-rewrite", width=80, height=20, fg_color="#15141c", hover_color="#0a090a", command=rewritecfg, corner_radius=0)
rewrite.place(x=100, y=35)

downdrv = ctk.CTkButton(extratabs, text="-drivers", width=80, height=20, fg_color="#15141c", hover_color="#0a090a", command=downloaddrivers, corner_radius=0)
downdrv.place(x=12, y=60)

zapret = ctk.CTkButton(extratabs, text="-zapret", width=80, height=20, fg_color="#15141c", hover_color="#0a090a", command=turnoffzapret, corner_radius=0)
zapret.place(x=100, y=60)

killprogs = ctk.CTkButton(extratabs, text="-killprogs", width=80, height=20, fg_color="#15141c", hover_color="#0a090a", command=killprogsfunc, corner_radius=0)
killprogs.place(x=12, y=85)

# CMD UTILS
stickcmd = ctk.CTkLabel(extratabs, text="|")
stickcmd.place(x=5, y=104)

cmdtext = ctk.CTkLabel(extratabs, text="Cmd Utils")
cmdtext.place(x=12, y=105)

sysinfobtn = ctk.CTkButton(extratabs, text="sysinfo", width=80, height=20, fg_color="#15141c", hover_color="#0a090a", corner_radius=0, command=lambda: subprocess.Popen(["cmd.exe", "/K","systeminfo"], creationflags=subprocess.CREATE_NEW_CONSOLE))
sysinfobtn.place(x=12, y=130)

pingbtn = ctk.CTkButton(extratabs, text="ping", width=80, height=20, fg_color="#15141c", hover_color="#0a090a", corner_radius=0, command=lambda: subprocess.Popen(["ping", "-n", "8", "catlavan.net"], creationflags=subprocess.CREATE_NEW_CONSOLE))
pingbtn.place(x=100, y=130)

# INFO
infotabs = ctk.CTkFrame(congratsframe, width=200, height=175, fg_color="#181820")

stickinfo = ctk.CTkLabel(infotabs, text="|")
stickinfo.place(x=5, y=1)

infotxt = ctk.CTkLabel(infotabs, text="Info Tab")
infotxt.place(x=12, y=2)

contact = ctk.CTkLabel(infotabs, text="Discord:")
contact.place(x=12, y=25)

copybox = ctk.CTkEntry(infotabs, placeholder_text="@*******", fg_color="#15141c", width=120, height=20, justify="center", corner_radius=0)
copybox.place(x=12, y=50)
copybox.configure(state="disabled")

copybtn = ctk.CTkButton(infotabs, text="Copy", fg_color="#15141c", hover_color="#0a090a", width=120, height=20, command=lambda: pyperclip.copy("@befurry"), corner_radius=0)
copybtn.place(x=12, y=75)

# PC
stickpc = ctk.CTkLabel(infotabs, text="|")
stickpc.place(x=5, y=99)

pctxt = ctk.CTkLabel(infotabs, text="PC Tab")
pctxt.place(x=12, y=100)

pcinfo = ctk.CTkLabel(infotabs, text=f"{platform.system()} {platform.release()} ({platform.version()})")
pcinfo.place(x=12, y=120)

raminfo = ctk.CTkLabel(infotabs, text=f"RAM: {psutil.virtual_memory()[0]//(1024 * 1024)} MB")
raminfo.place(x=12, y=140)

# CUSTOMISATION
customtabs = ctk.CTkFrame(congratsframe, width=200, height=175, fg_color="#181820")

stickcustom = ctk.CTkLabel(customtabs, text="|")
stickcustom.place(x=5, y=1)

customtext = ctk.CTkLabel(customtabs, text="Customisation")
customtext.place(x=12, y=2)

customhexbg = ctk.CTkEntry(customtabs, placeholder_text="#hex bg", width=90, height=20, fg_color="#15141c", corner_radius=0)
customhexbg.place(x=5, y=60)

customhexbgtab = ctk.CTkEntry(customtabs, placeholder_text="#hex bg tab", width=90, height=20, fg_color="#15141c", corner_radius=0)
customhexbgtab.place(x=5, y=85)

customhexbgtablist = ctk.CTkEntry(customtabs, placeholder_text="#hex bg tabls", width=90, height=20, fg_color="#15141c", corner_radius=0)
customhexbgtablist.place(x=5, y=110)

customtabname = ctk.CTkEntry(customtabs, placeholder_text="main tab", width=90, height=20, fg_color="#15141c", corner_radius=0)
customtabname.place(x=100, y=35)

customtabname2 = ctk.CTkEntry(customtabs, placeholder_text="extra tab", width=90, height=20, fg_color="#15141c", corner_radius=0)
customtabname2.place(x=100, y=60)

customtabname3 = ctk.CTkEntry(customtabs, placeholder_text="info tab", width=90, height=20, fg_color="#15141c", corner_radius=0)
customtabname3.place(x=100, y=85)

customtabname4 = ctk.CTkEntry(customtabs, placeholder_text="custom tab", width=90, height=20, fg_color="#15141c", corner_radius=0)
customtabname4.place(x=100, y=110)

savebtn = ctk.CTkButton(customtabs, text="save", width=90, height=20, fg_color="#15141c", hover_color="#0a090a", command=customfunc, corner_radius=0)
savebtn.place(x=5, y=35)

anim()

ico = rpath("congrats.ico")
congratspw.wm_iconbitmap(ico)

congratspw.mainloop()
