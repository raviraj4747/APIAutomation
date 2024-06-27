#!/usr/bin/python

import sys, os


def runCommand(script1, script2,testresult1,testresult2):
    command = "aws ecs run-task --cluster selenium-automation --task-definition selenium-automation:5 --launch-type FARGATE --network-configuration \"awsvpcConfiguration={subnets=[subnet-096b4f0a86729de0e],securityGroups=[sg-0e156fef484038cff],assignPublicIp=ENABLED}\" --overrides '{\"containerOverrides\":[{\"name\": \"selenium-automation\", \"command\": [\"pytest\",\"" + script1 + "\",\"--junitxml=" + testresult1 + ";pytest\",\"" + script2 + "\",\"--junitxml=" + testresult2 + "\"]}]}'&"
    return command

script1 = str(sys.argv[1])
script2 = str(sys.argv[2])
testresult1 = str(sys.argv[1]) + "_" + ".xml"
testresult2 = str(sys.argv[2]) + "_" + ".xml"
print(testresult1)
print(testresult2)
print(runCommand(script1, script2, testresult1, testresult2))
os.system(runCommand(script1, script2, testresult1, testresult2))
