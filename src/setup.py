from distutils.core import setup, Extension
import setup_translate

plugdir = '/usr/lib/enigma2/python/Plugins/Extensions/EPGImport'

dreamcrc = Extension('EPGImport/dreamcrc',
                    sources = ['dreamcrc.c'])

pkg = 'EPGImport'
setup (name = 'enigma2-plugin-extensions-xmltvimport',
       version = '0.9.12',
       description = 'C implementation of Dream CRC32 algorithm',
       packages = [pkg],
       package_data = {pkg: ['*.png', 'locale/*/LC_MESSAGES/*.mo']},
       ext_modules = [dreamcrc],
       cmdclass = setup_translate.cmdclass, # for translation
)
