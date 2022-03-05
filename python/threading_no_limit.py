#! python3
import time, requests, os, threading

def download_img(image_url):
  print('thread: ', threading.current_thread())
  img_data = requests.get(image_url).content
  filename = img_url.split('/')[5]+'.jpg'
  filepath = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', filename))
  with open(filepath, 'wb') as handler:
    handler.write(img_data)
    print(image_url, time.time())
    return filepath

img_urls = ['http://inews.gtimg.com/newsapp_bt/0/50023803t5fqil81/640', 
'http://inews.gtimg.com/newsapp_bt/0/50027k2eo4lqkn32/640', 
'http://inews.gtimg.com/newsapp_bt/0/500285icah5aknff/640', 
'http://inews.gtimg.com/newsapp_bt/0/5001re2tdg7r045f/640', 
'http://inews.gtimg.com/newsapp_bt/0/5001sihf6u0qg71b/640', 
'http://inews.gtimg.com/newsapp_bt/0/50027qg5ildail18/640', 
'http://inews.gtimg.com/newsapp_bt/0/5001rgsr10hb03a0/640', 
'http://inews.gtimg.com/newsapp_bt/0/50027gst6knakn7h/640', 
'http://inews.gtimg.com/newsapp_bt/0/5001rh61dijqkn94/640', 
'http://inews.gtimg.com/newsapp_bt/0/5001reamevgb03fr/640']

start_time = time.time()
print(start_time)

for img_url in img_urls:
	try:
		t = threading.Thread(target=download_img, args=(img_url, ))
		t.start()
	except Exception as e:
		print(e)

while threading.active_count() != 1:
  pass

print('total time: ', time.time()-start_time)
