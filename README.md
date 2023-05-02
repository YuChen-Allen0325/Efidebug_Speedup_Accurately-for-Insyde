# User's Guide

The purpose of project is creating a file that list all GUID and name in work directory and Use "Guid.xref" compare with "putty.log".

If the GUID in "Guid.xref" occurs in "putty.log", then replace it to the corresponded name.



"putty.log = your_log_file_name"

".exe file is in the dist directory"

"work directory = root directory of Insyde code base"

"This program only use to after your work directory efidebug build, so your work directory must have "Build" folder"

"The file collect the some special GUID defined in c or h file are not accurately"



    1.Path is your work directory (need absolute path)

    2.You have to input your_log_file_name and extension, then you should put the file in your work directory

    3.It may requires a few minute to execute

    4.The new files created are called "ClearlyDocument", "Conflict_GUID", "new_your_log_file_name"

    5.If the executed program is canceled suddenly. You may input error or you should rename your log file
  
  
  
In ClearlyDocument, the file lists all GUID in the work directory (Summary table of GUIDs)


In Conflict_GUID, the file lists all of different name used the same GUID.
"used" : You can find out in both of "Guid.xref" and "ClearlyDocument".
"unused" : You can only find out in the "ClearlyDocument"


In new_your_log_file_name, the file generated after your_log_file_name replaced GUID to corresponded name


"Don't name your file to "ClearlyDocument" or "Conflict_GUID" before running "Efidebug_Speedup.exe", or there will be overlayed !"

-------------------------------------------------------------------------------------------------------------------------------------------

Demonstration as below:

1. original file and work directory

![DEMO1](https://user-images.githubusercontent.com/94295939/234796530-d1d11cfe-870d-41e1-a7e3-b4124081791a.jpg)

2. input requirements

This option up to user require (choose 'Y', not produce Summary table of GUIDs)!
![050201](https://user-images.githubusercontent.com/94295939/235560095-bf5c9e99-2e7d-4cd8-b822-60144ec95f40.jpg)

![050202](https://user-images.githubusercontent.com/94295939/235560153-52cf1547-5478-4e29-aa2a-d07d6975335f.jpg)

![050203](https://user-images.githubusercontent.com/94295939/235560160-88782630-4fc9-45d9-a223-6ee23409eb77.jpg)



3. result of production file

if choose 'Y':
![050204](https://user-images.githubusercontent.com/94295939/235560235-5f5915ac-95b2-4f61-953b-792639a1ab49.jpg)

if choose 'N':
![050205](https://user-images.githubusercontent.com/94295939/235560284-22107074-41e5-4dad-9350-9ba2aad25c28.jpg)

