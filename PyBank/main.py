#*******************************************************************************************
 #
 #  File Name:  main.py
 #
 #  File Description:
 #      This program, main.py, reads budget data from a csv file in the Resources folder, 
 #      budget_data.csv, composed of two columns: "Date" and "Profit/Losses".  The Python 
 #      script analyzes the records to calculate each of the following values: the total 
 #      number of months included in the dataset, the net total amount of "Profit/Losses" 
 #      over the entire period, the changes in "Profit/Losses" over the entire period and 
 #      the average of those changes, the greatest increase in profits (date and amount) 
 #      over the entire period, and the greatest decrease in profits (date and amount) over 
 #      the entire period.  In addition, the program both prints the analysis to the terminal 
 #      and exports a text file with the results, budget_data_analysis.txt, to the analysis 
 #      folder.
 #
 #
 #  Date            Description                             Programmer
 #  ----------      ------------------------------------    ------------------
 #  07/30/2023      Initial Development                     Nicholas George
 #
 #******************************************************************************************/

import csv
from enum import Enum


# This enumeration contains constant values for the input csv file's column indices.
class DataColumnIndexEnumeration(Enum):

    DATE_COLUMN_INDEX = 0

    PROFIT_LOSS_COLUMN_INDEX = 1


# This enumeration contains indices for the nested summary dictionary's keys.
class DictionaryIndicesEnumeration(Enum):

    TOTAL_MONTHS = 0

    TOTAL = 1

    AVERAGE_CHANGE = 2

    GREATEST_INCREASE_IN_PROFIT_LOSS = 3

    GREATEST_DECREASE_IN_PROFIT_LOSS = 4


    NESTED_DATA = 1

    DATE = 0

    VALUE = 1


# These constants contain the names of the input and output file paths.
CONSTANT_INPUT_FILE_NAME = './Resources/budget_data.csv'

CONSTANT_OUTPUT_FILE_NAME = './analysis/budget_data_analysis.txt'


# This constant is the title and tile line for the output data.
CONSTANT_OUTPUT_DATA_TITLE = 'Financial Analysis'

CONSTANT_OUTPUT_DATA_TITLE_LINE = '----------------------------'


#*******************************************************************************************
 #
 #  Subroutine Name:  readFileAndCalculateValuesSubRoutine
 #
 #  Subroutine Description:
 #      This subroutine reads an input csv file and calculates the summary values needed 
 #      for the program output.
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

    # These variables contain the current and last profit/loss values as the program moves
    # down the rows of input data.
    lastProfitLossIntegerVariable = 0

    currentProfitLossIntegerList = 0


    # These variables contain the change in profit/loss between the current and last
    # values and the net change in profit/loss.
    currentChangesProfitLossIntegerVariable = 0

    netChangesProfitLossIntegerVariable = 0


    #This line of code opens the csv file and returns a file object.
    with open(CONSTANT_INPUT_FILE_NAME) as csvFile:

        # This line of code reads the data from the file object and assigns 
        # it to a reader object.
        csvReaderObject = csv.reader(csvFile)

        # This for repetition loop moves down the rows of data and calculates the values 
        # for the summary.
        for rowIndex, csvRow in enumerate(csvReaderObject):

            # If the row index is equal to zero, the program takes no action because the first 
            # row of data is the header information.
            
            # If the row index is greater than one, these lines of code calculate the changes 
            # in profit/loss and update summary dictionary variables for the net total 
            # profit/loss, net total change in profit/loss, and dates and names for the
            # greatest increase and greatest decrease in profit/loss.
            if rowIndex > 1: 

                # This line of code takes the current profit/loss value from the row of data 
                # and assigns it to a variable.
                currentProfitLossIntegerVariable \
                    = int(csvRow[DataColumnIndexEnumeration.PROFIT_LOSS_COLUMN_INDEX.value])

                # This line of code adds the current profit/loss value to the summary dictionary
                # value for the net total profit/loss .
                summaryDictionary[list(summaryDictionary.keys())[DictionaryIndicesEnumeration.TOTAL.value]] \
                    += currentProfitLossIntegerVariable


                # This line of code calculates the change in profit/loss and assigns it
                # to a variable.
                currentChangesProfitLossIntegerVariable \
                    = (currentProfitLossIntegerVariable - lastProfitLossIntegerVariable)

                # This line of code adds the current change in profit/loss to the net total 
                # change in profit/loss.
                netChangesProfitLossIntegerVariable \
                    += currentChangesProfitLossIntegerVariable


                # This line of code assigns the current profit/loss value to the variable 
                # for the last profit/loss value for the next row.
                lastProfitLossIntegerVariable \
                    = currentProfitLossIntegerVariable


                # These lines of code check to see if the current increase in profit/loss 
                # is the greatest increase.  If it is, the program assigns the date and
                # value in the row of data to the appropriate summary dictionary variables.
                if currentChangesProfitLossIntegerVariable \
                    > summaryDictionary[list(summaryDictionary.keys())[DictionaryIndicesEnumeration.GREATEST_INCREASE_IN_PROFIT_LOSS.value]][list(list(summaryDictionary.items())[DictionaryIndicesEnumeration.GREATEST_INCREASE_IN_PROFIT_LOSS.value][DictionaryIndicesEnumeration.NESTED_DATA.value].keys())[DictionaryIndicesEnumeration.VALUE.value]]:

                    summaryDictionary[list(summaryDictionary.keys())[DictionaryIndicesEnumeration.GREATEST_INCREASE_IN_PROFIT_LOSS.value]][list(list(summaryDictionary.items())[DictionaryIndicesEnumeration.GREATEST_INCREASE_IN_PROFIT_LOSS.value][DictionaryIndicesEnumeration.NESTED_DATA.value].keys())[DictionaryIndicesEnumeration.DATE.value]] \
                        = csvRow[DataColumnIndexEnumeration.DATE_COLUMN_INDEX.value]

                    summaryDictionary[list(summaryDictionary.keys())[DictionaryIndicesEnumeration.GREATEST_INCREASE_IN_PROFIT_LOSS.value]][list(list(summaryDictionary.items())[DictionaryIndicesEnumeration.GREATEST_INCREASE_IN_PROFIT_LOSS.value][DictionaryIndicesEnumeration.NESTED_DATA.value].keys())[DictionaryIndicesEnumeration.VALUE.value]] \
                        = currentChangesProfitLossIntegerVariable


                # These lines of code check to see if the current decrease in profit/loss 
                # is the greatest decrease.  If it is, the program assigns the date and
                # value in the row of data to the appropriate summary dictionary variables.
                if currentChangesProfitLossIntegerVariable \
                    < summaryDictionary[list(summaryDictionary.keys())[DictionaryIndicesEnumeration.GREATEST_DECREASE_IN_PROFIT_LOSS.value]][list(list(summaryDictionary.items())[DictionaryIndicesEnumeration.GREATEST_DECREASE_IN_PROFIT_LOSS.value][DictionaryIndicesEnumeration.NESTED_DATA.value].keys())[DictionaryIndicesEnumeration.VALUE.value]]:
                    summaryDictionary[list(summaryDictionary.keys())[DictionaryIndicesEnumeration.GREATEST_DECREASE_IN_PROFIT_LOSS.value]][list(list(summaryDictionary.items())[DictionaryIndicesEnumeration.GREATEST_DECREASE_IN_PROFIT_LOSS.value][DictionaryIndicesEnumeration.NESTED_DATA.value].keys())[DictionaryIndicesEnumeration.DATE.value]] \
                        = csvRow[DataColumnIndexEnumeration.DATE_COLUMN_INDEX.value]
                    
                    summaryDictionary[list(summaryDictionary.keys())[DictionaryIndicesEnumeration.GREATEST_DECREASE_IN_PROFIT_LOSS.value]][list(list(summaryDictionary.items())[DictionaryIndicesEnumeration.GREATEST_DECREASE_IN_PROFIT_LOSS.value][DictionaryIndicesEnumeration.NESTED_DATA.value].keys())[DictionaryIndicesEnumeration.VALUE.value]] \
                        = currentChangesProfitLossIntegerVariable


            # If the row index is equal to one, the program is looking at the first row 
            # of data, and there is change in profit/loss to calculate.
            elif rowIndex == 1:

                # This line of code assigns the current profit/loss value in the data 
                # to the variable for the last profit/loss value, so the program can 
                # use it in the next iteration.
                lastProfitLossIntegerVariable \
                    = int(csvRow[DataColumnIndexEnumeration.PROFIT_LOSS_COLUMN_INDEX.value])
                

                # This line of code initializes the summary dictionary variable for net 
                # total profit/loss with the current protfit/loss value in the data.
                summaryDictionary[list(summaryDictionary.keys())[DictionaryIndicesEnumeration.TOTAL.value]] \
                    = lastProfitLossIntegerVariable
    
    
    # This line of code assigns the row index in the for loop to the summary dictionary variable for the total 
    # number of months.
    summaryDictionary[list(summaryDictionary.keys())[DictionaryIndicesEnumeration.TOTAL_MONTHS.value]] = rowIndex


    # This line of code calculates the average change in profit/loss by taking the net changes in profit/loss 
    # and dividing by the number of months minus one, because changes in profit/loss do not start until the 
    # second month when there is both a current and last value available.
    summaryDictionary[list(summaryDictionary.keys())[DictionaryIndicesEnumeration.AVERAGE_CHANGE.value]] \
        = round( \
            float( \
                netChangesProfitLossIntegerVariable) \
                    / float(summaryDictionary[list(summaryDictionary.keys())[DictionaryIndicesEnumeration.TOTAL_MONTHS.value]]-1), \
                  2)


#*******************************************************************************************
 #
 #  Subroutine Name:  writeDataToTerminalSubRoutine
 #
 #  Subroutine Description:
 #      This subroutine writes the data in the summary dictionary to the terminal.
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

    print()

    print(CONSTANT_OUTPUT_DATA_TITLE)

    print()

    print(CONSTANT_OUTPUT_DATA_TITLE_LINE)

    print()

    print(f'{list(summaryDictionary.keys())[DictionaryIndicesEnumeration.TOTAL_MONTHS.value]}: {summaryDictionary[list(summaryDictionary.keys())[DictionaryIndicesEnumeration.TOTAL_MONTHS.value]]}')

    print()

    print(f'{list(summaryDictionary.keys())[DictionaryIndicesEnumeration.TOTAL.value]}: ${summaryDictionary[list(summaryDictionary.keys())[DictionaryIndicesEnumeration.TOTAL.value]]}')

    print()

    print(f'{list(summaryDictionary.keys())[DictionaryIndicesEnumeration.AVERAGE_CHANGE.value]}: ${summaryDictionary[list(summaryDictionary.keys())[DictionaryIndicesEnumeration.AVERAGE_CHANGE.value]]}')

    print()

    print(f'{list(summaryDictionary.keys())[DictionaryIndicesEnumeration.GREATEST_INCREASE_IN_PROFIT_LOSS.value]}: {summaryDictionary[list(summaryDictionary.keys())[DictionaryIndicesEnumeration.GREATEST_INCREASE_IN_PROFIT_LOSS.value]][list(list(summaryDictionary.items())[DictionaryIndicesEnumeration.GREATEST_INCREASE_IN_PROFIT_LOSS.value][DictionaryIndicesEnumeration.NESTED_DATA.value].keys())[DictionaryIndicesEnumeration.DATE.value]]} (${summaryDictionary[list(summaryDictionary.keys())[DictionaryIndicesEnumeration.GREATEST_INCREASE_IN_PROFIT_LOSS.value]][list(list(summaryDictionary.items())[DictionaryIndicesEnumeration.GREATEST_INCREASE_IN_PROFIT_LOSS.value][DictionaryIndicesEnumeration.NESTED_DATA.value].keys())[DictionaryIndicesEnumeration.VALUE.value]]})')

    print()

    print(f'{list(summaryDictionary.keys())[DictionaryIndicesEnumeration.GREATEST_DECREASE_IN_PROFIT_LOSS.value]}: {summaryDictionary[list(summaryDictionary.keys())[DictionaryIndicesEnumeration.GREATEST_DECREASE_IN_PROFIT_LOSS.value]][list(list(summaryDictionary.items())[DictionaryIndicesEnumeration.GREATEST_DECREASE_IN_PROFIT_LOSS.value][DictionaryIndicesEnumeration.NESTED_DATA.value].keys())[DictionaryIndicesEnumeration.DATE.value]]} (${summaryDictionary[list(summaryDictionary.keys())[DictionaryIndicesEnumeration.GREATEST_DECREASE_IN_PROFIT_LOSS.value]][list(list(summaryDictionary.items())[DictionaryIndicesEnumeration.GREATEST_DECREASE_IN_PROFIT_LOSS.value][DictionaryIndicesEnumeration.NESTED_DATA.value].keys())[DictionaryIndicesEnumeration.VALUE.value]]})')

    print()


#*******************************************************************************************
 #
 #  Subroutine Name:  writeDataToFileSubRoutine
 #
 #  Subroutine Description:
 #      This subroutine writes the data in the summary dictionary to the output file.
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

    with open(CONSTANT_OUTPUT_FILE_NAME, 'w') as txtFile:
    
        txtFile.write('\n')

        txtFile.write(CONSTANT_OUTPUT_DATA_TITLE)

        txtFile.write('\n\n')

        txtFile.write(CONSTANT_OUTPUT_DATA_TITLE_LINE)

        txtFile.write('\n\n')

        txtFile.write(f'{list(summaryDictionary.keys())[DictionaryIndicesEnumeration.TOTAL_MONTHS.value]}: {summaryDictionary[list(summaryDictionary.keys())[DictionaryIndicesEnumeration.TOTAL_MONTHS.value]]}')

        txtFile.write('\n\n')
        
        txtFile.write(f'{list(summaryDictionary.keys())[DictionaryIndicesEnumeration.TOTAL.value]}: ${summaryDictionary[list(summaryDictionary.keys())[DictionaryIndicesEnumeration.TOTAL.value]]}')

        txtFile.write('\n\n')

        txtFile.write(f'{list(summaryDictionary.keys())[DictionaryIndicesEnumeration.AVERAGE_CHANGE.value]}: ${summaryDictionary[list(summaryDictionary.keys())[DictionaryIndicesEnumeration.AVERAGE_CHANGE.value]]}')

        txtFile.write('\n\n')

        txtFile.write(f'{list(summaryDictionary.keys())[DictionaryIndicesEnumeration.GREATEST_INCREASE_IN_PROFIT_LOSS.value]}: {summaryDictionary[list(summaryDictionary.keys())[DictionaryIndicesEnumeration.GREATEST_INCREASE_IN_PROFIT_LOSS.value]][list(list(summaryDictionary.items())[DictionaryIndicesEnumeration.GREATEST_INCREASE_IN_PROFIT_LOSS.value][DictionaryIndicesEnumeration.NESTED_DATA.value].keys())[DictionaryIndicesEnumeration.DATE.value]]} (${summaryDictionary[list(summaryDictionary.keys())[DictionaryIndicesEnumeration.GREATEST_INCREASE_IN_PROFIT_LOSS.value]][list(list(summaryDictionary.items())[DictionaryIndicesEnumeration.GREATEST_INCREASE_IN_PROFIT_LOSS.value][DictionaryIndicesEnumeration.NESTED_DATA.value].keys())[DictionaryIndicesEnumeration.VALUE.value]]})')

        txtFile.write('\n\n')

        txtFile.write(f'{list(summaryDictionary.keys())[DictionaryIndicesEnumeration.GREATEST_DECREASE_IN_PROFIT_LOSS.value]}: {summaryDictionary[list(summaryDictionary.keys())[DictionaryIndicesEnumeration.GREATEST_DECREASE_IN_PROFIT_LOSS.value]][list(list(summaryDictionary.items())[DictionaryIndicesEnumeration.GREATEST_DECREASE_IN_PROFIT_LOSS.value][DictionaryIndicesEnumeration.NESTED_DATA.value].keys())[DictionaryIndicesEnumeration.DATE.value]]} (${summaryDictionary[list(summaryDictionary.keys())[DictionaryIndicesEnumeration.GREATEST_DECREASE_IN_PROFIT_LOSS.value]][list(list(summaryDictionary.items())[DictionaryIndicesEnumeration.GREATEST_DECREASE_IN_PROFIT_LOSS.value][DictionaryIndicesEnumeration.NESTED_DATA.value].keys())[DictionaryIndicesEnumeration.VALUE.value]]})')

        txtFile.write('\n')


#*******************************************************************************************
 #
 #  Subroutine Name: n/a
 #
 #  Subroutine Description:
 #      This is the main subroutine, the beginning and end of this program's execution.
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

    'Greatest Increase in Profits' : {'Date' : '', 'Value' : 0 },

    'Greatest Decrease in Profits' : {'Date' : '', 'Value' : 0 },

}


readFileAndCalculateValuesSubRoutine()


writeDataToTerminalSubRoutine()


writeDataToFileSubRoutine()
