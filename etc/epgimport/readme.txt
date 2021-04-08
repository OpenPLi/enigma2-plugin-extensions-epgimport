XMLTV Importer

This software is released under the GPLv2 license.

Providers should check out the .xml files in the /etc/epgimport
directory for information on creating your own source.

Users need not read this, just configure it from the plugins.

Special thanks go to:

'rytec' for providing the XMLTV data
'oudeis' and 'arnoldd' for the initial plugin
'Panagiotis Malakoudis' for his tips for UTF-8
The PLi team for putting up with me
All the sat4all.com folks who contributed

Request:

Some channels share the same service reference but have multiple languages available for there EPG.
Today it is always the latest loaded EPG data file that will push its language and you have no easy control on this download order.
The current solution is to totally exclude the downloading of an EPG package file but this not always possible (for exemple news channels are all in the same file).

<!-- DK --> <!-- 0.8W --> <channel id=" DiscoveryHD.dk "> 1:0:19:1006:29:46:E080000:0:0:0: </channel><!--  Discovery HD Showcase  -->
<!-- FI --> <!-- 0.8W --> <channel id=" DiscoveryHD.fi "> 1:0:19:1006:29:46:E080000:0:0:0: </channel><!--  Discovery HD Showcase  -->
<!-- HRV --> <!-- 0.8W --> <channel id=" DiscoveryHDShowcase.rs "> 1:0:19:1006:29:46:E080000:0:0:0: </channel><!--  Discovery HD Showcase  -->
<!-- HU --> <!-- 0.8W --> <channel id=" DiscoveryHDShowcase.hu "> 1:0:19:1006:29:46:E080000:0:0:0: </channel><!--  Discovery HD Showcase  -->
<!-- NO --> <!-- 0.8W --> <channel id=" DiscoveryChannel.no "> 1:0:19:1006:29:46:E080000:0:0:0: </channel><!--  Discovery HD Showcase  -->
<!-- SE --> <!-- 0.8W --> <channel id=" DiscoveryHDshowcase.se "> 1:0:19:1006:29:46:E080000:0:0:0: </channel><!--  Discovery HD Showcase  -->
<!-- SVN --> <!-- 0.8W --> <channel id=" DiscoveryHD.svn "> 1:0:19:1006:29:46:E080000:0:0:0: </channel><!--  HD Discovery Shovcase  -->

All the same service ref, but different language EPG attached.

It was requested to find a mechanism to filter out some specific or group of channel id.


Solution:

You can now create a file /etc/epgimport/channel_id_filter.conf

this file will containt one regular expression per line, a logical OR operation will be performed between every regular expression (regex) lines.
There are many tutorials about regex on the internet. But here is some basis for you:

. means any characters but only once
* means 0 or more characters
+ means 1 or more characters
\. means the dot itself (since . means any characters)
^ start of the string
$ means end of the string
.* will replace any characters

The filters are turned into lower case because the channel id are also always turned into lower case in EPGImport
So FR, Fr, fR will anyway be turned into: fr

So if you want to exclude every french channel id use
.*\.fr
This means any string ending by .fr will be filtered out

Remark:  
-> *\.fr is not a valid regex because * means that the preceding char should repeated several times but you don't specify any, so .* is the correct syntax. Remember . means any char but . only means only one time any char.
-> Invalid regex will simply be ignored (it will be mentionned in the EPGImport log) but this won't prevent the EPG loading.
-> Too wide regex will filter out more than you expect, for example if you define just .* you will have no EPG because everything will be filtered out. So use wildcard with caution. If you are not familiar with regex use the fixed syntax: ChannelIDName\.Extension


You can also specify the single channel id example:    discoveryhd\.dk   will only match the channel id="DiscoveryHD.dk" (remember the channel id is turned into lowercase).
If you decide to exclude all the .dk channel id you can simply specify:  .*\.dk

The filter will apply to every possible channels.xml files so once you define an exclusion it will be use globally. You can only control the filtering on the /etc/epgimport/custom_channels.xml file.
