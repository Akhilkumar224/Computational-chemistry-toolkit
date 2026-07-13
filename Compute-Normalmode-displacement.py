#For any quries Contact: kumarakhil224@gmail.com
#TO RUN THIS PROGRAM YOU NEED A GAUSSIAN LOG FILE CONTAING FREQUENCIES AND NORMAL MODE COORDINATES
#Note that enter the atom number in ascending order

import math
file_name= input("Enter the file name\n")
target_freq=float(input("Enter the frequency\n"))
atom1=int(input("Enter the atom number 1\n"))
atom2=int(input("Enter the atom number 2\n"))

with open(file_name,'r')as f:
    lines=f.readlines()


i=0    
while i<len(lines):
    if "Frequencies" in lines[i]:
        parts=lines[i].strip().split()
        freq=([float(x) for x in parts[2:]])
        for idx_num,f in enumerate(freq):
            if math.isclose(f,target_freq,abs_tol=1e-4):
#                print(f"Freq = {target_freq}, index = {idx_num}")    
                i+=5
                while i<len(lines):
                    if "Frequencies" in lines[i]:
                        break
                    parts=lines[i].strip().split()
                    if int(parts[0]) == atom1:
                        coord1 = (float(parts[2+3*idx_num]), float(parts[3+3*idx_num]), float(parts[4+3*idx_num]))
                        print(f"Coordinates for atom number 1 = {coord1}")
                    elif int(parts[0]) == atom2:
                        coord2 = (float(parts[2+3*idx_num]), float(parts[3+3*idx_num]), float(parts[4+3*idx_num]))
                        print(f"Coordinates for atom number 2 = {coord2}")
                        dist = math.sqrt((coord2[0]-coord1[0])**2+(coord2[1]-coord1[1])**2+(coord2[2]-coord1[2])**2)
                        print(f"Distace between Atom 1 and Atom 2 = {dist}")
                        break                
                    i+=1
                break 
    i+=1




            
       
