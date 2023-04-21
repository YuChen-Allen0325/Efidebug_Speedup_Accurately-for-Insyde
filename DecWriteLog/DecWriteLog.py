from GuidTransform import Guidfilter


def DecWriteLog(InputFileName, ClearlyDocument_Path):
    
    DecGuid = 'Guid'
    BracketInStr = '{'
    Guid_And_Name_Str = ''
    EqualSign = '='
    Hashtags = '#'

    try:
        with open(InputFileName, 'r') as dec_file:    
            
            for line_by_line in dec_file:
                
                InitialFlag = False
                Guid_Str = ''
                Name_Str = ''    
                line_by_line = str(line_by_line)
                
                if (DecGuid in line_by_line) and (EqualSign in line_by_line):
                    if (len(line_by_line) > 60) and (BracketInStr in line_by_line):
                        if Hashtags not in line_by_line[0:5]:
                            Guid_And_Name_Str = line_by_line[:]                    
                            
                            for UnitChar in Guid_And_Name_Str:
                                if InitialFlag == True:
                                    Guid_Str += UnitChar
                                if UnitChar == '=':
                                    InitialFlag = True
                            
                            Guid_Str = Guid_Str.replace('\n', '')
                            Guid_Str = Guidfilter.FromMessGuidtoCleanGuid(Guid_Str)
                            Guid_Str = Guid_Str.replace(' ', '')
                            
                            for UnitChar2 in Guid_And_Name_Str:
                                if UnitChar2 == '=':
                                    break
                                Name_Str += UnitChar2
                            
                            with open((ClearlyDocument_Path + "\\" + "ClearlyDocument.txt"), 'a') as ClrDoc:
                                ClrDoc.write('{:<60}{:<}\n'.format(Guid_Str[:38], Name_Str))
    except:
        pass
