import os
from sys import intern


print(" /$$$$$$$$ /$$       /$$                ")
print("| $$_____/| $$      | $$                ")
print("| $$      | $$$$$$$ | $$   /$$  /$$$$$$$")
print("| $$$$$   | $$__  $$| $$  /$$/ /$$_____/")
print("| $$__/   | $$  \ $$| $$$$$$/ |  $$$$$$ ")
print("| $$      | $$  | $$| $$_  $$  \____  $$")
print("| $$$$$$$$| $$  | $$| $$ \  $$ /$$$$$$$/")
print("|________/|__/  |__/|__/  \__/|_______/ ")

print("Welcome to Ehks <Ethical Hacks , Penetration tests> , Made by Ebrahim Ahmed ")
print("****************************************************************************")
print("WARNING : Dont use this tool to hack anyone without their premission , Im not responsible for anything happens to you , Use it in the people you have premission on ")
print("Choose your option , 1 for downloading and installing missing files to use option E hacks , 2 for choosing E hacking tools")
print("Your option : ")
k = int(input())
if k == 1:
  print("Downloading the file required to use option 2")
  os.system("sudo apt update && sudo apt install nmap -y && sudo apt install wireshark -y && sudo apt install ettercap-text-only -y")
if k == 2:
  print("Choose from 1 Nmap <network mapper> , 2 setoolkit for <social engineering attacks> , 3 wireshark and ettercap for <sniffing attacks> ")
  x = int(input())
  if x == 1:
    print("launching nmap !")
    print("choose 1 nmap tcp scan , 2 nmap stealthy scan , 3 nmap full scan ")
    c = int(input())
    if c == 1:
      print("launching tcp attack !")
      print("enter your target ip address:")
      victim = input()
      os.system(f"sudo nmap -sT {victim}")
    if c == 2:
      print("launching nmap sleathy scan !")
      print("enter your target ip address:")
      victim = input()
      os.system(f"sudo nmap -sS {victim}")  
    if c == 3:
      print("launching nmap full scan")
      print("enter your target ip address:")
      victim == input()
      os.system(f"sudo nmap -A {victim}") 
  if x == 2:
    print("launching setoolkit !")
    os.system("sudo setoolkit")
  if x == 3:
    print("launching ettercap and wireshark !")
    print("enter your listener ip address <your pc address , to get it write in the terminal : <hostname -I > :")
    my_ip = input()
    print("enter target ip address:")
    target = input()
    print("enter your internet type , wireless: wlan0 , wired: eth0")
    internet = input()
    os.system(f"sudo ettercap -T -S -i {internet} -M arp:remote /{my_ip}// /{target}//")
    os.system("sudo wireshark")
print("Done doing your request ! ")
 

