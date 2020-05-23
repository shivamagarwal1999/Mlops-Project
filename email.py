import smtplib
sender = 'Enter senders mail id'
receiver = 'Enter recievers mail id'
passwd ='Enter senders password'
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
message = "Hello Developer, Your model has been trained Successfully and gives the accuracy= cat /code/accuracy.txt .
           Thank you."
server.sendmail(sender, receiver, message)
