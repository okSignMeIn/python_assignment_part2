pip freeze > requirements.txt

# On another system, you can use to install the project specific dependencies by

pip install -r requirements.txt

# and for using conda environment.yml

conda env export > environment.yml

# For installing the project dependencies

conda env create -f environment.yml

