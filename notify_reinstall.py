#!/usr/bin/python
import sys
import utils
from himlarcli.nova import Nova
from himlarcli.keystone import Keystone
from himlarcli.notify import Notify
from email.mime.text import MIMEText

options = utils.get_options('Notify users of rebuild host', dry_run=True, hosts=1)
notify = Notify(options.config, debug=options.debug)
with open('misc/notify_email.txt', 'r') as body_txt:
    body_content = body_txt.read()

# Find region
keystoneclient = Keystone(options.config)
region = keystoneclient.get_region()

# Find users
novaclient = Nova(options.config, options.host[0])
if not novaclient.valid_host():
    print "ERROR: could not find host %s" % options.host[0]
    sys.exit(1)
toaddr = novaclient.list_instances()
for user, instance in toaddr.iteritems():
    user_instances = ""
    for server,info in instance.iteritems():
        user_instances += "%s (%s)\n" % (server, info['ip'])
    msg = MIMEText(user_instances + body_content)
    msg['Subject'] = 'UH-IaaS: Terminating instance (%s)' % region
    if not options.dry_run:
        notify.send_mail(user, msg)
    print '\nUser: %s' % user
    print 'Servers:\n' + user_instances + '\n'

notify.close()