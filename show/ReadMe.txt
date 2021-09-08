cd your dir

pip install virtualenv

python -m venv env 



cd env\Scripts

activate.bat


cd ..
cd ..

git clone https://github.com/cmyser/testovoe

cd testovoe

cd show 

pip install -r requirements.txt

cd data_show

serializer.py
если не работает то : python serializer.py

cd ..

python manage.py makemigrations
python manage.py makemigrations data_show

python manage.py migrate

python manage.py loaddata users
python manage.py loaddata posts

python manage.py createsuperuser 

python manage.py runserver 

if you dont see Traceback you win!


 
