# RockRace
A Racing Game developed with pygame in Python

for run this project you will need this requirments:
  -python3
  -pygame : $pip install pygame

to setup game in mac osx you need to install py2app with this coomand:
  $pip3 install py2app
  
  then go to your source directory and for create your own setup.py file you need to run this command:
    $py2applet --make-setup YourApplicationName.py Wrote setup.py
    
    in setup.py you can add your extra files in project with this line:
      DATA_FILES = ['yourfile1.json', 'yourfile2.png', ...]
    
    after you created setup.py , then run this last command:
      $python3 setup.py py2app -A
      
        then you will see a directory named dist that your executable app is in there
