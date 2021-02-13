#!/home/kali/Desktop python

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet zaafiyet analizi")
print("""
zaafiyet analizi aracina hos geldiniz.

""")

hedefip = raw_input("hedef ip giriniz: ")
os.system("nikto -h +hedefip")

