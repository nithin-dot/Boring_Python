#/bin/python
# Turn On the Less secure app access in google security
# https://myaccount.google.com/security?gar=1
# Make sure your IMAP is enable in your gmail settings
# https://mail.google.com/mail/u/1/#settings/fwdandpop
# Then run the program :)
import imaplib
import re 
from pytz import timezone
from datetime import timedelta
import email
import time

import datetime    
host = 'imap.gmail.com' # mail api address
username = 'example.com'# enter your mail address
password = 'Password' # enter your password
cleaner = re.compile('<.*?>') #clear the tags from mail
cleaner_2 = re.compile('=.*?=')
byte=[] # array declare
email_data = {}
def get_inbox():#function
    mail = imaplib.IMAP4_SSL(host) 
    mail.login(username, password) #login using your credentials
    status, messages = mail.select() # read inbox from your mail address
    # today = datetime.datetime.now()  # get the current date and time
    # yesterday = today - timedelta(days = 1)  # get yesterday date
    # Time=yesterday.strftime("%d-%b-%Y") #format the date to 12 Oct 2021
    # date='SINCE '+Time
    _,search_data=mail.search(None,'ALL') # search mail by date
    list=[int(i) for i in search_data[0].decode().split()]
    print(len(list))
    for num in search_data[0].split():
        print(f'Deleted Id:{num.decode()}')
        if(int(num.decode())>len(list)-500):
            mail.expunge()
            break
        _, data = mail.fetch(num,'(RFC822)') #Standard for ARPA Internet Text Messages
        _, b = data[0] #extract the 0th index from the list
        email_message = email.message_from_bytes(b) #decode the the mail messege
        for From,Date,sub in zip(['from'],['Date'],['subject']): # extract the data from the msg
            frommail = re.sub(cleaner, '',email_message[From]) # rm the unwanted char
            if("Gmail Team" in frommail):
                continue
            elif("GOKULAKRISHNAN D" in frommail):
                continue
            elif("MADHUSUDHANAN G" in frommail):
                continue
            elif("BALAKUMAR M" in frommail):
                continue
            elif("SHRI THARANYAA J P BIT" in frommail):
                continue
            elif("TAMILSELVAN S" in frommail):
                continue
            mail.store(num, "+FLAGS", "\\Deleted")
            print(f'\nDeleted From {frommail}at {email_message[Date]}') #format the input
            # print(f'Subject {sub}')
            # s=input("\nPress Enter to Continue....") #enter to continue or type any other key and press enter
            # if(s!=''):
            #     exit()
                

 

if __name__ == "__main__":
    my_inbox = get_inbox()


#To Extract the body 
        # email_data[From] = email_message[From]
        # for part in email_message.walk():
        #     if part.get_content_type() == "text/plain":
        #         body = part.get_payload(decode=True)
        #         print(body.decode())

  




# Old code
#TTS
    #     for header in ['from']:
    #         val=sheet.cell(row,column)
    #         val.value=email_message[header].rsplit('<', 1)[0]
    #         # tts = gtts.gTTS("mail from"+email_message[header].rsplit('<', 1)[0])
    #         # tts.save("C:/Users/Yourname/Desktop/email/"+num.decode()+".mp3")
    #         # playsound("C:/Users/Yourname/Desktop/email/"+num.decode()+".mp3")    
    #         # st = dateutil.parser.parse(email_message['date'])
    #         print("{}: {}".format(header, email_message[header]))
    #         # print(st.strftime('%a, %b %d, %Y at %I:%M %p'))

# This code is used to extract the forms and meeting links in the email...

    #         email_data[header] = email_message[header]
    #     for part in email_message.walk():
    #         if part.get_content_type() == "text/plain":
    #             body = part.get_payload(decode=True)
    #             email_data['body'] = body.decode()
    #             regax='http[s]?://forms.gle/(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    #             # regax='http[s]?://meet.google.com/(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    #             match=re.findall(regax, email_data['body'])
    #             # match = re.findall(regaxs, email_data['body'])
    #             # re.findall(regex, email_data['body'])
    #             # match = re.findall(r"on \d.*\d", email_data['body'])
    #             # word = ['AM','PM','Pm','pM','pm','2020']
    #             # text=email_data['body']
    #             # print(text[text.index('on')+len('on'):text.index('.')])
    #             for m in match:                 
    #                 data=sheet.cell(row,columns)
    #                 data.value=m
    #                 row+=1   
    #         elif part.get_content_type() == "text/html":
    #             html_body = part.get_payload(decode=True)
    #             email_data['html_body'] = html_body.decode()
    #     my_message.append(email_data)
    # return my_message
    
