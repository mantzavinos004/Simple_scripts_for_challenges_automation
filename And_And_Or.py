#you get a csv file with 4 inputs of 1 or 0. Those r going through two AND gates and one OR. The output is binary so we reverse it to ASCII
import csv

def script(input_file):
        results=[]
        with open(input_file,mode='r') as infile:
                csvreader =csv.reader(infile)
                next(csvreader)
                
                for row in csvreader:
                        input1=int(row[0])
                        input2=int(row[1])
                        input3=int(row[2])
                        input4=int(row[3])

                        and1=input1 & input2
                        and2=input3 & input4
                        final= and1 | and2
                        results.append(str(final))
                return ''.join(results)
input_file='input.csv'
output=script(input_file)

print(output)

ascii_text=''.join(chr(int(output[i:i+8],2)) for i in range(0,len(output),8))
print("The above binary gives the following ASCII: ",ascii_text)
