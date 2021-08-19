<p align="center">
<img src="attachments\email.png" width="128" height="128"/>
<br/>
<h3 align="center">bulk-email</h3>
<p align="center">Automate the process of sending emails to multiple recipients.</p>
<h2></h2>
</p>
<br />

<p align="center">
<a href="../../issues"><img src="https://img.shields.io/github/issues/aminbeigi/Bulk-Email.svg?style=flat-square" /></a>
<a href="../../pulls"><img src="https://img.shields.io/github/issues-pr/aminbeigi/Bulk-Email.svg?style=flat-square" /></a>
<img src="https://img.shields.io/github/license/aminbeigi/Bulk-Email?style=flat-square">
</p>

## Description
Bulk-Email uses the SMTP protocol to simply send emails to one or many recipients.  
Supports attachments which can be configured in config.ini.

## Instructions
1. Clone repo  
`git@github.com:aminbeigi/bulk-email.git`
2. Rename template files  
`config/config-template.ini` to `config/config.ini` and fill out fields  
`logs/bulkemail-template.log` to `bulkemail.log`  
`bulkemail/recipients-template.txt` to `bulkemail/recipients.txt`  
`bulkemail/subject-template.txt` to `bulkemail/subject.txt`  
`bulkemail/body-template.txt` to `bulkemail/body.txt`  
3. Turn on "Less secure app access" if using Gmail for Sender
4. Run `bulkemail` module with 3 command line arguments      
`python -m bulkemail bulkemail/recipients.txt bulkemail/subject.txt bulkemail/body.txt`
5. Check the log file

## Requirements
* Python 3.8.2+
* Email account

## Contributions
Contributions are always welcome!  
Just make a [pull request](../../pulls).

## Licence
MIT license
