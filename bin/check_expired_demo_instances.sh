#!/bin/bash
# Run as check_expired_demo_instances.sh region

region=$1
source /opt/himlarcli/bin/activate
/opt/himlarcli/demo.py expired -d 60 --region $region -t notify/demo-notify-expired-instances-30dleft.txt --force --debug --dry-run
/opt/himlarcli/demo.py expired -d 75 --region $region -t notify/demo-notify-expired-instances-15dleft.txt --force --debug --dry-run
/opt/himlarcli/demo.py expired -d 89 --region $region -t notify/demo-notify-expired-instances-1dleft.txt --force --debug --dry-run
