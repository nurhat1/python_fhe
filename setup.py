from setuptools import setup

if __name__ == '__main__':
    setup(name='he',
          version='1.0',
          description='Python homomorphic system',
          author='Konstantin Malysh',
          packages=['he'],
          classifiers=[
              'Operating System :: OS Independent',
              'Programming Language :: Python',
              'Programming Language :: Python :: 3.4',
              'Programming Language :: Python :: 3.5',
              'Topic :: Security :: Cryptography',
          ],
          install_requires=[
              'pyasn1 >= 0.1.3',
          ],

          )
