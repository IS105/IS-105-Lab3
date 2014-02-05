import sys
import os
import subprocess
import re

def min_sys_info():
    """
    ----- Studenter: -----
----- mysysinfo() -----

	Her er mitt resultat av kjøringen av denne funksjonen:
   
	
byteorder: little
os data: 
('Linux', 'root', '2.6.32-431.3.1.el6.x86_64', '#1 SMP Fri Jan 3 21:39:27 UTC 2014', 'x86_64')
os bruker: Criyonit
----- initialer() -----
2
----- infix_to_prefix() -----
2
----- lab3_scripts() -----
    """
    print "byteorder: " + sys.byteorder
    print "os data: "
    print os.uname()
    print "os bruker: " + os.getlogin()
