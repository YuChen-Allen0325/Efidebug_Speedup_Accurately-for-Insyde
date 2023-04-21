from . import TransformToUppercase
def AllGuidXrefUppercase(MessGuid):
    
    String = ''
    
    String1 = MessGuid[0:8]
    String2 = MessGuid[9:13]
    String3 = MessGuid[14:18]
    String4 = MessGuid[19:23]
    String5 = MessGuid[24:36]
    
    String1 = TransformToUppercase.TransToUppercase(String1)
    String2 = TransformToUppercase.TransToUppercase(String2)
    String3 = TransformToUppercase.TransToUppercase(String3)
    String4 = TransformToUppercase.TransToUppercase(String4)
    String5 = TransformToUppercase.TransToUppercase(String5)
    
    String = String1 + '-' + String2 + '-' + String3 + '-' + String4 + '-' + String5
    
    
    return String