# IN5180_LabSetup
Barebone scripts are used to communicate with the lab tools and do different tests. The functional tests are located in the functional_scripts folder and are:
- Init_test.py : Checking that all tools are online
- tool_check.py : Checking if a single tool is online
- set_voltage_DC.py : setting a DC voltage at both power supply (gpp) outputs and reading the resulting voltage at the multimeter (gdm)
- voltage_sweep_DC.py : Sweeping the gpp output and reading the result with the gdm.
- set_votlage_AC.py : setting a sine wave at the output of the function generator (mfg) and reading the amplitude and frequency with the oscilloscope (mdo)
- read_phase_AC : setting the same sine wave at both mfg otuputs and reading the frequency, amplitude and phase difference with the mdo.

Some scripts still in development are in the folder scripts_in_process.

All documents for the different instruments are found in the Documents folder
