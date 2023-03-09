#!/bin/bash
runfile=$(expr runMD_H)	# Server where to run
dt=$(expr 2)            # Timestep in fs
Nruneq=$(expr 100)	# initiation timestep -2
Nrun1=$(expr 5000)	# dt*Nrun = 0.25 ns of data per run -3
Nrun2=$(expr 2000)	# dt*Nrun = 1ns of data per run -3
Nrun3=$(expr 5000)	# dt*Nrun = 2.5ns of data per run -4
Temp=$(expr 298.15)		# Temperature in K
Press=$(expr 5)			# Pressure in atm

N_wat=$(expr 1000)		# Number of water molecules
N_salt=$(expr 9)		# Number of KCl's per 1m solution


for folder in running
do
	mkdir $folder
	cd $folder

	for m in 4 #3 2 1
	do
		mkdir m_$m
		cd m_$m

		for i in 1 #2 3 4
		do
			mkdir $i
			cd $i

			# Coppying all needed files to run folder (alphabetical order)
			cp ../../../input/$runfile runMD
			cp ../../../input/simulation.in .
			cp ../../../input/copy_files.sh .
			cp ../../../input/forcefield.data .


			# Set simulation_preprocessing.in file values
			randomNumber=$(shuf -i 1-100 -n1)
			sed -i 's/R_VALUE/'$randomNumber'/' simulation.in
			sed -i 's/T_VALUE/'$Temp'/' simulation.in
			sed -i 's/P_VALUE/'$Press'/' simulation.in
			sed -i 's/dt_VALUE/'$dt'/' simulation.in
			sed -i 's/Nrun_eq_VALUE/'$Nruneq'/' simulation.in
			sed -i 's/Nrun1_VALUE/'$Nrun1'/' simulation.in
			sed -i 's/Nrun2_VALUE/'$Nrun2'/' simulation.in
			sed -i 's/Nrun3_VALUE/'$Nrun3'/' simulation.in
			sed -i 's/Nrun4_VALUE/'$Nrun4'/' simulation.in

			# Set filder location
			sed -i 's/run_FOLDER/'$i'/' copy_files.sh

			# Set runMD variables
			sed -i 's/JOB_NAME/KCl T is '${Temp%.*}' m is '$m' run '$i'/' runMD
			sed -i 's/INPUT/simulation.in/' runMD

			# Creating config folder
			mkdir config
			cd config
			cp ../../../../input/K.xyz .
			cp ../../../../input/params.ff .
			cp ../../../../input/Cl.xyz .
			cp ../../../../input/water.xyz .

			# compute total number of Li and SO4
			N=$(($m*$N_salt))

			# Create initial configuration using fftool and packmol
			~/software/lammps/la*18/fftool/fftool $N_wat water.xyz $N K.xyz $N Cl.xyz -r 55 > /dev/null
			~/software/lammps/la*18/packmol*/packmol < pack.inp > packmol.out
			~/software/lammps/la*18/fftool/fftool $N_wat water.xyz $N K.xyz $N Cl.xyz -r 55 -l > /dev/null

			# removing the force data from packmol as I use my own forcefield.data. copy data.lmp remove rest
			sed -i '12,27d' ./data.lmp
			cp data.lmp ../data.lmp
			cd ..
			rm -r config

			# Commiting run and reporting that
			sbatch runMD
			echo "Runtask commited: T="$Temp", m="$m", run " $i"."
			cd ..
		done
		cd ..
	done
	cd ..
done
cd ..
