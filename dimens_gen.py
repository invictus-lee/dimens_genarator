import xml.dom.minidom
import os

dom = xml.dom.minidom.parse('dimens.xml')
resources = dom.documentElement
dimens = resources.getElementsByTagName('dimen')

sw480_outstr = "<resources>\n"
sw600_outstr = "<resources>\n"
sw720_outstr = "<resources>\n"
sw820_outstr = "<resources>\n"

if os.path.exists('../values-sw480dp-land'):
	pass
else :
	os.makedirs(r'../values-sw480dp-land')


if os.path.exists('../values-sw600dp-land'):
	pass
else :
	os.makedirs(r'../values-sw600dp-land')


if os.path.exists('../values-sw720dp-land'):
	pass
else :
	os.makedirs(r'../values-sw720dp-land')

if os.path.exists('../values-sw820dp'):
	pass
else :
	os.makedirs(r'../values-sw820dp')


sw480_outfile = open('../values-sw480dp-land/dimens.xml','w') 
sw600_outfile = open('../values-sw600dp-land/dimens.xml','w') 
sw720_outfile = open('../values-sw720dp-land/dimens.xml','w') 
sw820_outfile = open('../values-sw820dp/dimens.xml','w') 


for dimen in dimens:
	name = dimen.getAttribute('name')
	value_all = str(dimen.firstChild.data)
	value =float( filter(str.isdigit, value_all))
	ext =  filter(str.isalpha, value_all)
	sw480_outstr = sw480_outstr + "\t" + '<dimen name="'+name+'">'+str(value*(480.0/800.0))+ext+'</dimen>\n'
	sw600_outstr = sw600_outstr + "\t" + '<dimen name="'+name+'">'+str(value*(600.0/800.0))+ext+'</dimen>\n'
	sw720_outstr = sw720_outstr + "\t" +'<dimen name="'+name+'">'+str(value*(720/800.0))+ext+'</dimen>\n'
	sw820_outstr = sw820_outstr + "\t" +'<dimen name="'+name+'">'+str(value*(820/800.0))+ext+'</dimen>\n'

sw480_outstr += '</resources>\n'
sw600_outstr += '</resources>\n'
sw720_outstr += '</resources>\n'
sw820_outstr += '</resources>\n'

sw480_outfile.write(sw480_outstr)
sw480_outfile.close()
sw600_outfile.write(sw600_outstr)
sw600_outfile.close()
sw720_outfile.write(sw720_outstr)
sw720_outfile.close()
sw820_outfile.write(sw820_outstr)
sw820_outfile.close()

print '----------sw480------------'
print sw480_outstr

print '----------sw600------------'
print sw600_outstr

print '----------sw720------------'
print sw720_outstr

print '----------sw820------------'
print sw820_outstr

print '----success----' 

