# SmtpClient

The smtp client send a body with Title and To header conveniently.

```bash
% python3 sendnotification.py -h
usage: sendnotification.py [-h] [-s SUBJECT] [-v] recipient

The mail command to send a notification!

positional arguments:
  recipient             send a notification to recipient

optional arguments:
  -h, --help            show this help message and exit
  -s SUBJECT, --subject SUBJECT
                        add a subject in the mail
  -v, --verbose         run with verbose mode
```
