import os, psutil
import codecs

ram_size = 500 * 1024
disk_size = 500 * 1024

def ram_usage():
	process = psutil.Process(os.getpid())
	return process.memory_info().rss / 1024

def disk_usage():
	disk = 0
	start_path = '.'
	for path, dirs, files in os.walk(start_path):
		for f in files:
			fp = os.path.join(path, f)
			disk += os.path.getsize(fp)
	return disk / 1024

def ram_usage_p():
	return ram_usage() / ram_size

def disk_usage_p():
	return disk_usage() / disk_size
	
def circle(size, big='', color=''):
	return '<div class="dark '+big+' '+color+' c100 pPSIZE center"><span>PSIZE%</span><div class="slice"><div class="bar"></div><div class="fill"></div></div></div>'.replace('PSIZE', str(size)[:5])

def html_stats(request):
	s = codecs.open('stats_header.html', 'r', 'utf-8').read()
	if request:
		return s + '<center><br><br><table style=" width:75%;margin-top:10%;"><tr>RAM</tr><tr>'+circle(ram_usage_p()*100)+'</tr><br><tr>DISK</tr><tr>'+circle(disk_usage_p()*100, 'green')+'</tr></table></center>'
	else:
		return s + '<center><table style=" width:75%;margin-top:10%;"><tr><th>RAM</th><th>DISK</th></tr><tr><td>'+circle(ram_usage_p()*100, big='big')+'</td><td>'+circle(disk_usage_p()*100, big='big', color='green')+'</td></tr></table></center>'