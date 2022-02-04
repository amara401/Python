import boto3
aws_ecs= boto3.client('ecs')  # indicates service
response = aws_ecs.describe_tasks(
    clusters='<cluster_name/cluster_arn>',
    tasks=[
        'string',   # for single task
/* for cluster in clusters:
    clusterName = cluster.split(‘/’)[1]
    tasks = aws_ecs.list_tasks(cluster=clusterName)[taskArns]
     task_names = aws_ecs. describe_tasks(cluster=cluster tasks=tasks)[‘tasks’]
    print(task_description)*/ for multiple tasks
    ],
    include=[
        'TAGS',
    ]
)
for containers in response:
print(‘image’)

#======================================================#

import boto3

client = boto3.client('ecs', region='eu-west-1')

response = client.describe_clusters(
    clusters=[
        'ran-dev-ecs',
    ],
    include=[
        'ATTACHMENTS'|'CONFIGURATIONS'|'SETTINGS'|'STATISTICS'|'TAGS',
    ]
)

##################################################

import boto3

client = boto3.client('ecs', region='eu-west-1')

response = client.list_clusters(
)

####################################################
import boto3

client = boto3.client('ecs', region='eu-west-1')

response = client.describe_tasks(
    cluster='ran-dev-ecs',
    tasks=[
        'string',
    ],
    include=[
        'TAGS',
    ]
)

###################################################
import boto3

client = boto3.client('ecs', region='eu-west-1')

response = client.list_tasks(
    cluster='ran-dev-ecs',
)

print(response)


###########################################
response = client.describe_tasks(
    cluster='ran-dev-ecs',
    tasks=[
        x,
    ]
)

#======================================================================#
import smtplib  
import email.utils
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

SENDER = 'madaa@dnb.com'  
SENDERNAME = 'Amarnadh MM'

# Replace recipient@example.com with a "To" address. If your account 
# is still in the sandbox, this address must be verified.
RECIPIENT  = 'madaa@dnb.com'

# Replace smtp_username with your Amazon SES SMTP user name.
USERNAME_SMTP = "smtp_username"

# Replace smtp_password with your Amazon SES SMTP password.
PASSWORD_SMTP = "smtp_password"

# (Optional) the name of a configuration set to use for this message.
# If you comment out this line, you also need to remove or comment out
# the "X-SES-CONFIGURATION-SET:" header below.
#CONFIGURATION_SET = "ConfigSet"

# If you're using Amazon SES in an AWS Region other than US West (Oregon), 
# replace email-smtp.us-west-2.amazonaws.com with the Amazon SES SMTP  
# endpoint in the appropriate region.
HOST = "email-smtp.us-west-1.amazonaws.com"
PORT = 587

# The subject line of the email.
SUBJECT = 'This is test SES mail'

# The email body for recipients with non-HTML email clients.
BODY_TEXT = ("Amazon SES Test\r\n"
             "This email was sent through the Amazon SES SMTP "
             "Interface using the Python smtplib package."
            )


# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = SUBJECT
msg['From'] = email.utils.formataddr((SENDERNAME, SENDER))
msg['To'] = RECIPIENT
# Comment or delete the next line if you are not using a configuration set
#msg.add_header('X-SES-CONFIGURATION-SET',CONFIGURATION_SET)

# Record the MIME types of both parts - text/plain and text/html.
part1 = MIMEText(BODY_TEXT, 'plain')
#part2 = MIMEText(BODY_HTML, 'html')

# Attach parts into message container.
# According to RFC 2046, the last part of a multipart message, in this case
# the HTML message, is best and preferred.
msg.attach(part1)
#msg.attach(part2)

# Try to send the message.
try:  
    server = smtplib.SMTP(HOST, PORT)
    server.ehlo()
    server.starttls()
    #stmplib docs recommend calling ehlo() before & after starttls()
    server.ehlo()
    server.login(USERNAME_SMTP, PASSWORD_SMTP)
    server.sendmail(SENDER, RECIPIENT, msg.as_string())
    server.close()
# Display an error message if something goes wrong.
except Exception as e:
    print ("Error: ", e)
else:
    print ("Email sent!")
    

#################################################################################

import smtplib, ssl

smtp_server = "smtp.gmail.com"
port = 587  # For starttls
sender_email = "my@gmail.com"
password = input("Type your password and press enter: ")
receiver_email = 
message = 

# Create a secure SSL context
context = ssl.create_default_context()

# Try to log in to server and send email
try:
    server = smtplib.SMTP(smtp_server,port)
    server.ehlo() # Can be omitted
    server.starttls(context=context) # Secure the connection
    server.ehlo() # Can be omitted
    server.login(sender_email, password)
	server.sendmail(sender_email, receiver_email, message)
    # TODO: Send email here
except Exception as e:
    # Print any error messages to stdout
    print(e)
finally:
    server.quit()     
	
	
#################################################################################
import requests
# Define the remote file to retrieve
remote_url = 'https://www.google.com/robots.txt'
# Define the local filename to save data
local_file = 'local_copy.txt'
# Make http request for remote file data
data = requests.get(remote_url)
# Save file data to local copy
with open(local_file, 'wb')as file:
   file.write(data.content)	
