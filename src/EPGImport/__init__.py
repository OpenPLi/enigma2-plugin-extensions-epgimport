from __future__ import absolute_import, print_function
from Components.Language import language
from Tools.Directories import resolveFilename, SCOPE_PLUGINS
from gettext import bindtextdomain, dgettext, gettext

PluginLanguageDomain = "EPGImport"
PluginLanguagePath = "Extensions/EPGImport/locale"


def localeInit():
	bindtextdomain(PluginLanguageDomain, resolveFilename(SCOPE_PLUGINS, PluginLanguagePath))


def _(txt):
	if dgettext(PluginLanguageDomain, txt):
		return dgettext(PluginLanguageDomain, txt)
	else:
		print("%s fallback to default translation for %s" % (PluginLanguageDomain, txt))
		return gettext(txt)


localeInit()
language.addCallback(localeInit)
