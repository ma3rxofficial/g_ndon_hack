# VARIABLES

hacker_xterm_theme = 'xterm -cr green -bg black -fg white -hold -e' # THEME FOR XTERM
logo = """
        GONDON HACK GONDON HACK GONDON HACK GONDON HACK
        ***********************************************
                        THE 'BEST' HACK
                        
                                                    kvant
                                                    is
                                                        g
                                                        a
                                                        й"""

# [NUMBER OF FUNC.] FUNC NAME. HELP INFO
funcs_menu = """
[1.] Mail Hack. Mail hacking! Official mail.ru, gmail.com support.
[2.] Token Capture. Capturing club by token(Kv4nT's idea)

[0] Exit. Exiting from script.
[-1] Notifications. Modify auto-notify system.
"""

# FUNCS

def lts(s):
    # initialize an empty string
    str1 = ", "

    return (str1.join(s))

def exiting():
    print('Boy Next Door. Goodbye!')

def func_parse(func):
    if func == '1':
        import MailHack
        MailHack.start_mail_hack()

    elif func == '2':
        import Token_Capture_Club
        Token_Capture_Club.start_token()

    elif func == '0':
        exit()

    #elif fucn == '-1':




