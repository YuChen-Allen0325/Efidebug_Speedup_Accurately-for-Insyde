from GuidTransform import Guidfilter

def CHWriteLog(InputFileName, ClearlyDocument_Path):
    
    CHAllGuidName = {} # Guid:Name

    EFI_GUID_Str = 'EFI_GUID'
    GuidStr = 'Guid'
    EqualSign = '='
    Bracket = '{'
    JudgeRef = '0x'  
    HaveIf = 'if'

    StringStorage1 = ''
    StringStorage2 = ''
    MessGuidNameStr = ''

    with open(InputFileName, 'r') as CHRead:
        
        for CHRead_by_line in CHRead:
            
            NameStr = ''
            GuidStr = ''
            CommaCounter = 0 # 10
            xCounter = 0 # 11            
            CHRead_by_line = str(CHRead_by_line)
            CHRead_by_line = CHRead_by_line.replace(' ', '')
            StringStorage1 = CHRead_by_line
            PureNameFlag = True
            MessGuidFlag = False
            
            
            if (EFI_GUID_Str in CHRead_by_line) and (GuidStr in CHRead_by_line):
                if (EqualSign in CHRead_by_line) and (JudgeRef in CHRead_by_line):
                    if (len(CHRead_by_line) > 40) and (Bracket in CHRead_by_line):

                        MessGuidNameStr = CHRead_by_line
                        MessGuidNameStr = MessGuidNameStr.replace(EFI_GUID_Str,'')
                        MessGuidNameStr = MessGuidNameStr.replace('\n', '')
                        
                        for Unit_MessGuidNameStr in MessGuidNameStr:
                            if Unit_MessGuidNameStr == '=':
                                PureNameFlag = False
                                MessGuidFlag = True
                                
                            if PureNameFlag == True:
                                NameStr += Unit_MessGuidNameStr
                            
                            if MessGuidFlag == True:
                                GuidStr += Unit_MessGuidNameStr
                        
                        GuidStr = Guidfilter.FromMessGuidtoCleanGuid(GuidStr)
                        GuidStr = GuidStr.replace(' ', '')
                        GuidStr = GuidStr.replace('\n','')
                        GuidStr = GuidStr.replace('\\','')
                        
                        NameStr = NameStr.replace('const','')
                        NameStr = NameStr.replace('STATIC','')
                        NameStr = NameStr.replace('static','')
                        NameStr = NameStr.replace('/','')
                        NameStr = NameStr.replace('GLOBAL_REMOVE_IF_UNREFERENCED','')
                        
                        CHAllGuidName[GuidStr] = NameStr
                            
                        continue
            
            
            for UnitCHRead_by_line in CHRead_by_line:    
                if UnitCHRead_by_line == 'x':
                    xCounter += 1
                if UnitCHRead_by_line == ',':
                    CommaCounter += 1
                    
            if (xCounter == 11) and (CommaCounter == 10):
                MessGuidNameStr = StringStorage2 + StringStorage1
                if (EFI_GUID_Str in MessGuidNameStr) and (GuidStr in MessGuidNameStr):
                    if (EqualSign in MessGuidNameStr) and (JudgeRef in MessGuidNameStr):
                        if (len(MessGuidNameStr) > 40) and (Bracket in MessGuidNameStr): 
      
                            MessGuidNameStr = MessGuidNameStr.replace(EFI_GUID_Str,'')
                            MessGuidNameStr = MessGuidNameStr.replace('\n', '')
                            
                            for Unit_MessGuidNameStr in MessGuidNameStr:
                                if Unit_MessGuidNameStr == '=':
                                    PureNameFlag = False
                                    MessGuidFlag = True
                                    
                                if PureNameFlag == True:
                                    NameStr += Unit_MessGuidNameStr
                                
                                if MessGuidFlag == True:
                                    GuidStr += Unit_MessGuidNameStr
                            
                            GuidStr = Guidfilter.FromMessGuidtoCleanGuid(GuidStr)
                            GuidStr = GuidStr.replace(' ', '')
                            GuidStr = GuidStr.replace('\n','')
                            GuidStr = GuidStr.replace('\\','')


                            NameStr = NameStr.replace('const','')
                            NameStr = NameStr.replace('STATIC','')
                            NameStr = NameStr.replace('static','')
                            NameStr = NameStr.replace('/','')
                            NameStr = NameStr.replace('\n','')
                            NameStr = NameStr.replace('GLOBAL_REMOVE_IF_UNREFERENCED','')
                                                        
                            CHAllGuidName[GuidStr] = NameStr
        
            StringStorage2 = CHRead_by_line
            
    with open((ClearlyDocument_Path + "\\" + "ClearlyDocument.txt"), 'a') as ClrDoc:
        for PureGuid, PureName in CHAllGuidName.items():
            PureGuid = PureGuid + ' ' + ' '
            ClrDoc.write('{:<60}{:<}\n'.format(PureGuid[:38], PureName))