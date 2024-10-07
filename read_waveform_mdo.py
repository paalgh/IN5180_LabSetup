#Setting a square wave at the function generator (mfg)
#Read the output with the oscilloscope (mdo)

#This script is not functional, do not use !!!!!!!!!!!!!!!!!!

import pyvisa
import argparse
import time 

#Function for checking if tool is available
def exisiting_tool(lab_num,tool,soccet_num):
    fung = rm.open_resource("TCPIP::nano-slab-"+str(lab_num)+"-"+tool+".uio.no::"+str(soccet_num)+"::SOCKET")
    fung.read_termination = '\n'
    if(tool == "gpp"):
        pass 
    else:
        fung.write_termination = '\n'
    print(fung.query('*IDN?'))
    return fung
    

if (__name__ == "__main__"):
    parser = argparse.ArgumentParser(
        description="Setting a DC voltage with the power supply (gpp) and reading it with the digital multimeter(gdm)"
    )
    parser.add_argument("--slab_num", required=True, type=int, help="Lab space number between 1 and 6")
    parser.add_argument("--mfg_output_port", required=True, type=int, help="Which of the MFG channels is used, 1 or 2")
    parser.add_argument("--mdo_input_port", required=True, type=int, help="Osillosccope input channel")
    parser.add_argument("--waveform_type", required=True, type=str, help="MFG output waveform")
    parser.add_argument("--frequency", required=True, type=float, help="MFG output frequency")
    parser.add_argument("--amplitude", required=True, type=float, help="MFG output amplitude")
    parser.add_argument("--offset", required=True, type=float, help="MFG output DC offset")
    parser.add_argument("--data_file_name", required=True, type=str, help="Filename where output will be stored")
    
    args = parser.parse_args()
    
    #Date output file handeling
    f = open(args.data_file_name, "w")
    
    
    #Invoking the resources
    rm = pyvisa.ResourceManager()
    rm.list_resources()
	
    #Checking tool availability
    osc = exisiting_tool(args.slab_num,"mdo",3000)
    mfg = exisiting_tool(args.slab_num,"mfg",1026)
    
    #Set the decired waveform:
    mfg.write("source"+str(args.mfg_output_port)+":apply:"+args.waveform_type+" "+str(args.frequency)+","+str(args.amplitude)+","+str(args.offset))
    
    #Set acquisition mode:
    osc.write(":acquire:mode sample")
    print(osc.query(":acquire:mode?"))
    osc.write(":acquire:recordlength 1e+4")
    
    #Read the stored waveform once it is ready
    while(osc.query(":ACQuire"+str(args.mdo_input_port)+":STATe?")==0):
        pass
    header=osc.query(":ACQuire"+str(args.mdo_input_port)+":MEMory?")
    print(type(header))
    
    osc.write(':header OFF')
    
    data = osc.query(":ACQuire"+str(args.mdo_input_port)+":MEMory?")
    print(data)
    #Writing data to file and closing
    f.write(data)
    f.close()
    
    file = "Disk:/ImageTest.PNG"
    time.sleep(1)
    '''
    #Saving an image to file
    osc.write("SAVe:IMAGe:FILEFormat PNG") #Choose file format
    osc.write("SAVe:IMAGe:INKSaver OFF") #Invert background
    osc.write("SAVe:IMAGe "+file)

    osc.write("SAVe:IMAGe USB:/test1.png")
    
    '''
    #Save waveform data as picture
    sampling_time=2 #Sampling time in seconds
    osc.write(":DATALOG:STATE ON")
    osc.write(":DATALOG:SOURce CH"+str(args.mdo_input_port))
    osc.write(":DATALOG:DUR "+str(sampling_time))
    osc.write(":DATALOG:SAVE image")
    osc.write(":DATALOG:STATE OFF")
    
    
