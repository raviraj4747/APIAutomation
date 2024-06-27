#!/usr/bin/python

import sys, os


def runCommand(script, testresult):
    command = "aws ecs run-task --cluster converse-selenium --task-definition converse-selenium:7 --launch-type FARGATE --region us-east-1 --network-configuration \"awsvpcConfiguration={subnets=[subnet-0f9ed585c4d6d5f75],securityGroups=[sg-0d984628f590b7397],assignPublicIp=ENABLED}\" --overrides '{\"containerOverrides\": [{\"name\": \"converse-selenium\", \"command\": [\"pytest\",\"" + script + "\",\"--junitxml=" + testresult + "\"]}]}'&"

    return command


script = str(sys.argv[1])
# username   = str(sys.argv[2])
# password   = str(sys.argv[3])
# param1     = str(sys.argv[4])
# param2     = str(sys.argv[5])
# param3     = str(sys.argv[6])
testresult = str(sys.argv[1]) + "_" + ".xml"
# testresult = str(sys.argv[2])
print(testresult)
os.system(runCommand(script, testresult))
