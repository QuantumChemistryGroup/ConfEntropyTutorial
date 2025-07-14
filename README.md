# ConfEntropyTutorial
Tutorial on how to calculate molecular entropy and perform Boltzmann averaging

0) Download folder ```programs``` with all the scripts onto your Linux computer.
1) (Step_1) Generate Cartesian coordinates of any random conformer of a system (e.g. m1_00_PEt2Ph.xyz in Step_1) and optimize your random conformer, e.g. with ORCA:

a) preprare an input file: ```python3 /path/to/programs/dft_opt-orca_CONF.py m1_00_PEt2Ph.xyz PBE0-D3 TZ``` (feel free to adjust dft_opt-orca_CONF.py to feet your needs)

b) run ORCA: ```/path/to/ORCA/orca m1_00_PEt2Ph-PBE0-D3-TZ.inp > m1_00_PEt2Ph-PBE0-D3-TZ.out```

c) extract CHELPG charges from output: ```python3 /path/to/programs/get_CHR_ORCA.py m1_00_PEt2Ph-PBE0-D3-TZ.out ```. You should obtain file ```m1_00_PEt2Ph-PBE0-D3-TZ.CHR``` that contains your cherges.

d) Prepare the file that lists rotatble bonds and angle incremenets for rotation, see ```m1_00_PEt2Ph-PBE0-D3-TZ.ROT```. I choose the following settings for rotation:
```
1 2 60 300 5
1 20  60 300 5
1 9 45 135 5
```
Bond 1 - 2 (P - C2H5) rotates by 60 degrees, maximum angle is 300 deg, for each thus generated structure rotatble bond allows to rotate by +/- 5 degrees to resolve possible clashes (see more here: https://github.com/QuantumChemistryGroup/uniconf-bin)
Bond 1 - 20 (P - C2H5): identical to 1 - 2 settings
Bond 1 - 9 (P-C6H5): rotates by 45 degrees, maxium angle is 135 deg.

e) Generate the Uniconf input file: ```python3 /path/to/programs/input_uniconf-ALKENE.py m1_00_PEt2Ph-PBE0-D3-TZ.CHR```

f) run Uniconf on generated file ```m1_00_PEt2Ph-PBE0-D3-TZ-uni.inp```:

```path/to/programs/uniconf m1_00_PEt2Ph-PBE0-D3-TZ-uni.inp > m1_00_PEt2Ph-PBE0-D3-TZ-uni.out```

2) Copy the obtained file ```m1_00_PEt2Ph-PBE0-D3-TZ-uniMM.xyz``` to other folder (e.g. to Step_2), split it, and then remove m1_00_PEt2Ph-PBE0-D3-TZ-uniMM.xyz:
```
python3 /path/to/programs/split_xyz_E.py m1_00_PEt2Ph-PBE0-D3-TZ-uniMM.xyz
rm m1_00_PEt2Ph-PBE0-D3-TZ-uniMM.xyz
```
3) copy all *xyz files into subfloder into the other folder, e.g. ```Step_3/raw_data``` and opt+freq them with any method/code

4)  
