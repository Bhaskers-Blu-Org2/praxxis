@ECHO OFF
@SETLOCAL
SET RUNNER="../src/mtool/app.py"
CALL python %RUNNER% %1 %2 %3 %4
