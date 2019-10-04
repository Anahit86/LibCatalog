import configparser
from configparser import ConfigParser
parser= ConfigParser()
config_file_list= ["books.txt","users.txt"]
file1= config_file_list[0]
file2 = config_file_list[1]


fil1 = configparser.ConfigParser()
fil2 = configparser.ConfigParser()
fil1.read(file1)
fil2.read(file2)

ISBN1 = fil1.sections()
tit = [fil1[s]['title'] for s in ISBN1]
ac = [fil1[s]['available_copies'] for s in ISBN1]

userid=fil2.sections()
username=[fil2[s]["name"] for s in userid]
config=configparser.ConfigParser()

config.read("temp.txt")
config.add_section("reserve")
#for us in username:
#    config.set("reserve",us,"")
#    config.set(us,"check_out_time","")
#    config.set(us,"return_time","")
with open("temp.txt", 'w') as f:
    config.write(f)
    f.close()
