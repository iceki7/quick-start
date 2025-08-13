@echo off
setlocal

@REM 留下一个文件夹里所有0 1结尾的ply

 
set "source_dir=."
set "dest_dir=%source_dir%\keep"
 
if not exist "%dest_dir%" (
    mkdir "%dest_dir%"
)
 
for %%f in ("%source_dir%\*0.ply") do (
    move "%%f" "%dest_dir%"
)

for %%f in ("%source_dir%\*1.ply") do (
    move "%%f" "%dest_dir%"
)
 
endlocal
echo finished!!
pause