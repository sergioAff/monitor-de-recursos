import psutil
import time
import winsound

while True:
    porcentaje_cpu=psutil.cpu_percent(interval=0.5)
    memoria=psutil.virtual_memory().available/1073741824
    disco=psutil.disk_usage('C:').free/1073741824
    
    
    print(f'''-----------------------------\nCpu en uso: {porcentaje_cpu}%\nMemoria disponible: {round(memoria,2)} gb 
Espacio libre: {round(disco,2)} gb\n-----------------------------''')
    
    if porcentaje_cpu >=75:
        winsound.Beep(2500,50)
    
    time.sleep(0.5)
     