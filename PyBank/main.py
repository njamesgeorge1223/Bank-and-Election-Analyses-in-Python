#*******************************************************************************************
 #
 #  File Name:  main.py
 #
 #  File Description:
 #      The file contains the function, main, which begins program execution. This program
 #      reads budget data from a csv file, summarizes the data, and writes its results to
 #      the terminal and an output file.
 #
 #
 #  Date            Description                             Programmer
 #  ----------      ------------------------------------    ------------------
 #  07/30/2023      Initial Development                     Nicholas George
 #
 #******************************************************************************************/

import csv
from enum import Enum


# These enumerations contain constant values for the input csv file's column indices.
class ConstantsEnumeration(Enum):

    DATE_COLUMN_INDEX = 0

    PROFIT_LOSS_COLUMN_INDEX = 1


# This enumeration contains indices for the summary dictionary's keys.
class DictionaryIndicesEnumeration(Enum):

    TOTAL_MONTHS = 0

    TOTAL = 1

    AVERAGE_CHANGE = 2

    GREATEST_INCREASE_IN_PROFIT_LOSS = 3

    GREATEST_DECREASE_IN_PROFIT_LOSS = 4


# These constants contain the names of the input and output file paths.
CONSTANT_INPUT_FILE_NAME = "./Resources/budget_data.csv"

CONSTANT_OUTPUT_FILE_NAME = "./analysis/budget_data_analysis.txt"


#*******************************************************************************************
 #
 #  Subroutine Name:  readFileAndCalculateValuesSubRoutine
 #
 #  Subroutine Description:
 #      This subroutine reads an input csv file and calculates the summary values needed for
 #      the program output.
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  n/a     n/a             n/a
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  7/30/2023           Initial Development                         Nicholas George
 #
 #******************************************************************************************/

def readFileAndCalculateValuesSubRoutine():

    # These variables contain the current and last profit and loss values as the program moves
    # down the rows.
    lastProfitLossIntegerVariable = 0

    currentProfitLossIntegerList = 0


    # These variables contain the current change in profit and loss between the current and last
    # values and the net change in profit and loss.
    currentChangesProfitLossIntegerVariable = 0

    netChangesProfitLossIntegerVariable = 0


    #This line of code opens the csv file and returns a file object.
    with open(CONSTANT_INPUT_FILE_NAME) as csvFile:

        # This line of code reads the data from the file object and assigns 
        # it to a reader object.
        csvReaderObject = csv.reader(csvFile)

        # This for repetition loop calculates the values for the summary.
        for rowIndex, csvRow in enumerate(csvReaderObject):


            # This line of code assigns the row index in the for loop to the variable for the total 
            # number of months.
            summaryDictionary['Total Months'] = rowIndex


            # If the row index is equal to zero, the program takes no action because the first line 
            # of data is the header information.
            if rowIndex > 1: 


                # These lines of code calculate the changes in profit and loss and updates the net 
                # profit and loss if the row index is greater than one.
                currentProfitLossIntegerVariable \
                    = int(csvRow[ConstantsEnumeration.PROFIT_LOSS_COLUMN_INDEX.value])

                summaryDictionary['Total'] \
                    += currentProfitLossIntegerVariable


                currentChangesProfitLossIntegerVariable \
                    = (currentProfitLossIntegerVariable - lastProfitLossIntegerVariable)

                netChangesProfitLossIntegerVariable \
                    += currentChangesProfitLossIntegerVariable


                lastProfitLossIntegerVariable \
                    = currentProfitLossIntegerVariable


                # These lines of code check to see if the current increase in profit and loss 
                # is the greatest.
                if currentChangesProfitLossIntegerVariable \
                    > summaryDictionary['Greatest Increase in Profits']['Value']:

                    summaryDictionary['Greatest Increase in Profits']['Date'] \
                        = csvRow[ConstantsEnumeration.DATE_COLUMN_INDEX.value]

                    summaryDictionary['Greatest Increase in Profits']['Value'] \
                        = currentChangesProfitLossIntegerVariable


                # These lines of code check to see if the current decrease in profit and loss 
                # is the greatest.
                if currentChangesProfitLossIntegerVariable \
                    < summaryDictionary['Greatest Decrease in Profits']['Value']:

                    summaryDictionary['Greatest Decrease in Profits']['Date'] \
                        = csvRow[ConstantsEnumeration.DATE_COLUMN_INDEX.value]
                    
                    summaryDictionary['Greatest Decrease in Profits']['Value'] \
                        = currentChangesProfitLossIntegerVariable

            elif rowIndex == 1:

                # These lines of code calculate the changes in profit and loss and updates the net 
                # profit and loss if the row index is equal to one.
                lastProfitLossIntegerVariable \
                    = int(csvRow[ConstantsEnumeration.PROFIT_LOSS_COLUMN_INDEX.value])
                
                summaryDictionary['Total'] \
                    = lastProfitLossIntegerVariable

    summaryDictionary['Average Change'] \
        = round( \
            float( \
                netChangesProfitLossIntegerVariable) / float(summaryDictionary['Total Months']-1), \
                  2)


#*******************************************************************************************
 #
 #  Subroutine Name:  writeDataToTerminalSubRoutine
 #
 #  Subroutine Description:
 #      This subroutine writes the summary data to the terminal.
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  n/a     n/a             n/a
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  7/30/2023           Initial Development                         Nicholas George
 #
 #******************************************************************************************/

def writeDataToTerminalSubRoutine():


    print("Financial Analysis")

    print()

    print("----------------------------")

    print()

    print(f"{list(summaryDictionary.keys())[DictionaryIndicesEnumeration.TOTAL_MONTHS.value]}: {summaryDictionary['Total Months']}")

    print()

    print(f"{list(summaryDictionary.keys())[DictionaryIndicesEnumeration.TOTAL.value]}: ${summaryDictionary['Total']}")

    print()

    print(f"{list(summaryDictionary.keys())[DictionaryIndicesEnumeration.AVERAGE_CHANGE.value]}: ${summaryDictionary['Average Change']}")

    print()

    print(f"{list(summaryDictionary.keys())[DictionaryIndicesEnumeration.GREATEST_INCREASE_IN_PROFIT_LOSS.value]}: {summaryDictionary['Greatest Increase in Profits']['Date']} (${summaryDictionary['Greatest Increase in Profits']['Value']})")

    print()

    print(f"{list(summaryDictionary.keys())[DictionaryIndicesEnumeration.GREATEST_DECREASE_IN_PROFIT_LOSS.value]}: {summaryDictionary['Greatest Decrease in Profits']['Date']} (${summaryDictionary['Greatest Decrease in Profits']['Value']})")

    print()


#*******************************************************************************************
 #
 #  Subroutine Name:  writeDataToFileSubRoutine
 #
 #  Subroutine Description:
 #      This subroutine writes the summary data to the output file.
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  n/a     n/a             n/a
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  7/30/2023           Initial Development                         Nicholas George
 #
 #******************************************************************************************/

def writeDataToFileSubRoutine():

    with open(CONSTANT_OUTPUT_FILE_NAME, "w") as txtFile:
    
        txtFile.write("Financial Analysis")

        txtFile.write('\n\n')

        txtFile.write("----------------------------")

        txtFile.write('\n\n')

        txtFile.write(f"{list(summaryDictionary.keys())[DictionaryIndicesEnumeration.TOTAL_MONTHS.value]}: {summaryDictionary['Total Months']}")

        txtFile.write('\n\n')
        txtFile.write(f"{list(summaryDictionary.keys())[DictionaryIndicesEnumeration.TOTAL.value]}: ${summaryDictionary['Total']}")

        txtFile.write('\n\n')

        txtFile.write(f"{list(summaryDictionary.keys())[DictionaryIndicesEnumeration.AVERAGE_CHANGE.value]}: ${summaryDictionary['Average Change']}")

        txtFile.write('\n\n')

        txtFile.write(f"{list(summaryDictionary.keys())[DictionaryIndicesEnumeration.GREATEST_INCREASE_IN_PROFIT_LOSS.value]}: {summaryDictionary['Greatest Increase in Profits']['Date']} (${summaryDictionary['Greatest Increase in Profits']['Value']})")

        txtFile.write('\n\n')

        txtFile.write(f"{list(summaryDictionary.keys())[DictionaryIndicesEnumeration.GREATEST_DECREASE_IN_PROFIT_LOSS.value]}: {summaryDictionary['Greatest Decrease in Profits']['Date']} (${summaryDictionary['Greatest Decrease in Profits']['Value']})")

        txtFile.write('\n\n')


#*******************************************************************************************
 #
 #  Subroutine Name: n/a
 #
 #  Subroutine Description:
 #      This is the main subroutine, the beginning and end of this program's execution
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  n/a     n/a             n/a
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  7/30/2023           Initial Development                         Nicholas George
 #
 #******************************************************************************************/

summaryDictionary = {

    'Total Months' : 0,

    'Total' : 0,

    'Average Change' : 0.0,

    'Greatest Increase in Profits' : {'Date' : "", 'Value' : 0 },

    'Greatest Decrease in Profits' : {'Date' : "", 'Value' : 0 },

}


readFileAndCalculateValuesSubRoutine()


writeDataToTerminalSubRoutine()


writeDataToFileSubRoutine()
