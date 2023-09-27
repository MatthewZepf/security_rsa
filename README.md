# security_rsa
This is some starter code for implementing RSA encryption (public and private keys) in Python using the RSA module  
I'll post my solution after today if anyone want's to check  

# How to get started
install vscode (not necessary if you have another python ide you love, but it makes this simpler)  
<h5> For Mac: Follow <a href="https://eecs485staff.github.io/p1-insta485-static/setup_macos.html"> this </a>  </h5>

<h5> For Windows: </h5>  
Please have Ubuntu with wsl 2 installed, and run the following commands  
you can check if you have wsl 2 by running the following command $ wsl -l -v in Ubuntu  
if you see a 2 below version you are good  
Run the following commands to make sure you have Python 3, pip, and virtual environments setup  <br>
$ sudo apt update  <br>
$ sudo apt install python3 python3-pip python3-venv python3-wheel python3-setuptools git tree default-jre   <br> 
<br>

<h5> For both OS </h5>
Make a directory for security via terminal/ubuntu  
this can be done with $mkdir security when you find a spot you are fine putting it  
$cd security/ to enter into the directory,  
then type $git clone https://github.com/MatthewZepf/security_rsa.git to get the files  
navigate to the new directory (use ls and cd here)  
when you are in the new directory containing main.py run the following commands in terminal  
$ python3 -m venv env
$ source env/bin/activate
$ pip install rsa
$ code . 
then you should have all the necessary packages installed 
to run the python file in terminal, simply enter  
$ python3 main.py  
If you have any questions, for installing vscode you can follow the 280 tutorials here although we don't use c++ for security
https://eecs280staff.github.io/tutorials/setup_vscode.html  
For more details on the python setup, you can find the eecs 485 tutorial https://eecs485staff.github.io/p1-insta485-static/setup_macos.html  
<h1> If you have any trouble with setup or the coding, let me know </h1>

