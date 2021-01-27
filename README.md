# Uranus is a python library.

## 1. upload and install command

python setup.py sdist bdist_wheel
python -m twine upload --repository testpypi dist/*
pip install --index-url https://test.pypi.org/simple/ plutopy
pip install --upgrade --index-url https://test.pypi.org/simple/ plutopy

python setup.py sdist bdist_wheel
python -m twine upload dist/*
pip install plutopy
pip install --upgrade plutopy

## ATTENTION!!!
1. Each package or subpackage must has __init__.py.
2. Setup.py's install_requires need set.
3. Increase version before upload.
4. Exclude package in setup.py, exclude files in MANIFEST.in
