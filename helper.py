#This file contains methods that will provide assistance to other python files found within this repository.

import re

CLEANR = re.compile('<.*?>') 

def cleanhtml(raw_html):
#clean a string by removing html tags
    cleantext = re.sub(CLEANR, '', raw_html)
    return cleantext