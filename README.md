# Shadow Views
 #       v.1.0
# Simple bot to get number of viewers to your youtube videos made by Python,Tor, And Selenium Webdrive with 120 refresh time rate



# Requirements 

1) Tor
2) stem library
3) Pysocks
4) Python3
5) Selenium

# Tested on kali Linux,Ubuntu,Debian

works only on Linux

# ! Installation !

Linux

`apt-get install tor`

Now open tor configuration file located in /etc/tor/torrc and uncomment below lines.

`ControlPort 9051`

`HashedControlPassword "your password"`


Save and exit.


`pip install stem`

`pip install pysocks`

`install selenium`

`install firefox webdrive and add the path loctaed in (/etc/bin) and chmod 755`

`service tor restart`

If you are using both python version on single machine use pip3 for python3

# How to use

`git clone https://github.com/c0d3l3ss/shadow-view.git`

`cd Shadow-Traffic`

`chmod 744 shadows.py`

`python3 shadows.py`

`enter your tor password from torrc file`

`enter target address with protocol`

`enter number of views you want`

`Now target link will be visited with different ip and User-Agent`

`you can add more agnets in agents.txt file(the file include over 10K radom users)`

# Support

https://twitter.com/c03d3lss

This Script is updated from breakfold traffic python script which requests links only
Shadow traffic get real views with requests

# Disclaimer

Author will not take any responsibility of your activity using this tool.
For Educational purpose only.

# Credits
@c0d3l3ss

# License

MIT License
