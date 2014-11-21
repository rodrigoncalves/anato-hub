#!/bin/bash
echo -n "Removing *.pyc ------------------------------------------ "
find . -type f -name "*.pyc" -exec rm -rf "{}" \;

sudo coverage erase
sudo coverage run --source='.' manage.py test
sudo coverage xml -o test-reports/coverage.xml 
sudo /opt/sonar-runner-2.3/bin/sonar-runner

