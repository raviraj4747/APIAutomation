#!/usr/bin/python

import sys, os


def runCommand(script1, testresult1):
    command = "aws ecs run-task --cluster selenium-automation --task-definition selenium-automation:5 --launch-type FARGATE --network-configuration \"awsvpcConfiguration={subnets=[subnet-096b4f0a86729de0e],securityGroups=[sg-0e156fef484038cff],assignPublicIp=ENABLED}\" --overrides '{\"containerOverrides\":[{\"name\": \"selenium-automation\", \"command\": [\"pytest\",\"" + script1 + "\",\"--junitxml=" + testresult1 + "\"]}]}'&"
    return command


script1 = str(sys.argv[0])
testresult1 = str(sys.argv[1]) + "_" + ".xml"
print(testresult1)
print(runCommand(script1, testresult1))
os.system(runCommand(script1, testresult1))
