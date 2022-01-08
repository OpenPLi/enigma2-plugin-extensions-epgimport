from __future__ import absolute_import, print_function

import gettext

from Components.Language import language
from Tools.Directories import SCOPE_PLUGINS, resolveFilename

PluginLanguageDomain = "EPGImport"
PluginLanguagePath = "Extensions/EPGImport/locale"


def localeInit():
    gettext.bindtextdomain(PluginLanguageDomain, resolveFilename(SCOPE_PLUGINS, PluginLanguagePath))


def _(txt):
    t = gettext.dgettext(PluginLanguageDomain, txt)
    if t == txt:
        print("[" + PluginLanguageDomain + "] fallback to default translation for ", txt)
        t = gettext.gettext(txt)
    return t


localeInit()
language.addCallback(localeInit)
