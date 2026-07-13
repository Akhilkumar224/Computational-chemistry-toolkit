import os
import subprocess
import time

summary = open("Gaussian_summary.txt","w")

for file in os.listdir(os.getcwd()):
    if file.endswith(".gjf"):
        file_name = file
        cmd = f"g16 {file_name}"

        print(f"\nRunning: {file_name}")
        start_time = time.time()

        process = subprocess.run(cmd, shell=True)

        end_time = time.time()
        elapsed_time = end_time - start_time

        print(f"Time taken: {elapsed_time:.2f} seconds")

        log_file = file_name.replace(".gjf", ".log")

        if os.path.exists(log_file):
            with open(log_file, "r") as f:
                content = f.read()
                if "Normal termination" in content:
                    print(f"{file_name} terminated normally\n")
                    summary.write(f"{file_name:30s} {'SUCCESS':30s} Elapsed time = {elapsed_time:10.2f}\n") 
                else:
                    print(f"\{file_name} did NOT terminate normally")
                    summary.write(f"{file_name:30s} {'FAILED':30s} Elapsed time = {elapsed_time:10.2f}\n")
                    
        else:
            print(f"\nLog file not found for {file_name}")
            

summary.close()
