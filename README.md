# radiomicsBug
bug for radiomics

description:
when run this code in python, like:

python test.py

the result is OK, the radiomics would calculate 129 features

However, after pyinstaller (double click on the GenerateExe.bat), run the dist/test/test.exe.
The radiomics would only calculate 22 features. 



the version of radiomics is 2.2.0
the version of pyinstaller is 3.5
os: win7
