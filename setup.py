from setuptools import setup, find_packages

setup(
    name='ml_rest_api',
    version='0.1.0',
    description='A RESTful API to return predictions from a trained ML model, built with Python 3 and Flask-RESTplus',
    url='https://github.com/jgbustos/ml_rest_api',
    author='Jorge Garcia de Bustos',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Flask'
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    keywords='python3 flask-restplus machine-learning rest-api',

    packages=find_packages(),

    install_requires=['Flask==1.0.2',
                      'flask-restplus==0.12.1',
                      'numpy==1.15.2',
                      'scipy==1.1.0',
                      'pandas==0.23.4',
                      'scikit-learn==0.20.0',
                      'lightgbm==2.2.1',
                      'tensorflow==1.11.0',
                      'keras==2.2.4',],
)
