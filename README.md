# Mac-Camera
Using python on my macbook with opencv and webcam


I will be using openCV 4.0 on my macbook air. I currently have sierra, however, you can use whatever version of OSX as long as its above Sierra.

Installing openCV is kind of a pain. make sure you have python and homebrew installed via terminal. also get pip. 

    #download the latest version of python: I use 3.6 for stability issues with older version of mac osx, 
    but it is entirely user prefrence:
    https://www.python.org/downloads/
    and pick your version
    
    
    #to install homebrew copy and paste this directly in terminal:
    /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
    
    #then to update and get wget to install pip:
    brew update
    brew install wget

    
    #to install pip copy and paste this directly in terminal:
    wget https://bootstrap.pypa.io/get-pip.py
    sudo python3 get-pip.py
    
    #now some people like to use virtual enviornments, however I have only had issues while trying to use them so I skipped it
    and went straight on my mac for easeier functionality:
    sudo pip install opencv-contrib-python
    
Now open CV is on your mac.

   A few things I like to get installed before any code is:
      pip install numpy
      pip install matplotlib
      pip install imutils
      pip install transform
  

Now start making code!!
    
