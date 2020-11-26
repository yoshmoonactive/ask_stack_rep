cd ask_stack_app
python setup.py sdist
cd dist
pip install ask_stack_app-1.0.0.tar.gz
cd ../..
python -m pytest