from setuptools import setup

setup(name='sparklez',
      version='0.1.3',
      description='Npm & Rubygem search',
      url='http://github.com/nickforsman/sparklez',
      author='Niclas Forsman',
      author_email='n.forsman@hotmail.com',
      license='MIT',
      entry_points={
          'console_scripts':['sparklez=sparklez.sparklez:main'],
      },
      packages=['sparklez'],
      install_requires=[
          'click',
          'requests',
          'inquirer',
      ],
      zip_safe=False)
