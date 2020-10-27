# Ravens-Progressive-Mattrices

##Introduction
Raven’s Progressive Matrices (RPM) is a human intelligence test that uses visual analogies of geometric shapes to solve the missing figure within a problem matrix. In Project 1, the goal is to design a Knowledge-Based AI agent that can pass at least 7 out of 12 (2x2) Test Problems in Basic B and Test B, as it progressively gets more challenging. To determine the answer for the problem as shown in Figure 1, we first observe the semantic relationships that can be made from A->B and C-> D. D being one of the 6 options available on the right.

##Implementation
Python was the language choice for this project. As recommended in the project description, the only libraries that were used were PIL (https://pillow.readthedocs.io/en/stable/)  which stood for  ‘Python Imaging Library’  and Numpy, a ‘Primary Array Programming Library’. “The image module provides a class with the same name which is used to represent a PIL image. The module also provides a number of factory functions, including functions to load images from files, and to create new images”(Sunitamamgai, 2019). The image differences and rotations were calculated via six utility functions  :

- ImageChops.difference()
- image.transpose(Image.ROTATE_90)
- image.transpose(Image.ROTATE_180
- image.transpose(Image.ROTATE_270)
- image.transpose(Image.FLIP_LEFT_RIGHT)
- image.transpose(Image.FLIP_TOP_BOTTOM

My main function (‘rmsdiff’) simply converts two images into grayscale, then calls on ImageChops.difference(). This will return the absolute value of the pixel-by-pixel difference between 2 images. Additionally, the function simply calculates the root-mean-square difference between Figure A to B or C. For further checks, this function can compare B and C to 6 different choices by iterating through an array ‘choice_arr’. I used Image.open(figx.VisualFilename) to store all the figures under variable names. To sum up, my agent for solving 2X2 matrices utilizes both concepts of production rules, semantic networks and generate/test. 
