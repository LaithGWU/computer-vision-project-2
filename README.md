# computer-vision-project-2

I decided to make the ascii art generator because I think ascii art is cool and is the most universal art form for computers. The inputs to my program are a jpg or png file and desired resize ratio. The output is both a print to terminal and a txt file. This repo has example inputs and outputs from my testing. This program is for anyone that has an image that they would like to convert into ascii characters for whatever reason. It would be a nice way displaying the image on a computer with no graphical interface.

The first step of this programs process is to open an image specified by the user. It then resizes the image based on a percentage given by the user and converts the image to greyscale. The program then examines the brightness value of each pixel in the image and maps an ascii character from a string of ascii characters ordered from least to most noisy. It creates a string from the combination of all these characters and then prints to the screen as well as saving it to a text file.

This process works decently for low resolution images; for higher resolution images it becomes very slow to iterate through each pixel of the image. This is fine because high resolution images don't really work well for ascii art anyway. This is part of the reason I allow the user to modify the size of the image. I let the user make the choice of percentage because in my testing I found different images needed different scales of resizing to look good in ascii.

In the end I was pretty happy with the results of my conversions, particulary with the lovers.jpg. Images with a lot of background noise, like bird.jpg, end up looking a bit too noisy. To fix this would require segmenting the foreground from the background and only producing ascii characters for the foreground. 

This program does solve the use cases for someone wanting to convert an image to ascii. I could add networking so that the user could easily send the ascii art to a friend who would be able to view it in their terminal.

For this project I mainly just used PIL. I tried using numpy to work on the array of pixels but I felt like it was overkill for what I was trying to do. I also tried to output the ascii art as an image so I could display higher character count art easier, this did not end up working out.