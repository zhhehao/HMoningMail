#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'This mod be used to send mail'

__author__ = 'Bruce He'

import smtplib
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

def Hmod_send_mail(subject, content=''):

	def _format_addr(s):
		_name, _addr = parseaddr(s)
		return formataddr((Header(_name, 'utf-8').encode(), _addr))

	# sender address
	_from_addr = 'hpythonscript@bt.com'
	# password if need to auth
	# qq mail need verify code in here, not password
	# _password = ''
	# multi receivers can put into a list
	_to_addr = ['bruce.he@bt.com', 'oaheh@qq.com']
	# smtp server address
	_smtp_server = 'smtpr.bt.com'


	# create mail content
	msg = MIMEText(content, 'plain', 'utf-8')
	msg['From'] = _format_addr('HPython Script <%s>' % _from_addr)
	msg['To'] = _format_addr('Dear Bruce <%s>' % _to_addr)
	msg['Subject'] = Header(subject, 'utf-8').encode()

	# smtplib instance, no SSL
	_server = smtplib.SMTP(_smtp_server, 25)
	# _server = smtplib.SMTP_SSL('smtp.qq.com', 465)
	# display connect information
	_server.set_debuglevel(1)
	# login if need password
	# _server.login(_from_addr, _password)
	# encrypt by tls, if need
	_server.starttls()
	# send mail
	_server.sendmail(_from_addr, _to_addr, msg.as_string())
	# quit server
	_server.quit()

# if __name__ == '__main__':
# 	Hmod_send_mail('Hello, world!')
