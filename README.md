# ConfEntropyTutorial
Tutorial on how to calculate molecular entropy and perform Boltzmann averaging

0) Download folder ```programs``` with all the scripts onto your Linux computer.
1) Generate Cartesian coordinates of any random conformer of a system (e.g. m1_00_PEt2Ph.xyz in folder Step_1) and optimize your random conformer, e.g. with ORCA:

a) preprare an input file: ```python3 /path/to/programs/dft_opt-orca_CONF.py m1_00_PEt2Ph.xyz PBE0-D3 TZ``` (feel free to adjust dft_opt-orca_CONF.py to meet your needs)

b) run ORCA: ```/path/to/ORCA/orca m1_00_PEt2Ph-PBE0-D3-TZ.inp > m1_00_PEt2Ph-PBE0-D3-TZ.out```

c) extract CHELPG charges from output: ```python3 /path/to/programs/get_CHR_ORCA.py m1_00_PEt2Ph-PBE0-D3-TZ.out ```. You should obtain file ```m1_00_PEt2Ph-PBE0-D3-TZ.CHR``` that contains your charges and Cartesian coordinates.

d) Prepare the file that lists rotatble bonds and angle incremenets for rotation, see ```m1_00_PEt2Ph-PBE0-D3-TZ.ROT```. I choose the following settings for rotation:
```
1 2 60 300 5
1 20  60 300 5
1 9 45 135 5
```
Bond 1 - 2 (P - C2H5) rotates by 60 degrees, maximum angle is 300 deg, for each thus generated structure rotatable bond is allowed to rotate by +/- 5 degrees to resolve possible clashes (see more here: https://github.com/QuantumChemistryGroup/uniconf-bin)
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
3) copy all *xyz files into subfloder in the other folder, e.g. ```Step_3/raw_data``` and opt+freq them with any method/code. Here I used xtb and GFN2 (options: ```--ohess extreme --cycles 5000 --acc 0.01 --iterations 5000```). ORCA/B97-3c or Priroda/QM3 are also good choices. After optimization remove all *xyz files.

4) For each opt+freq files extract E, thermodynamic corrections, and Cartesian coordinates:

For ORCA:

```python3 /path/to/programs/last_coord_orca_E.py m1_00_PEt2Ph-PBE0-D3-TZ-uniMM_34-XXX.out```

```python3 /path/to/programs/td_input_orca.py m1_00_PEt2Ph-PBE0-D3-TZ-uniMM_34-XXX.out float(scale)```

For Priroda: 

```python3 /path/to/programs/pr_xyz_E.py m1_00_PEt2Ph-PBE0-D3-TZ-uniMM_34-XXX.out```

```python3 /path/to/programs/td_input_priroda.py m1_00_PEt2Ph-PBE0-D3-TZ-uniMM_34-XXX.out float(scale) ```

For xtb:

```python3 /path/to/programs/last_coord_xtb_E.py m1_00_PEt2Ph-PBE0-D3-TZ-uniMM_34-XXX.out```

```python3 /path/to/programs/td_input_xtb.py m1_00_PEt2Ph-PBE0-D3-TZ-uniMM_34-XXX.out float(scale) ```

Here: float(scale) is the scaling coefficient for harmonic frequencies.

If imaginary frequencies were found, they can be either removed manually with an additional optimization step, or they can be converted into real ones with ```td_input_XXX.py``` scripts.

After the opt+freq procedure, remove the ```g98.out``` file.

Then, get rid off the duplicates running the following script in this folder:

```python3 /path/to/programs/rmsdp_min.py 12 0.1 10 5```

Check file ```rmsd_min.txt``` manually - there are listed couples of conformers for which rmsd difference below 0.5 Angstroem was obtained. If necessary, remove some duplicates manually.

Finally, copy all unique conformers to one folder above:

```python3 /path/to/programs/work_with_bash_cp.py ```

Then go up by one directory

```cd ..```

6) In folder Step_3 you have both *xyz and *dat files for all unique conformers.

7) Run the script in the folder:

   ```python /path/to/programs/ensemble.py T1 T2```, where T1, T2 - temperatures. By default, ensemble.py uses GR_25_4_1 model. Open the script and modify line ```td = ['GR_25_4_1']``` with your model of choice, HO, GR_100_4_1, etc. 

When I run the script:

```python3 ../programs/ensemble.py 298.15```, I obtained files ```SI_S.txt``` and ```SI_H.txt```

```SI_H.txt``` - contains enthalpic corrections for all temeratures and statistical thermodynamic models in the following format: Temperature, TD model, name_of_the_most_stable_conformer, Boltzman_weight_of_the_most_stable_conformer, number_of_conformers, Enthalpic_correcrtion_in_Hartree for the most stable conformer, Hcorr_av - Hcorr_1 : difference between the ensemble average enthalpic correction and that of the most stable conformer, total enthalpic correction (the summ of previous two)

```298.15    GR_25_4_1 m1_00_PEt2Ph-PBE0-D3-TZ-uniMM_54_-T_opt.xyz  0.21    21 0.23181 0.00068 0.23249```


```SI_S.txt``` - contains enthalpic corrections for all temeratures and statistical thermodynamic models in the following format: Temperature, TD model, name_of_the_most_stable_conformer, Boltzman_weight_of_the_most_stable_conformer, number_of_conformers, Entropy for the most stable conformer, S_av - S_1 : difference between the ensemble average entropy and that of the most stable conformer, conformational entropy, total entropy (the summ of previous three)

```298.15    GR_25_4_1 m1_00_PEt2Ph-PBE0-D3-TZ-uniMM_54_-T_opt.xyz  0.21    21 111.95   0.16   4.40 116.51```

```Hcorr_av - Hcorr_1``` is ```H(T)-H(0)``` in CREST
```S_av - S_1``` is ```δSrrho``` in CREST
```conformational entropy``` is ```Sconf``` in CREST

```m1_00_PEt2Ph-PBE0-D3-TZ-uniMM_54_-T_opt.xyz``` turned out to be the most stable conformer according to dG GFN2 and msRRHO(25) model. It can further be treated with DFT. Then, total entropy will be that of DFT freq calculation + (S_av - S_1) + conformational entropy, i.e. S(DFT) + 0.16 + 4.40 e.u. (cal (mol K)-1)

Total enthalpic correction will be: Hcorr(DFT) + 0.00068 (Hartree)

In case of any questions do not hesitate to contact us: Yury.Minenkov"at"gmail.com 
