from termcolor import colored 
from art import * 
import socket 



tprint("Mr. M3ARS", font="big") 
tprint("Porty v1", font="doom") 


host = input(colored("Taranacak Host Adresini Giriniz: ", 'yellow')) 
start_port = int(input(colored("Taranacak Port Aralığının Başlangıç Numarasını Giriniz: ", 'yellow'))) 
end_port = int(input(colored("Taranacak Port Aralığının Bitiş Numarasını Giriniz: ", 'yellow'))) 




def scan_ports(host, start, end): 
    open_ports = [] 
    for port in range(start, end + 1): 
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        sock.settimeout(0.2) 
        result = sock.connect_ex((host, port)) 
        if result == 0:  
            service = socket.getservbyport(port) 
            print(colored(f'{port} Numaralı Port Açık ve {service} Servisi Çalışıyor', 'green')) 
            open_ports.append(port) 
    if not open_ports:
        print(colored("Açık Port bulunamadı", 'red')) 




scan_ports(host, start_port, end_port) 