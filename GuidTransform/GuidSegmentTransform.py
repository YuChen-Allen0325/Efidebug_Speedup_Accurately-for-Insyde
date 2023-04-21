def GetTheSegmentedGuid(Messguid,GuidString,SegmentNumber):
    StoreFlag = False
    Xcounter = 0
    CommaCounter = 0

    for UnitGuid in Messguid:
        if CommaCounter >= SegmentNumber:
            break
        
        if UnitGuid == 'x':
            Xcounter += 1
            StoreFlag = True
            continue
            
        if UnitGuid == ',':
            CommaCounter += 1
            StoreFlag = False

        if (StoreFlag == True) and (Xcounter >= SegmentNumber):
            GuidString += UnitGuid
            
    return GuidString


def RestoreLossZero(GuidString, StringLength):
    
    LossZeroCount = 0
    
    if (len(GuidString) < StringLength):
        
        LossZero = StringLength - len(GuidString)
        
        for LossZeroCount in range(LossZero):
            GuidString = '0'+GuidString
    
    return GuidString