# -*- coding: utf-8 -*-
import screen_capture
import attached_mail

if __name__ == '__main__':
    filename = 'screen16.png'
    screen_capture.capture(filename)
    #
    from_addr = "tukiyo3+test@gmail.com"
    to_addr = from_addr
    subject = "screen captured." 
    body = "please help me ..."
    msg = attached_mail.create_message(from_addr, to_addr, subject, body, filename)
    attached_mail.send(from_addr, [to_addr], msg)
