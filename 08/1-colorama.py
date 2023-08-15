from colorama import Fore , Style , Back
# back --> rang background hast
# style --> no font hast  BRIGHT , NORMAL , DIM
# Fore --> rang font hast

print(Fore.GREEN,"som has green")
print(Fore.RESET,end="")
print("soltani")
print(Back.CYAN,"python is cyan")
print(Back.RESET)  # reset bargasht be tabnzimat peshfarz hast
print()
print(Style.BRIGHT,"qoli dar BRIGHT")
print(Style.NORMAL,"qoli dar NORMAL")
print(Style.DIM,"qoli dar DIM")

print(Fore.RESET)
print(Back.RESET)
print(Style.RESET_ALL) # --> barbash hamechiz be pishfarz 
