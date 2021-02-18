# Instruction to run Auto Tests (Headless)

Install Python version (I used 3.8.6)"

Add Python to PATH" when asked

Open terminal go to root folder of the project and execute following command
to install all packages required to run the python tests

Check if pip is installed by pip help

If not, Download get-pip.py save to the root of the project.

Then -   
python get-pip.py"

Add pip to path" when asked.

Then -

pip install -r pip_requirements.txt

If you are still in root folder of the project now run-

pytest test_lingoda -v --html=./testreport.html

Reports following the test can be found in the same directory as the testreport.html. Open with Chrome/Firefox to review test results.