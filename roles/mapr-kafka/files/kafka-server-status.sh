#!/bin/sh
# {{ ansible_managed }}
ps -ef | grep -i 'kafka\.Kafka'
exit $?