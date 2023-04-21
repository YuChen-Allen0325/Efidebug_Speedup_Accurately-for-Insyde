from . import InfTransformToUppercase

def InfWriteLog(InputFileName, ClearlyDocument_Path):
    
    MyHashtagsFilter = '#'
    Purpose_Have_Equalsign = '='
    InfBaseName = 'BASE_NAME'
    InfFileGuid = 'FILE_GUID'
    BASE_NAME_Str = ''
    BASE_NAME_Clear_Str = ''
    FILE_GUID_Str = ''
    FILE_GUID_Clear_Str = ''

    try:
        with open(InputFileName, 'r') as inf_file:
            for file in inf_file:
                
                file_str = str(file)
                
                if MyHashtagsFilter in file_str[0:5]:
                    continue
                
                if (InfBaseName in file_str) and (Purpose_Have_Equalsign in file_str):
                    BASE_NAME_Str = file_str
                    
                if (InfFileGuid in file_str) and (Purpose_Have_Equalsign in file_str): 
                    FILE_GUID_Str = file_str 
                    break

        for UnitStr in BASE_NAME_Str:
            BASE_NAME_Clear_Str += UnitStr
            if UnitStr == '=':
                break

        UnitStr = ''

        for UnitStr in FILE_GUID_Str:
            FILE_GUID_Clear_Str += UnitStr
            if UnitStr == '=':
                break

        BASE_NAME_Str = BASE_NAME_Str.replace(BASE_NAME_Clear_Str, '')
        BASE_NAME_Str = BASE_NAME_Str.replace('\n', '')
        BASE_NAME_Str = BASE_NAME_Str.replace(' ', '')
        
        FILE_GUID_Str = FILE_GUID_Str.replace(FILE_GUID_Clear_Str, '')
        FILE_GUID_Str = FILE_GUID_Str.replace('\n', '')
        FILE_GUID_Str = FILE_GUID_Str.replace(' ', '')
        FILE_GUID_Str = InfTransformToUppercase.TransToUppercase(FILE_GUID_Str)

        with open((ClearlyDocument_Path + "\\" + "ClearlyDocument.txt"), 'a') as ClrDoc:
            ClrDoc.write('{:<60}{:<}\n'.format(FILE_GUID_Str[:38],'  '+BASE_NAME_Str))
            
    except:
        pass
                


