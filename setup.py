from setuptools import setup, find_packages

setup(name='twisted-django1.5-autobahn-on-openshift', version='1.0',
      packages=find_packages(),
      description='Example application that allow to run twisted, django and websocket on openshift',
      author='lodatol', author_email='lodato.luciano@gmail.com',
      url='http://www.python.org/sigs/distutils-sig/',
      dependency_links=[
          "http://pypi.python.org/pypi/Twisted/",
          "http://pypi.python.org/pypi/autobahn",
          "http://pypi.python.org/pypi/Django/"
      ],
      install_requires=['Django==1.5.1',
                        'Twisted',
                        'Autobahn'],
      )
