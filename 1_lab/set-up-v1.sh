#!/bin/bash
# Заголовок вверху називається shebang
name="2_pro"
cd $name
echo "Start creating virtual env in PATH: $(pwd)" # Це команда покаже де ми зараз знаходимось, у якій папці
python -m venv ./venv_$name # Створення середовища
echo "VENV created. There are newxt files/folders:"
ls
source ./venv_$name/Scripts/activate # Активація
pip install -r requirements.txt # інсталяція бібліотек
deactivate
echo "Done"