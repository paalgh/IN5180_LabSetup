import pyvisa
import time

rm = pyvisa.ResourceManager()
rm.list_resources_info()

def exisiting_tool(lab_num,tool,soccet_num):
    fung = rm.open_resource("TCPIP::nano-slab-"+str(lab_num)+"-"+tool+".uio.no::"+str(soccet_num)+"::SOCKET")
    fung.read_termination = '\n'
    if(tool == "gpp"):
        pass 
    else:
        fung.write_termination = '\n'
    print(fung.query('*IDN?'))
    return fung
	
	
print("Tool check:")
mdo = exisiting_tool(6,"mdo",3000) #oscilloscope

mdo.write('AWG1:offset 2.0')
print(mdo.query('AWG1:offset?'))
#print(type(mdo.query('FRA:RUN?')))
time.sleep(2)

mdo.write('FRA:RUN')
time.sleep(2)
#print(mdo.query('FRA:RUN?'))
while(mdo.query('FRA:RUN?')=="RUN"):
    pass
    
print(mdo.query('AWG1:offset?'))


mdo.write('FRA:STOP')
