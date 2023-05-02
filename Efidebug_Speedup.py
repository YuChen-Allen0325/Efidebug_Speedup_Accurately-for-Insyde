
import os
import linecache
import shutil
from InfWriteLog import InfWriteLog as InfWL
from DecWriteLog import DecWriteLog as DecWL
from CHWriteLog import CHWriteLog as CHWL
from GuidXrefTransform import TransformToUppercaseAll as TransGuidXref



counter = 0
quick_analysis = False

while (1) :
    if counter >= 1:
        print("your input illegal !")
    
    optional_input = input("Do you want to quick analysis? If you want, you will not get the ClearlyDocument!   please input Y/N : ")
    optional_input = str(optional_input)

    if optional_input == 'Y':
        quick_analysis = True
        break
    
    if optional_input == 'N':
        break
    
    if optional_input == 'y':
        quick_analysis = True
        break
    
    if optional_input == 'n':
        break
    
    counter += 1

directory = input("please input your work directory path (e.g. : C:\ADL_N_Setup): ")
directory = str(directory)
logfile_name = input("please input your log file name (include file extension  e.g. : putty.log): ")
logfile_name = str(logfile_name)
XrefExistFlag = False
Make_Sure_Execute_Flag = True
Bracket = '{'
extension_c = '.c'
extension_h = '.h'
extension_inf = '.inf'
extension_dec = '.dec'
Have_GUID_Ref_file = '\Guid.xref'
Guid_Ref = ''                      #Guid.xref path
ScanCH = '\Build'
exclude_dirs = ["Conf","BaseTools"]
GuidXrefGuid = ''
GuidXrefName = ''
ReplaceLineDic = {}               # String:line
ReplaceLineCounter = 0
ReplaceString = ''
ClearlyDocumentGuid = ''
ClearlyDocumentName = ''
ClearlyDocumentString = ''
ClearlyDocumentString_list = []
ClearlyDocumentString_set  = set()
GuidXrefDic = {}
GuidXrefDic_Conflict = {}
ClrDoc_Name = ''
UnUsedConflictGuidDic = {}
Conflict_GUID_Str = ''

original_file = directory + "\\" + logfile_name
new_file = directory + "\\" + "new_" +logfile_name
check_new_file_exist = os.path.exists(new_file)



if os.path.exists((directory + "\\" + logfile_name)) and (check_new_file_exist == False):
      
    #--------------------------------- Create ClearlyDocument.txt --------------------------------
    
    try:
        
        if os.path.exists((directory + "\\" + "Guid.xref")):
            Guid_Ref = directory + "\\" + "Guid.xref"
            XrefExistFlag = True
        
        if os.path.exists((directory + "\\" + "ClearlyDocument.txt")):
            os.remove((directory + "\\" + "ClearlyDocument.txt"))
        
        if quick_analysis == False:
            print("\nCreate ClearlyDocument.txt...")
        else:
            print("\n")
            
            
        if not((XrefExistFlag == True) and (quick_analysis == True)):
            for root, dirs, files in os.walk(directory):
                dirs[:] = [d for d in dirs if d not in exclude_dirs]
                
                for filename in files:
                    
                    if XrefExistFlag == False:
                        if (Have_GUID_Ref_file in (os.path.join(root, filename))) and (ScanCH in (os.path.join(root, filename))):
                            Guid_Ref = os.path.join(root, filename)   # Get Guid.xref path
                        
                    if quick_analysis == False:
                        if filename.endswith(extension_inf):
                            InfWL.InfWriteLog(os.path.join(root, filename), directory)
                            
                        elif filename.endswith(extension_dec):
                            DecWL.DecWriteLog(os.path.join(root, filename), directory)                      
                            
                        elif (filename.endswith(extension_c)) and (ScanCH not in root):
                            CHWL.CHWriteLog(os.path.join(root, filename),directory)            
                            
                        elif (filename.endswith(extension_h)) and (ScanCH not in root):
                            CHWL.CHWriteLog(os.path.join(root, filename),directory)
                            
                        else:
                            continue
    
        if Guid_Ref == '':
            Make_Sure_Execute_Flag = False
            
        shutil.copy(original_file, new_file)   # copy original log file to new log file
            
    except:
        pass
        
    #---------------------------------- Compare Guid.xref & log file --------------------------------------------
    try:
        if (Make_Sure_Execute_Flag == True):
            
            if os.path.exists((directory + "\\" + "Conflict_GUID.txt")):
                os.remove((directory + "\\" + "Conflict_GUID.txt"))
                
            print("Guid.xref compare with log file...")    
                    
            with open(Guid_Ref, 'r') as GuidXref:
                for GuidXref_Row in GuidXref:
                    
                    GuidXref_Row = str(GuidXref_Row)
                    GuidXrefGuid = GuidXref_Row[0:36]
                    GuidXrefGuid = TransGuidXref.AllGuidXrefUppercase(GuidXrefGuid)
                    GuidXrefName = GuidXref_Row[37:]
                    ReplaceLineCounter = 0
                    
                    with open(new_file, 'r') as PuttyLog:
                        for PuttyLog_Row in PuttyLog:
                            
                            PuttyLog_Row = str(PuttyLog_Row)
                            
                            if GuidXrefGuid in PuttyLog_Row:
                                
                                ReplaceString = PuttyLog_Row
                                ReplaceString = ReplaceString.replace(GuidXrefGuid, GuidXrefName)
                                ReplaceString = ReplaceString.replace('\n','')
                                ReplaceLineDic[ReplaceLineCounter] = (ReplaceString + '\n')
                                
                            ReplaceLineCounter += 1
        

            with open(new_file, 'r') as PuttyLog_R:
                lines = PuttyLog_R.readlines()
                
            for line_number, new_content in ReplaceLineDic.items():
                lines[line_number] = new_content
                
            with open(new_file, 'w') as PuttyLog_W:
                PuttyLog_W.writelines(lines)
          
            
        if (ReplaceLineDic == {}):
            print('Your Build folder not exist Guid.xref to compare with log file !!')   
                 
    #--------------------------------------- ClearlyDocument orderliness -----------------------------------------

        if quick_analysis == False:
            
            print("Organize ClearlyDocument.txt file...")
            
            with open((directory + "\\" + "ClearlyDocument.txt"), 'r') as ClrDoc:
                for Unit_ClrDoc in ClrDoc:
                    
                    if (Unit_ClrDoc == '') or (Unit_ClrDoc == ' '):
                        continue
                    
                    ClearlyDocumentGuid = Unit_ClrDoc[0:36]
                    
                    if (Bracket in ClearlyDocumentGuid):
                        continue
                    
                    ClearlyDocumentName = Unit_ClrDoc[50:]
                    ClearlyDocumentName = ClearlyDocumentName.replace(' ','')
                    
                    ClearlyDocumentString = ClearlyDocumentGuid + ' ' + ClearlyDocumentName
                    
                    ClearlyDocumentString_list.append(ClearlyDocumentString)
                    
                ClearlyDocumentString_set = set(ClearlyDocumentString_list)
                ClearlyDocumentString_list = list(ClearlyDocumentString_set)
                
            os.remove((directory + "\\" + "ClearlyDocument.txt"))        
            
            with open((directory + "\\" + "ClearlyDocument.txt"), 'a') as ClrDoc:
                
                for ClearlyDocumentString_list_Row in range(len(ClearlyDocumentString_list)):
                    ClrDoc.write(ClearlyDocumentString_list[ClearlyDocumentString_list_Row])


    # --------------------------- Guid.xref compare with ClearlyDocument.txt to get Conflict_GUID.txt -----------------------------------

        if (ReplaceLineDic != {}):
            
            print("Create Conflict_GUID.txt...")
            
            with open(Guid_Ref, 'r') as GuidXref:
                for GuidXref_Row in GuidXref:

                    GuidXref_Row = str(GuidXref_Row)
                    GuidXrefGuid = GuidXref_Row[0:36]
                    GuidXrefGuid = TransGuidXref.AllGuidXrefUppercase(GuidXrefGuid)
                    GuidXrefName = GuidXref_Row[37:]
                    GuidXrefName = GuidXrefName.replace('\n','')                    
                    
                    if GuidXrefGuid in GuidXrefDic.keys():
                        GuidXrefDic[GuidXrefGuid].append(GuidXrefName)
                    else:
                        GuidXrefDic[GuidXrefGuid] = [GuidXrefName]
                    
                for GuidXrefDic_Guid, GuidXrefDic_NameList in GuidXrefDic.items():
                    if len(GuidXrefDic_NameList) > 1:
                        GuidXrefDic_Conflict[GuidXrefDic_Guid] = GuidXrefDic_NameList  #conflict dic (used)
                        
            if quick_analysis == False:
                for GuidXrefDic_Conflict_Guid, GuidXrefDic_Conflict_NameList in GuidXrefDic_Conflict.items():
                    
                    with open((directory + "\\" + "ClearlyDocument.txt"), 'r') as ClrDoc:
                        for Unit_ClrDoc in ClrDoc:
                            
                            if GuidXrefDic_Conflict_Guid in Unit_ClrDoc:
                            
                                ClrDoc_Name = Unit_ClrDoc[37:]
                                ClrDoc_Name = ClrDoc_Name.replace('\n','')

                                if ClrDoc_Name not in GuidXrefDic_Conflict_NameList:
                                    
                                    if GuidXrefDic_Conflict_Guid in UnUsedConflictGuidDic.keys():           
                                        UnUsedConflictGuidDic[GuidXrefDic_Conflict_Guid].append(ClrDoc_Name)   #conflict dic (unused)
                                        
                                    else:
                                        UnUsedConflictGuidDic[GuidXrefDic_Conflict_Guid] = [ClrDoc_Name]
                                    
                 
            with open((directory + "\\" + "Conflict_GUID.txt"), 'a') as CftDoc:
                for GuidXrefDic_Conflict_Guid, GuidXrefDic_Conflict_NameList in GuidXrefDic_Conflict.items():
                    Conflict_GUID_Str = ''
                    Conflict_GUID_Str = GuidXrefDic_Conflict_Guid + '   ' + 'used: ' + str(GuidXrefDic_Conflict_NameList)
                    
                    if GuidXrefDic_Conflict_Guid in UnUsedConflictGuidDic.keys():
                        Conflict_GUID_Str += '   ||   '+'unused: ' + str(UnUsedConflictGuidDic[GuidXrefDic_Conflict_Guid])
                     
                    Conflict_GUID_Str += '\n' 
                        
                    CftDoc.write(Conflict_GUID_Str)
                
    except:
        pass

else:
    print("Your log file not exist or you should rename your log file!")
