cd your dir

pip install virtualenv

python3 -m venv env 

если не работает то : python -m venv env

cd env\Scripts

activate.bat


cd ..
cd ..

git clone https://github.com/cmyser/testovoe

cd show 

pip install -r requirements.txt

cd show_data

serializer.py
если не работает то : python serializer.py

python manage.py makemigrations
python manage.py makemigrations data_show

python manage.py migrate

python manage.py loaddata users
python manage.py loaddata posts

python manage.py createsuperuser 

python manage.py runserver 

if you dont see Traceback you win!


 
