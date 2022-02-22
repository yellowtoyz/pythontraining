#!/usr/bin/env python3
"""RZFeeser | Alta3 Research
   Pushing files around using shutil and os from the standard library"""

# import additional code to complete our task
import shutil
import os

def main():
    """code to move files around"""
    # move into the working directory
    os.chdir("/home/student/pythontraining/mycode/")

    # copy the fileA to fileB
    shutil.copy("5g_researchC1/sdn_networkC1.txt", "5g_researchC1/sdn_network.txtC1.copy")

    # copy the entire directoryA to directoryB
    os.system("rm -rf /home/student/pythontraining/mycode/5g_research_backuC1p/")
    shutil.copytree("5g_researchC1/", "5g_research_backupC1/")

if __name__ == "__main__":
    main()

