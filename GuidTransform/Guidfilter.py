from . import GuidSegmentTransform, GuidTransformToUppercase

def FromMessGuidtoCleanGuid(Messguid):
    GuidString = ''

    GuidString1 = ''
    GuidString2 = ''
    GuidString3 = ''

    GuidString4 = ''
    UnitGuidString4Pattern1 = ''
    UnitGuidString4Pattern2 = ''

    GuidString5 = ''
    UnitGuidString5Pattern1 = ''
    UnitGuidString5Pattern2 = ''
    UnitGuidString5Pattern3 = ''
    UnitGuidString5Pattern4 = ''
    UnitGuidString5Pattern5 = ''
    UnitGuidString5Pattern6 = ''
    NewUnitGuidString5Pattern6 = ''

    GuidString1 = GuidSegmentTransform.GetTheSegmentedGuid(Messguid, GuidString1, 1)
    GuidString1 = GuidString1.replace(' ', '')
    GuidString1 = GuidSegmentTransform.RestoreLossZero(GuidString1, 8)
    GuidString1 = GuidTransformToUppercase.TransToUppercase(GuidString1)

            
    GuidString2 = GuidSegmentTransform.GetTheSegmentedGuid(Messguid, GuidString2, 2)
    GuidString2 = GuidString2.replace(' ', '')
    GuidString2 = GuidSegmentTransform.RestoreLossZero(GuidString2, 4)
    GuidString2 = GuidTransformToUppercase.TransToUppercase(GuidString2)
            
    GuidString3 = GuidSegmentTransform.GetTheSegmentedGuid(Messguid, GuidString3, 3)
    GuidString3 = GuidString3.replace(' ', '')
    GuidString3 = GuidSegmentTransform.RestoreLossZero(GuidString3, 4)
    GuidString3 = GuidTransformToUppercase.TransToUppercase(GuidString3)

    ## ------------------------------------------------------------------------------------

    UnitGuidString4Pattern1 = GuidSegmentTransform.GetTheSegmentedGuid(Messguid, UnitGuidString4Pattern1, 4)
    UnitGuidString4Pattern1 = UnitGuidString4Pattern1.replace(' ', '')
    UnitGuidString4Pattern1 = GuidSegmentTransform.RestoreLossZero(UnitGuidString4Pattern1, 2)
    UnitGuidString4Pattern1 = GuidTransformToUppercase.TransToUppercase(UnitGuidString4Pattern1)

    UnitGuidString4Pattern2 = GuidSegmentTransform.GetTheSegmentedGuid(Messguid, UnitGuidString4Pattern2, 5)
    UnitGuidString4Pattern2 = UnitGuidString4Pattern2.replace(' ', '')
    UnitGuidString4Pattern2 = GuidSegmentTransform.RestoreLossZero(UnitGuidString4Pattern2, 2)
    UnitGuidString4Pattern2 = GuidTransformToUppercase.TransToUppercase(UnitGuidString4Pattern2)

    GuidString4 = UnitGuidString4Pattern1 + UnitGuidString4Pattern2
                    
    ## --------------------------------------------------------------------------------------

    UnitGuidString5Pattern1 = GuidSegmentTransform.GetTheSegmentedGuid(Messguid, UnitGuidString5Pattern1, 6)
    UnitGuidString5Pattern1 = UnitGuidString5Pattern1.replace(' ', '')
    UnitGuidString5Pattern1 = GuidSegmentTransform.RestoreLossZero(UnitGuidString5Pattern1, 2)
    UnitGuidString5Pattern1 = GuidTransformToUppercase.TransToUppercase(UnitGuidString5Pattern1)    
                    
    UnitGuidString5Pattern2 = GuidSegmentTransform.GetTheSegmentedGuid(Messguid, UnitGuidString5Pattern2, 7)
    UnitGuidString5Pattern2 = UnitGuidString5Pattern2.replace(' ', '')
    UnitGuidString5Pattern2 = GuidSegmentTransform.RestoreLossZero(UnitGuidString5Pattern2, 2)
    UnitGuidString5Pattern2 = GuidTransformToUppercase.TransToUppercase(UnitGuidString5Pattern2)                   
                    
    UnitGuidString5Pattern3 = GuidSegmentTransform.GetTheSegmentedGuid(Messguid, UnitGuidString5Pattern3, 8)
    UnitGuidString5Pattern3 = UnitGuidString5Pattern3.replace(' ', '')
    UnitGuidString5Pattern3 = GuidSegmentTransform.RestoreLossZero(UnitGuidString5Pattern3, 2)
    UnitGuidString5Pattern3 = GuidTransformToUppercase.TransToUppercase(UnitGuidString5Pattern3)        

    UnitGuidString5Pattern4 = GuidSegmentTransform.GetTheSegmentedGuid(Messguid, UnitGuidString5Pattern4, 9)
    UnitGuidString5Pattern4 = UnitGuidString5Pattern4.replace(' ', '')
    UnitGuidString5Pattern4 = GuidSegmentTransform.RestoreLossZero(UnitGuidString5Pattern4, 2)
    UnitGuidString5Pattern4 = GuidTransformToUppercase.TransToUppercase(UnitGuidString5Pattern4)          
                    
    UnitGuidString5Pattern5 = GuidSegmentTransform.GetTheSegmentedGuid(Messguid, UnitGuidString5Pattern5, 10)
    UnitGuidString5Pattern5 = UnitGuidString5Pattern5.replace(' ', '')
    UnitGuidString5Pattern5 = GuidSegmentTransform.RestoreLossZero(UnitGuidString5Pattern5, 2)  
    UnitGuidString5Pattern5 = GuidTransformToUppercase.TransToUppercase(UnitGuidString5Pattern5)               
                    
    UnitGuidString5Pattern6 = GuidSegmentTransform.GetTheSegmentedGuid(Messguid, UnitGuidString5Pattern6, 11)
    UnitGuidString5Pattern6 = UnitGuidString5Pattern6.replace(' ', '')
    UnitGuidString5Pattern6 = GuidSegmentTransform.RestoreLossZero(UnitGuidString5Pattern6, 2)                  ## This data not clean            

    for UnitChar in UnitGuidString5Pattern6:
        if (UnitChar == ' ') or (UnitChar == '}'):
            break 
        NewUnitGuidString5Pattern6 += UnitChar

    NewUnitGuidString5Pattern6 = GuidSegmentTransform.RestoreLossZero(NewUnitGuidString5Pattern6, 2)
    NewUnitGuidString5Pattern6 = GuidTransformToUppercase.TransToUppercase(NewUnitGuidString5Pattern6) 
        
    GuidString5 = UnitGuidString5Pattern1 + UnitGuidString5Pattern2 + UnitGuidString5Pattern3 + UnitGuidString5Pattern4 + UnitGuidString5Pattern5 + NewUnitGuidString5Pattern6
        
    GuidString = GuidString1+ '-' + GuidString2 + '-' + GuidString3 + '-' + GuidString4 + '-' + GuidString5

    return GuidString