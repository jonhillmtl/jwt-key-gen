from distutils.core import setup

setup(name='jwt_key_gen',
      version='0.1',
      description='Produces a JSON Web Token key',
      author='Jon Hill',
      author_email='jon@jonhill.ca',
      url='https://github.com/jonhillmtl/jwt-key-gen',
      license='MIT',
      entry_points={
          'console_scripts': [
              'jwt_key_gen=jwt_key_gen:main',
          ],
      },
      packages=['jwt_key_gen'],
      install_requires=['jwcrypto', 'termcolor']
)
