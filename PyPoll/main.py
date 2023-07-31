#*******************************************************************************************
 #
 #  File Name:  main.py
 #
 #  File Description:
 #      This program takes a set of poll data from a csv file in the Resources folder, 
 #      election_data.csv, composed of three columns: "Voter ID", "County", and "Candidate". 
 #      This Python script analyzes the votes and calculates each of the following values: 
 #      the total number of votes cast, a complete list of candidates who received votes, the 
 #      percentage of votes each candidate won, the total number of votes each candidate won, 
 #      and the winner of the election based on popular vote.  In addition, the program both 
 #      prints the analysis to the terminal and exports a text file with the results, 
 #      election_data_analysis.txt, to the analysis folder.
 #
 #
 #  Date            Description                             Programmer
 #  ----------      ------------------------------------    ------------------
 #  07/30/2023      Initial Development                     Nicholas George
 #
 #******************************************************************************************/

import csv
from enum import Enum


# This enumeration contains constant indices for the input csv file's columns.
class DataColumnIndicesEnumeration(Enum):

    BALLOT_ID_INDEX = 0

    COUNTY_INDEX = 1

    CANDIDATE_INDEX = 2


# This enumeration contains indices for the nested summary dictionary's keys.
class DictionaryIndicesEnumeration(Enum):

    TOTAL_VOTES = 0

    CANDIDATES = 1

    WINNER = 2


    NESTED_DATA = 1

    NAME = 0

    PERCENT = 1

    VOTE_COUNT = 2


# These constants contain the names of the input and output file paths.
CONSTANT_INPUT_FILE_NAME = './Resources/election_data.csv'

CONSTANT_OUTPUT_FILE_NAME = './analysis/election_data_analysis.txt'


# These constants are the title and tile line for the output data.
CONSTANT_OUTPUT_DATA_TITLE = 'Election Results'

CONSTANT_OUTPUT_DATA_TITLE_LINE = '----------------------------'

# This constant is the program's message if there is a tie for the winner.
CONSTANT_CANDIDATE_TIE_MESSAGE = 'There is no winner: the election is a tie!'


#*******************************************************************************************
 #
 #  Subroutine Name:  calculateCandidatePercentagesSubRoutine()
 #
 #  Subroutine Description:
 #      This subroutine calculates each candidate's percentage of the total vote based 
 #      on the candidate's vote count and the total vote count.  The program assigns 
 #      the calculated percentage to the summary dictionary's candidate percent list.
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

def calculateCandidatePercentagesSubRoutine():

    tempPercentFloatVariable = 0.0

    for candidateIndex, candidateName in enumerate(summaryDictionary[list(summaryDictionary.keys())[DictionaryIndicesEnumeration.CANDIDATES.value]][list(list(summaryDictionary.items())[DictionaryIndicesEnumeration.CANDIDATES.value][DictionaryIndicesEnumeration.NESTED_DATA.value].keys())[DictionaryIndicesEnumeration.NAME.value]]):
        
        tempPercentFloatVariable \
            = round((summaryDictionary[list(summaryDictionary.keys())[DictionaryIndicesEnumeration.CANDIDATES.value]][list(list(summaryDictionary.items())[DictionaryIndicesEnumeration.CANDIDATES.value][DictionaryIndicesEnumeration.NESTED_DATA.value].keys())[DictionaryIndicesEnumeration.VOTE_COUNT.value]][candidateIndex] \
                     / summaryDictionary[list(summaryDictionary.keys())[DictionaryIndicesEnumeration.TOTAL_VOTES.value]])*100, \
                    3)
        
        summaryDictionary[list(summaryDictionary.keys())[DictionaryIndicesEnumeration.CANDIDATES.value]][list(list(summaryDictionary.items())[DictionaryIndicesEnumeration.CANDIDATES.value][DictionaryIndicesEnumeration.NESTED_DATA.value].keys())[DictionaryIndicesEnumeration.PERCENT.value]]. \
            append(tempPercentFloatVariable)
        

#*******************************************************************************************
 #
 #  Subroutine Name:  determineWinnerSubRoutine()
 #
 #  Subroutine Description:
 #      This subroutine compares each candidate's vote count to find the winner of the
 #      election and, also, checks for a tie.
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

def determineWinnerSubRoutine():

    # This variable tells the program whether a tie has occurred between two or more winning 
    # candidates.
    candidateTieFlagBooleanVariable = False

    # This variable holds the winning candidate's nested index in the summary dictionary.
    winnerIndexIntegerVariable = 0

    # This variable holds the winning candidate's vote count.
    winnerVoteCountIntegerVariable = 0 


    # This for repetiton loop starts with the first candidate then looks for another candidate 
    # with a greater vote count. 
    for candidateIndex, candidateName in enumerate(summaryDictionary[list(summaryDictionary.keys())[DictionaryIndicesEnumeration.CANDIDATES.value]][list(list(summaryDictionary.items())[DictionaryIndicesEnumeration.CANDIDATES.value][DictionaryIndicesEnumeration.NESTED_DATA.value].keys())[DictionaryIndicesEnumeration.NAME.value]]):
        
        # The program compares vote counts to determine the greatest one and stores the winning 
        # candidate's index and vote count in the appropriate variables.
        if candidateIndex > 0:


            if summaryDictionary[list(summaryDictionary.keys())[DictionaryIndicesEnumeration.CANDIDATES.value]][list(list(summaryDictionary.items())[DictionaryIndicesEnumeration.CANDIDATES.value][DictionaryIndicesEnumeration.NESTED_DATA.value].keys())[DictionaryIndicesEnumeration.VOTE_COUNT.value]][candidateIndex] > winnerVoteCountIntegerVariable:
            
                winnerVoteCountIntegerVariable = summaryDictionary[list(summaryDictionary.keys())[DictionaryIndicesEnumeration.CANDIDATES.value]][list(list(summaryDictionary.items())[DictionaryIndicesEnumeration.CANDIDATES.value][DictionaryIndicesEnumeration.NESTED_DATA.value].keys())[DictionaryIndicesEnumeration.VOTE_COUNT.value]][candidateIndex]
            
                winnerIndexIntegerVariable = candidateIndex
       

        # The program initializes the vote count variable with the first candidate's vote count; 
        # the index is already initialized to the first candidate upon declaration.
        else:

            winnerVoteCountIntegerVariable \
                = summaryDictionary[list(summaryDictionary.keys())[DictionaryIndicesEnumeration.CANDIDATES.value]][list(list(summaryDictionary.items())[DictionaryIndicesEnumeration.CANDIDATES.value][DictionaryIndicesEnumeration.NESTED_DATA.value].keys())[DictionaryIndicesEnumeration.VOTE_COUNT.value]][candidateIndex]


    # The program now takes the winning candidates vote count and compares it to the other candidate's 
    # vote counts.  If there is a match, the program changes the Boolean flag value to true and writes 
    # a message to the appropriate summary dictionary member before exiting the for loop.
    for candidateIndex, candidateName in enumerate(summaryDictionary[list(summaryDictionary.keys())[DictionaryIndicesEnumeration.CANDIDATES.value]][list(list(summaryDictionary.items())[DictionaryIndicesEnumeration.CANDIDATES.value][DictionaryIndicesEnumeration.NESTED_DATA.value].keys())[DictionaryIndicesEnumeration.NAME.value]]):
  
        if summaryDictionary[list(summaryDictionary.keys())[DictionaryIndicesEnumeration.CANDIDATES.value]][list(list(summaryDictionary.items())[DictionaryIndicesEnumeration.CANDIDATES.value][DictionaryIndicesEnumeration.NESTED_DATA.value].keys())[DictionaryIndicesEnumeration.VOTE_COUNT.value]][candidateIndex] \
            == winnerVoteCountIntegerVariable and candidateIndex != winnerIndexIntegerVariable:

            candidateTieFlagBooleanVariable \
                = True

            summaryDictionary[list(summaryDictionary.keys())[DictionaryIndicesEnumeration.WINNER.value]] \
                = CONSTANT_CANDIDATE_TIE_MESSAGE
            
            break

    
    # If there is no tie, the program writes the winning candidate's name to the appropriate summary 
    # dictionary member.
    if candidateTieFlagBooleanVariable == False:
        
        summaryDictionary[list(summaryDictionary.keys())[DictionaryIndicesEnumeration.WINNER.value]] \
            = summaryDictionary[list(summaryDictionary.keys())[DictionaryIndicesEnumeration.CANDIDATES.value]][list(list(summaryDictionary.items())[DictionaryIndicesEnumeration.CANDIDATES.value][DictionaryIndicesEnumeration.NESTED_DATA.value].keys())[DictionaryIndicesEnumeration.NAME.value]][winnerIndexIntegerVariable]


#*******************************************************************************************
 #
 #  Subroutine Name:  readFileAndCalculateValuesSubRoutine
 #
 #  Subroutine Description:
 #      This subroutine reads the input csv file and calculates the summary values needed 
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

    # This variable contains the candidate's name from the current row of data.
    currentCandidateNameStringVariable \
        = ''

    # This variable is a Boolean flag that tells the program that it has encountered
    # a new candidate in the data.
    candidateFoundFlagBooleanVariable \
        = False


    #This line of code opens the csv file and returns a file object.
    with open(CONSTANT_INPUT_FILE_NAME) as csvFile:


        # This line of code reads the data from the file object and assigns 
        # it to a reader object.
        csvReaderObject \
            = csv.reader(csvFile)


        # This for repetition loop moves down the rows of data and calculates the values 
        # for the summary.
        for rowDataIndex, csvRow in enumerate(csvReaderObject):
   
            # If the row index is equal to zero, the program takes no action because the 
            # first row of data is the header information.
            
            # If the row index is greater than one, the program increments vote counts 
            # and looks for new candidates.
            if rowDataIndex > 1: 
                

                # This line of code assigns the current candidate's name to the appropriate 
                # variable.
                currentCandidateNameStringVariable \
                    = csvRow[DataColumnIndicesEnumeration.CANDIDATE_INDEX.value]
                
                # This line of code sets initializes the Boolean flag to false for processing.
                candidateFoundFlagBooleanVariable \
                    = False


                # This for repetition loop looks at all the existing candidates in the summary 
                # dictionary.
                for candidateIndex, candidateName in enumerate(summaryDictionary[list(summaryDictionary.keys())[DictionaryIndicesEnumeration.CANDIDATES.value]][list(list(summaryDictionary.items())[DictionaryIndicesEnumeration.CANDIDATES.value][DictionaryIndicesEnumeration.NESTED_DATA.value].keys())[DictionaryIndicesEnumeration.NAME.value]]):
                
                    # If the program finds the current candidate in the summary dictionary, it 
                    # increments the candidate's vote count, sets the Boolean flag to true, 
                    # and exits the for loop.
                    if candidateName == currentCandidateNameStringVariable:
                        
                        summaryDictionary[list(summaryDictionary.keys())[DictionaryIndicesEnumeration.CANDIDATES.value]][list(list(summaryDictionary.items())[DictionaryIndicesEnumeration.CANDIDATES.value][DictionaryIndicesEnumeration.NESTED_DATA.value].keys())[DictionaryIndicesEnumeration.VOTE_COUNT.value]][candidateIndex] \
                            += 1
                        
                        candidateFoundFlagBooleanVariable = True
                        
                        break
                

                # If the program did not find the current candidate in the summary dictionary, 
                # it adds the candidate and sets the vote count to one.
                if candidateFoundFlagBooleanVariable == False:

                    summaryDictionary[list(summaryDictionary.keys())[DictionaryIndicesEnumeration.CANDIDATES.value]][list(list(summaryDictionary.items())[DictionaryIndicesEnumeration.CANDIDATES.value][DictionaryIndicesEnumeration.NESTED_DATA.value].keys())[DictionaryIndicesEnumeration.NAME.value]].append(currentCandidateNameStringVariable)
                    
                    summaryDictionary[list(summaryDictionary.keys())[DictionaryIndicesEnumeration.CANDIDATES.value]][list(list(summaryDictionary.items())[DictionaryIndicesEnumeration.CANDIDATES.value][DictionaryIndicesEnumeration.NESTED_DATA.value].keys())[DictionaryIndicesEnumeration.VOTE_COUNT.value]].append(1)


            # If the row index is equal to one, it adds the first candidate to the summary 
            # dictionary and sets his/her vote count to one.
            elif rowDataIndex == 1:

                currentCandidateNameStringVariable = csvRow[DataColumnIndicesEnumeration.CANDIDATE_INDEX.value]

                summaryDictionary[list(summaryDictionary.keys())[DictionaryIndicesEnumeration.CANDIDATES.value]][list(list(summaryDictionary.items())[DictionaryIndicesEnumeration.CANDIDATES.value][DictionaryIndicesEnumeration.NESTED_DATA.value].keys())[DictionaryIndicesEnumeration.NAME.value]].append(currentCandidateNameStringVariable)
               
                summaryDictionary[list(summaryDictionary.keys())[DictionaryIndicesEnumeration.CANDIDATES.value]][list(list(summaryDictionary.items())[DictionaryIndicesEnumeration.CANDIDATES.value][DictionaryIndicesEnumeration.NESTED_DATA.value].keys())[DictionaryIndicesEnumeration.VOTE_COUNT.value]].append(1)
    

    # This line of code takes the counter from the for loop and assigns its value to the summary 
    # dictionary's total votes member.
    summaryDictionary[list(summaryDictionary.keys())[DictionaryIndicesEnumeration.TOTAL_VOTES.value]] = rowDataIndex


    calculateCandidatePercentagesSubRoutine()

    determineWinnerSubRoutine()


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

    print(f'{list(summaryDictionary.keys())[DictionaryIndicesEnumeration.TOTAL_VOTES.value]}: {summaryDictionary[list(summaryDictionary.keys())[DictionaryIndicesEnumeration.TOTAL_VOTES.value]]}')

    print()

    print(CONSTANT_OUTPUT_DATA_TITLE_LINE)

    print()


    for candidateIndex, candidateName in enumerate(summaryDictionary[list(summaryDictionary.keys())[DictionaryIndicesEnumeration.CANDIDATES.value]]):
        
        print(f'{summaryDictionary[list(summaryDictionary.keys())[DictionaryIndicesEnumeration.CANDIDATES.value]][list(list(summaryDictionary.items())[DictionaryIndicesEnumeration.CANDIDATES.value][DictionaryIndicesEnumeration.NESTED_DATA.value].keys())[DictionaryIndicesEnumeration.NAME.value]][candidateIndex]}: {summaryDictionary[list(summaryDictionary.keys())[DictionaryIndicesEnumeration.CANDIDATES.value]][list(list(summaryDictionary.items())[DictionaryIndicesEnumeration.CANDIDATES.value][DictionaryIndicesEnumeration.NESTED_DATA.value].keys())[DictionaryIndicesEnumeration.PERCENT.value]][candidateIndex]}% ({summaryDictionary[list(summaryDictionary.keys())[DictionaryIndicesEnumeration.CANDIDATES.value]][list(list(summaryDictionary.items())[DictionaryIndicesEnumeration.CANDIDATES.value][DictionaryIndicesEnumeration.NESTED_DATA.value].keys())[DictionaryIndicesEnumeration.VOTE_COUNT.value]][candidateIndex]})')
        
        print()


    print(CONSTANT_OUTPUT_DATA_TITLE_LINE)

    print()

    print(f'{list(summaryDictionary.keys())[DictionaryIndicesEnumeration.WINNER.value]}: {summaryDictionary[list(summaryDictionary.keys())[DictionaryIndicesEnumeration.WINNER.value]]}')

    print()

    print(CONSTANT_OUTPUT_DATA_TITLE_LINE)

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

        txtFile.write(f'{list(summaryDictionary.keys())[DictionaryIndicesEnumeration.TOTAL_VOTES.value]}: {summaryDictionary[list(summaryDictionary.keys())[DictionaryIndicesEnumeration.TOTAL_VOTES.value]]}')

        txtFile.write('\n\n')

        txtFile.write(CONSTANT_OUTPUT_DATA_TITLE_LINE)

        txtFile.write('\n\n')


        for candidateIndex, candidateName in enumerate(summaryDictionary[list(summaryDictionary.keys())[DictionaryIndicesEnumeration.CANDIDATES.value]]):
            
            txtFile.write(f'{summaryDictionary[list(summaryDictionary.keys())[DictionaryIndicesEnumeration.CANDIDATES.value]][list(list(summaryDictionary.items())[DictionaryIndicesEnumeration.CANDIDATES.value][DictionaryIndicesEnumeration.NESTED_DATA.value].keys())[DictionaryIndicesEnumeration.NAME.value]][candidateIndex]}: {summaryDictionary[list(summaryDictionary.keys())[DictionaryIndicesEnumeration.CANDIDATES.value]][list(list(summaryDictionary.items())[DictionaryIndicesEnumeration.CANDIDATES.value][DictionaryIndicesEnumeration.NESTED_DATA.value].keys())[DictionaryIndicesEnumeration.PERCENT.value]][candidateIndex]}% ({summaryDictionary[list(summaryDictionary.keys())[DictionaryIndicesEnumeration.CANDIDATES.value]][list(list(summaryDictionary.items())[DictionaryIndicesEnumeration.CANDIDATES.value][DictionaryIndicesEnumeration.NESTED_DATA.value].keys())[DictionaryIndicesEnumeration.VOTE_COUNT.value]][candidateIndex]})')
            
            txtFile.write('\n\n')


        txtFile.write(CONSTANT_OUTPUT_DATA_TITLE_LINE)

        txtFile.write('\n\n')

        txtFile.write(f'{list(summaryDictionary.keys())[DictionaryIndicesEnumeration.WINNER.value]}: {summaryDictionary[list(summaryDictionary.keys())[DictionaryIndicesEnumeration.WINNER.value]]}')

        txtFile.write('\n\n')

        txtFile.write(CONSTANT_OUTPUT_DATA_TITLE_LINE)

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

    'Total Votes' : 0,

    'Candidates' : {'Name' : [], 'Percent' : [], 'Vote Count' : []},

    'Winner' : ''

}


readFileAndCalculateValuesSubRoutine()

writeDataToTerminalSubRoutine()

writeDataToFileSubRoutine()
