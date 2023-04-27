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

![1682582303265](https://user-images.githubusercontent.com/94295939/234798334-46c5b7f8-5062-4d91-aa0a-5304a42ca64e.jpg)

![1682582385630](https://user-images.githubusercontent.com/94295939/234798368-27d3b1da-7a4f-4b8e-bbbc-f65cc85613cf.jpg)


3. executed process

![1682579548962](https://user-images.githubusercontent.com/94295939/234790140-e05da240-3f35-4446-aef5-a122137dcc04.jpg)

![1682579555230](https://user-images.githubusercontent.com/94295939/234790206-16dc0806-7abc-41cf-b010-7483c6ff84e3.jpg)

4. result of production file

![DEMO4](https://user-images.githubusercontent.com/94295939/234796494-1df9fe23-9f70-4d69-998e-68217812d67c.jpg)

