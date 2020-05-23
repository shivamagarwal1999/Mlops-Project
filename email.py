import smtplib
sender = 'shivamagarwal.home@gmail.com'
receiver = 'shivamagarwal3120@gmail.com'
passwd ='shivam350'
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
message = "Hello Developer, Your model has been trained Successfully and gives the accuracy= cat /code/accuracy.txt .
           Thank you."
server.sendmail(sender, receiver, message)
