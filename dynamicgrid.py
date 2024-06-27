#!/usr/bin/python

import sys, os


def runCommand(script1,testresult1):
    command = "aws ecs run-task --cluster selenium-automation --task-definition selenium-automation:8 --launch-type FARGATE --network-configuration \"awsvpcConfiguration={subnets=[subnet-03e1159fb00ba4aee],securityGroups=[sg-090b02cac2624f44b],assignPublicIp=ENABLED}\" --overrides '{\"containerOverrides\":[{\"name\": \"selenium-automation\", \"command\": [\"pytest\",\"" + script1 + "\",\"--junitxml=" + testresult1 + "\"]}]}'&"
    return command

script1 = str(sys.argv[1])
# username   = str(sys.argv[2])
# password   = str(sys.argv[3])
# param1     = str(sys.argv[4])
# param2     = str(sys.argv[5])
# param3     = str(sys.argv[6])
testresult = str(sys.argv[1]) + "_" + ".xml"
# testresult = str(sys.argv[2])
print(testresult)
os.system(runCommand(script1, testresult))
