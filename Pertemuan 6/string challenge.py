def StringChallenge(strParam):
    strParam=strParam.title()
    strParam=strParam.replace('*','')
    strParam=strParam.replace(' ','')
    strParam=strParam.replace('-','')
    return strParam

print(StringChallenge(input()))