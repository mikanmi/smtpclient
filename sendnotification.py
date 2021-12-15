#!/usr/bin/env python3

# Copyright (c) 2021 Patineboot. All rights reserved.
# sendnotification.py is licensed under the 2-Clause BSD license.

import sys
import subprocess
import argparse

# a SMTP client program
SMTP_CLIENT_PROGRAM = "msmtp"
TO_HEADER_TAG = "To:"
SUBJECT_HEADER_TAG = "Subject:"

class SmtpClient:

    def __init__(self, verbose):

        verbose_option = ""
        if verbose:
            verbose_option = "-v"

        self.__verbose = verbose_option
        self.__mail = ""

    def send(self, recipient):
        send_command_line = f"{SMTP_CLIENT_PROGRAM} {self.__verbose} {recipient}"

        send_command = send_command_line.split()
        process = subprocess.run(send_command, text=True, input=self.__mail, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        print (process.stdout, end="")
        if process.returncode != 0:
            process.check_returncode()

    def createNotification(self, subject, to):
        # read sys.stdin
        notification = sys.stdin.read()

        # add the mail headers, which are Subject: and To.
        subject_headher = ""
        if subject is not None:
            subject_headher = SUBJECT_HEADER_TAG + subject + "\n"
        to_headher = TO_HEADER_TAG + to  + "\n"

        self.__mail = subject_headher + to_headher + "\n" + notification

        print(self.__mail)

if __name__ == "__main__":
    # add command options to the argument parser.
    parser = argparse.ArgumentParser(
        prog="sendnotification.py",
        description="The mail command to send a notification!"
    )
    parser.add_argument("-s", "--subject", help="add a subject in the mail")
    parser.add_argument("-v", "--verbose", action="store_true", help="run with verbose mode")
    parser.add_argument("recipient", help="send a notification to recipient")

    # get command options from the command line.
    options = parser.parse_args()
    subject = options.subject
    verbose = options.verbose
    recipient = options.recipient

    # Create a notification
    smtpClient = SmtpClient(verbose)
    smtpClient.createNotification(subject, recipient)

    # Send the notification
    smtpClient.send(recipient)
