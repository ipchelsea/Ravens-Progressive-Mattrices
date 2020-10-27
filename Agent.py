# Your Agent for solving Raven's Progressive Matrices. You MUST modify this file.
#
# You may also create and submit new files in addition to modifying this file.
#
# Make sure your file retains methods with the signatures:
# def __init__(self)
# def Solve(self,problem)
#
# These methods will be necessary for the project's main method to run.

# Install Pillow and uncomment this line to access image processing.
from PIL import Image
from PIL import ImageChops
import numpy
import math



class Agent:
    # The default constructor for your Agent. Make sure to execute any
    # processing necessary before your Agent starts solving problems here.
    #
    # Do not add any variables to this signature; they will not be used by
    # main().
    attributelist = ['']
    def __init__(self):
        pass
  
    #Transformations
    #Referencing Geeks 4 Geeks
    #One of PIL.Image.FLIP_LEFT_RIGHT, PIL.Image.FLIP_TOP_BOTTOM, PIL.Image.ROTATE_90, PIL.Image.ROTATE_180, PIL.Image.ROTATE_270 or PIL.Image.TRANSPOSE.
    def rotate_90(self,image):
        transposed  = image.transpose(Image.ROTATE_90)
        return transposed

    def rotate_180(self,image):
        transposed  = image.transpose(Image.ROTATE_180)
        return transposed

    def rotate_270(self,image):
        transposed  = image.transpose(Image.ROTATE_270)
        return transposed    

    def reflect_LtoR(self,image):
        transposed  = image.transpose(Image.FLIP_LEFT_RIGHT)
        return transposed    

    def reflect_TtoB(self,image):
        transposed  = image.transpose(Image.FLIP_TOP_BOTTOM)
        return transposed    

    # The primary method for solving incoming Raven's Progressive Matrices
    def Solve(self,problem):

        choices_arr = [] #constructs empty array
        xrange = range
        for i in xrange(0,6):
            choices_arr.append(0)
    
        print("Basic Problems B" + ", " + problem.name + "\n")

        if len(problem.figures)!= 9: #checks for out of bounds exception
            return answer
        elif problem.problemType == "2x2":
            print (problem.problemType)

        for figName in problem.figures:
            if figName == "A":
               figA = problem.figures['A']
               FigA = Image.open(figA.visualFilename)
            elif figName == "B":
               figB = problem.figures['B']
               FigB = Image.open(figB.visualFilename)
            elif figName == "C":
               figC = problem.figures['C']
               FigC = Image.open(figC.visualFilename)
            elif figName == "1":
               fig1 = problem.figures['1']
               Choice1 = Image.open(fig1.visualFilename)
               choices_arr[0] = Choice1
            elif figName == "2":
               fig2 = problem.figures['2']
               Choice2 = Image.open(fig2.visualFilename)
               choices_arr[1] = Choice2
            elif figName == "3":
               fig3 = problem.figures['3']
               Choice3 = Image.open(fig3.visualFilename)
               choices_arr[2] = Choice3
            elif figName == "4":
               fig4 = problem.figures['4']
               Choice4 = Image.open(fig4.visualFilename)
               choices_arr[3] = Choice4
            elif figName == "5":
               fig5 = problem.figures['5']
               Choice5 = Image.open(fig5.visualFilename)
               choices_arr[4] = Choice5
            elif figName == "6":
               fig6 = problem.figures['6']
               Choice6 = Image.open(fig6.visualFilename)
               choices_arr[5] = Choice6


        #Rotate figure A to check against B,C and choices 1 to 6
        checkA_rotate90 = self.rotate_90(FigA)
        checkA_rotate180 = self.rotate_180(FigA)
        checkA_rotate270 = self.rotate_270(FigA)
        checkA_reflect = self.reflect_LtoR(FigA)
        checkA_deflect = self.reflect_TtoB(FigA)

        #Compares FigA to FigB, I used Root Mean Square difference to check for similarities
        if self.rmsdiff(checkA_rotate90, FigB) == 0:
            #print("Rotates Fig A 90 degrees, checks to B then checks C")
            #if A and B are the same, check C against options 1 through 6
            checkC_rotate90 = self.rotate_90(FigC)
            index = -1
            for choice in choices_arr:
                Check_ans = self.rmsdiff(checkC_rotate90, choice) #checks C against choices 1 to 6
                if Check_ans == 0:
                    index = choices_arr.index(choice) + 1
            return index #returns a number 

        #Compares FigA to FigC, I used Root Mean Square difference to check for similarities
        elif self.rmsdiff(checkA_rotate90, FigC) == 0:
            #print("Rotates Fig A 90 degrees, checks to C then checks B")
         #if A and C are the same, check B against options 1 through 6
            checkB_rotate90 = self.rotate_90(FigB)
            index = -1

            for choice in choices_arr:
                Check_ans = self.rmsdiff(checkB_rotate90, choice) #checks B against choices 1 to 6
                if Check_ans == 0: #if answer is the same
                    index = choices_arr.index(i) + 1
            return index #returns a number 

        elif self.rmsdiff(checkA_rotate180, FigB) == 0:
            #print("Rotates Fig A 180 degrees, checks to B then checks C")
            #if A and B are the same, check C against options 1 through 6
            checkC_rotate180 = self.rotate_180(FigC)
            index = -1
            for choice in choices_arr:
                Check_ans = self.rmsdiff(checkC_rotate180, choice) #checks C against choices 1 to 6
                if Check_ans == 0:
                    index = choices_arr.index(choice) + 1
            return index #returns a number 

        elif self.rmsdiff(checkA_rotate180, FigC) == 0:
            #print("Enters 180 rotation  A->C")
         #if A and C are the same, check B against options 1 through 6
            checkB_rotate180 = self.rotate_180(FigB)
            index = -1

            for choice in choices_arr:
                Check_ans = self.rmsdiff(checkB_rotate180, choice) #checks B against choices 1 to 6
                if Check_ans == 0: #if answer is the same
                    index = choices_arr.index(choice) + 1
            return index #returns a number

        elif self.rmsdiff(checkA_rotate270, FigB) == 0:
            #print("Enters 270 rotation  A -> B")
         #if A and C are the same, check B against options 1 through 6
            checkC_rotate270 = self.rotate_270(FigC)
            index = -1

            for choice in choices_arr:
                Check_ans = self.rmsdiff(checkC_rotate270, choice) #checks B against choices 1 to 6
                if Check_ans == 0: #if answer is the same
                    index = choices_arr.index(choice) + 1
            return index #returns a number

        elif self.rmsdiff(checkA_rotate270, FigC) == 0:
            #print("Enters 270 rotation A->C ")
         #if A and C are the same, check B against options 1 through 6
            checkB_rotate270 = self.rotate_270(FigB)
            index = -1

            for choice in choices_arr:
                Check_ans = self.rmsdiff(checkB_rotate270, choice) #checks B against choices 1 to 6
                if Check_ans == 0: #if answer is the same
                    index = choices_arr.index(choice) + 1
            return index #returns a number

        elif self.rmsdiff(checkA_reflect, FigB) == 0:
            #print("Enters reflection")
        #if A reflects B, check B against options 1 through 6                
            checkC_reflect = self.reflect_LtoR(FigC)
            index = -1
            for choice in choices_arr:

                Check_ans = self.rmsdiff(checkC_reflect, choice)
                if Check_ans == 0:
                   index = choices_arr.index(choice)+1
            return index

        #Looking at B-04                   
        elif self.rmsdiff(checkA_deflect, FigC) == 0:
            #print("Enters deflection")
         #if A deflects C, check B against options 1 through 6  
            checkB_reflect = self.reflect_TtoB(FigB)
            index = -1

            for choice in choices_arr:
                Check_ans = self.rmsdiff(checkB_reflect, choice)
                if Check_ans == 0:
                   index = choices_arr.index(choice)+ 1
                
            return index
            
        else:
            #print("all else")
            index = -1
            min = 1000000000
            absolutediff = self.rmsdiff(FigA, FigB)
            for choice in choices_arr:
                Check_ans = self.rmsdiff(FigC, choice)
            
                diff = math.fabs(absolutediff - Check_ans) #returns absolute value 
                #print(diff)
                #print(min)
                if diff < min:
                   min = diff
                   index = choices_arr.index(choice)+1
            return index


    #def check_ifShaded()

    #Compares 2 different images with RMS 
    def rmsdiff(self, im1, im2):
        #print("Calculate the root-mean-square difference between two images")
    
        image1 = im1.convert('L')
        image2 = im2.convert('L')

        diff = ImageChops.difference(image1, image2)
        h = diff.histogram()
       
        return math.sqrt(sum(h*(i**2) for i, h in enumerate(h))) / (float(im1.size[0]) * im1.size[1])