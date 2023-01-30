import os
import pandas as pd 
import csv


#function to read and remove Rawp that is less than 0.05. Concordance twin
def read_file1(file1,file2):

    with open (file1, "r") as rf:
        with open (file2, "a") as output:
            header = rf.readline()
            header = header.split()
            next(rf)
            for line in rf:
                lines = line.split()
                if float(lines[17]) < 0.05:
                    output.write(line+"\n")
                else:
                    continue

            dataframe = pd.read_csv(file2, sep = "\t", header=None, index_col = 0)
            
            return dataframe.to_csv(file2 , sep = '\t', index = True, header = header)

read_file1('/Users/thingnguyen/Documents/Projects/Twinproject/BloodLoad/Results/Result4_Refbase_beforenorm/Blood01232023_MZClClp_Concordant_RefBase_CellTypeCorrected_MvalueLogitRes_multinom_mztwinreg_BeforeNor.txt',
'/Users/thingnguyen/Documents/Projects/Twinproject/BloodLoad/Results/Result4_Refbase_beforenorm/MZClClp_Concordant_RefBase_BeforeNor_t-test_p-val_less_than_0.05.csv')

#function to read and remove logis that is less than 0.05. Concordance twin
def read_file2(file1,file2):

    with open (file1, "r") as rf:
        with open (file2, "a") as output:
            header = rf.readline()
            header = header.split()
            next(rf)
            for line in rf:
                lines = line.split()
                if float(lines[21]) < 0.05:
                    output.write(line+"\n")
                else:
                    continue

            dataframe = pd.read_csv(file2, sep = "\t", header=None, index_col = 0)
            
            return dataframe.to_csv(file2 , sep = '\t', index = True, header = header)

read_file2('/Users/thingnguyen/Documents/Projects/Twinproject/BloodLoad/Results/Result4_Refbase_beforenorm/Blood01232023_MZClClp_Concordant_RefBase_CellTypeCorrected_MvalueLogitRes_multinom_mztwinreg_BeforeNor.txt',
'/Users/thingnguyen/Documents/Projects/Twinproject/BloodLoad/Results/Result4_Refbase_beforenorm/MZClClp_Concordant_RefBase_BeforeNor_logisreg_p-val_less_than_0.05.csv')

#function to read and remove Rawp that is less than 0.05. MZtwin
def read_file3(file1,file2):

    with open (file1, "r") as rf:
        with open (file2, "a") as output:
            header = rf.readline()
            header = header.split()
            next(rf)
            for line in rf:
                lines = line.split()
                if float(lines[49]) < 0.05:
                    output.write(line+"\n")
                else:
                    continue

            dataframe = pd.read_csv(file2, sep = "\t", header=None, index_col = 0)
            
            return dataframe.to_csv(file2 , sep = '\t', index = True, header = header)

read_file3('/Users/thingnguyen/Documents/Projects/Twinproject/BloodLoad/Results/Result4_Refbase_beforenorm/Blood06142022_MZClClp_RefBase_CellTypeCorrected_MvalueLogitRes_mztwinreg_BeforeNor_PN.txt',
'/Users/thingnguyen/Documents/Projects/Twinproject/BloodLoad/Results/Result4_Refbase_beforenorm/MZClClp_RefBase_BeforeNor_t-test_p-val_less_than_0.05.csv')

#function to read and remove Logis that is less than 0.05. MZtwin
def read_file4(file1,file2):

    with open (file1, "r") as rf:
        with open (file2, "a") as output:
            header = rf.readline()
            header = header.split()
            next(rf)
            for line in rf:
                lines = line.split()
                if float(lines[53]) < 0.05:
                    output.write(line+"\n")
                else:
                    continue

            dataframe = pd.read_csv(file2, sep = "\t", header=None, index_col = 0)
            
            return dataframe.to_csv(file2 , sep = '\t', index = True, header = header)

read_file4('/Users/thingnguyen/Documents/Projects/Twinproject/BloodLoad/Results/Result4_Refbase_beforenorm/Blood06142022_MZClClp_RefBase_CellTypeCorrected_MvalueLogitRes_mztwinreg_BeforeNor_PN.txt',
'/Users/thingnguyen/Documents/Projects/Twinproject/BloodLoad/Results/Result4_Refbase_beforenorm/MZClClp_RafBase_BeforeNor_Logisreg_p-val_less_than_0.05.csv')