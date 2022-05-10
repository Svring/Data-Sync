# PNG-IDAT-Payload-Generator
Generate a PNG with a payload embedded in the IDAT chunk (Based off of previous concepts and code -- credit given below)
Additionally, bruteforce payloads matching a regex pattern

This is a Python3, PEP8-compatible, fully-working version of huntergregal's initial project. Rewritten and fixed by https://github.com/TheZ3ro @TheZ3Pro

## Based Off of Previous Concepts and Research
* Hunter Gregal -- https://github.com/huntergregal/PNG-IDAT-Payload-Generator
* Adam Logue -- https://www.adamlogue.com/revisiting-xss-payloads-in-png-idat-chunks
* IDontPlayDarts -- https://www.idontplaydarts.com/2012/06/encoding-web-shells-in-png-idat-chunks
* fin1te -- https://whitton.io/articles/xss-on-facebook-via-png-content-types
* Vavkamil -- https://github.com/vavkamil/PNG-IDAT-chunks

## Usage
```
usage: generate.py [-h] -m {xss,php} [-r REMOTEDOMAIN] -o OUTPUTIMAGE

Tool to generate PNG-IDAT Payloads.

optional arguments:
  -h, --help            show this help message and exit
  -m {xss,php}, --method {xss,php}
                        Choose payload method, -h to view available methods
  -r REMOTEDOMAIN, --remote-domain REMOTEDOMAIN
                        Remote domain to retrieve payload from (shorter the
                        better: ex. xx.xxx)
  -o OUTPUTIMAGE, --output-file OUTPUTIMAGE
                        Output payload to PNG file
```
* To bruteforce pattern matches, modify "payloadPatternBruter.py" to meet your needs and run it. 

## Concept
1. Generate PNG payload
 1. Bruteforce hex string that Gzdeflates into target payload
 2. Engineer discovered Gzdeflate string to bypass PNG filters
 3. Generate PNG file with payload embeded in IDAT chunk
2. Upload PNG payload to vulnerable target web application
3. Take control of web application response content-type (example: .png.html)

## To Do
* Vavkamil Bruteforce method(s) , tld vs prefix
* Pure Bruteforce method (long)
* Port `payloadPatternBruter.py` to Python3
