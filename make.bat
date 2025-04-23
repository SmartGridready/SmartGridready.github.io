@ECHO OFF

REM Command file for Sphinx documentation
REM Call using: make.bat <target>
REM Example: make.bat html

set SOURCEDIR=source
set BUILDDIR=build

if not defined SPHINXBUILD (
	goto set_sphinxbuild
)
else (
	goto begin
)

:set_sphinxbuild
set SPHINXBUILD=sphinx-build

:begin
pushd %~dp0

if "%1" == "" goto help

%SPHINXBUILD% >NUL 2>NUL
if errorlevel 9009 (
	echo.
	echo.The 'sphinx-build' command was not found. Make sure you have Sphinx
	echo.installed, then set the SPHINXBUILD environment variable to point
	echo.to the full path of the 'sphinx-build' executable. Alternatively you
	echo.may add the Sphinx directory to PATH.
	echo.
	echo.If you don't have Sphinx installed, grab it from
	echo.http://sphinx-doc.org/
	exit /b 1
)

%SPHINXBUILD% -M clean %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%

rd /s /q docs

%SPHINXBUILD% -M %1 %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%

xcopy %BUILDDIR%\html\* docs /E /I /Y

goto end

:help
%SPHINXBUILD% -M help %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%

:end
popd
