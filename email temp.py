from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from smtplib import SMTP
import smtplib
import sys
import config


 
username = config.username
password =config.password
mail_from = config.username
mail_to = "********@.com"
mail_subject = "OCI CS Wallix Attempts"

mimemsg = MIMEMultipart('alternative')
mimemsg['From']=mail_from
mimemsg['To']=mail_to
mimemsg['Subject']=mail_subject


html = """\
<html> 
    <head>
      <title>Cyber Security Data Analytics Alert</title>

  
    </head>
    <body>               
         <p style="font-family:verdana; font-size:2.0em; color:#1F497D;">
            Alert Type: <b>Low</b><br/>
                     Total Connection attempts to Wallix:{} 
                     <style>
                     {}

    </p>				
		<p style="font-family:verdana; font-size:1.87empx; color:#1F497D;" >
			 Regards,<br/>
			 SaH Cyber Securty Data Analytics<br/>
			 Powered by SaH International<br/>
			<span style="font-family:verdana; font-size:1.0em; color:#FF0000;">
				* This email has been generated as part of the SaH Cyber Security monitoring and it is intended for Cyber Security Analyst use only. 
			</span>
		</p>
	</body>
</html>
""".format(total_attempts,df1.iloc [0:6, 0:5].to_html())


part1 = MIMEText(html, 'html')

mimemsg.attach(part1)

connection = smtplib.SMTP(host='smtp.office365.com', port=587)
connection.starttls()
connection.login(username,password)
connection.send_message(mimemsg)
logfile(a, filename)
connection.quit()