# IN5180_LabSetup
Barebone scripts used to communicate with the lab tools. The functional tests are located in the functional_scripts folder and are:
- Init_test.py : Checking that all tools are online
- tool_check.py : Checking if a single tool is online
- set_voltage_DC.py : setting a DC voltage at both power supply (gpp) outputs and reading the resulting voltage at the multimeter (gdm)
- voltage_sweep_DC.py : Sweeping the gpp output and reading the result with the gdm.
- set_votlage_AC.py : setting a sine wave at the output of the function generator (mfg) and reading the amplitude and frequency with the oscilloscope (mdo)
- read_phase_AC : setting the same sine wave at both mfg otuputs and reading the frequency, amplitude and phase difference with the mdo.

Some scripts, still in development, are in the folder scripts_in_process.

All manuals for the different instruments are found in the Documents folder.

# Tutorial on running the scripts

This tutorial will help you get started with running python scripts on a virtual machine (VM) and give a description on how to run the scripts in this repository. 

## Getting ready on the virtual machine (Hello world tutorial)

1. If you are on your computer open the VMWare Horizon Client as you would for running Cadence. If you're on the lab computers open a browser (e.g. Edge), go to view.uio.no and log in with your UiO username and password. 
2. Open the *Lab Net Workstation*
3. Make a folder where you want to keep your code. Make the folder in your home directory (M:), eg. *\\uio\hume.uio.no\username*.
4. Open the command prompt (search *cmd* and it'll be the first thing to pop up) and navigate to your folder by writing cd /folder_name
5. Open the program Notepad++ (or any other text editor), make a new file (e.g. helloWorld.py) and copy in the code:
* print('Hello, world!')
6. Save the file in your folder
7. Run the program by typing: *python helloWorld.py* in the cmd and you should see the printed text appear.

## Running the scripts

The basic syntax for running a python script on the VM is: *python script_name.py*. In the scripts provided, there are arguments that the different scripts take in, such as desk number (1 - 6) and other relevant information. To find out what the script does and what the different arguments are you can run *python script_name.py -h*. You will get a description of the functionality, the syntax for running the script and a description of the different arguments. Let us look at one example, the tool_check.py script. The arguments needed are:
* slab_num (int)
* tool (str)
  
The slab_num is the desk number you are working at (1 closest to the offices) and tool is one of the four lab instruments:

* mdo = oscilloscope
* gpp = DC power supply
* gdm = multi-meter
* gfm = Function generator
The syntax for running the tool_check.py script for checking connectivity to the oscilloscope at desk 1 is:

*python tool_check.py --slab_num=1 --tool="mdg"*

The other scripts have more arguments but the syntax is the same. If you have any questions please feel free to contact Pål Gunnar by email (paalgh) or in office 5108.
