import sys

#checking ip address file and content validity

def ip_file_valid():
    #Prompting user for input
    ip_file = input ("\n# Enter IP file path and name (e.g D:\MyApps\myfile.txt) : ")

    #Checking if the file exists
    if os.path.isfile(ip)