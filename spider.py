import urllib
import urllib2
import cookielib
import re
import time
import sys
import gzip
import StringIO

## Global Variable
GIRLID = 0
IMAGEID  = 0
    
    
## build request and return response
def request_url(url):
    try:      
        # set cookie which acquire from chrome
        cookie = '''HWFORUM_SESSION=b626shs9hddbrfm8crummh3bf2; hwsso_login=""; testcookie=1; lang=en; authmethod=authpwd; hwsso_uniportal=34-13-49-14-30-76-00-EE-AA-48-82-06-77-B8-26-DD-97-37-7D-DC-0A-E9-4B-41-29-A6-E6-36-F9-3E-14-8C-6B-98-0D-8A-40-42-94-8E-D2-7B-80-8F-F1-A3-48-AC-B3-FC-47-B0-1D-F7-F1-6E-92-47-F3-05-C6-41-EF-4F-7C-E6-30-FA-A0-8E-76-38-92-47-F3-05-C6-41-EF-4F-7C-E6-30-FA-A0-8E-76-38-92-47-F3-05-C6-41-EF-4F-CE-E6-02-D4-0E-66-66-9D; hwssotinter=D8-B8-9E-BF-49-76-C7-FC-44-E8-9A-4F-B5-BD-CC-D3; sid=28-22-9D-5F-FF-C0-84-9A-93-06-E5-CD-60-E0-35-A8-1D-DF-E2-2B-79-F2-DB-20; uid=92-54-60-48-B2-D0-C0-84-3B-99-30-4D-C1-22-B2-7F; cip=B6-80-14-77-A8-E5-60-52-29-62-5B-47-AA-DA-27-DF; cname=B6-80-14-77-A8-E5-60-52-29-62-5B-47-AA-DA-27-DF; sip=8C-C7-B6-98-58-B9-B6-60-85-16-EA-96-9C-B4-41-0C-BD-B0-89-4D-C4-54-80-37; logFlag=in; online_update=1374490177; hwssotinter3=24000577733231; TS_think_language=zh-cn'''
        # build up the http header
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookielib.CookieJar()))
        urllib2.install_opener(opener)
        req = urllib2.Request(url)
        req.add_header('Cookie', cookie)
        req.add_header('Connection', 'keep-alive')
        req.add_header('Cache-Control', 'no-cache')
        req.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.72 Safari/537.36')
        req.add_header('Accept-Encoding', 'gzip,deflate,sdch')
        
        # read gzip data, then unzip and return text
        content = urllib2.urlopen(req).read()
        compressedstream = StringIO.StringIO(content) 
        gzipper = gzip.GzipFile(fileobj=compressedstream) 
        text = gzipper.read()
        return text
        
    except IOError:
        print 'problem reading page :', url

        
## retrieve xzzc page and analyze every post url
def retrieve_posts(url):
    text = request_url(url)
    if len(text) > 0:
        posts = re.findall(r'<span\sclass=\"pr20\"><a[\s\n]*href=\"(.*)\"\stitle', text)
        metafile = open('meta\girldb.txt', 'a')
        for post in posts:
            global GIRLID
            GIRLID += 1
            print '\n'
            print 'post :',post
            '''
            GIRL Metafile Structure:
                ID
                PostURL
            '''
            metafile.write(str(GIRLID)+',')
            metafile.write(post+',')
            metafile.write(str(0)+'\n')
            retrieve_imgs(post)
        


    
    
## retrieve post page and analyze img url
def retrieve_imgs(url):       
    text = request_url(url)
    if len(text) > 0:
        imgs = re.findall(r'<img data-ks-lazyload=\"(.*)\"\sonclick', text)
        print "images :",imgs
        metafile = open('meta\imgdb.txt', 'a') 
        for img in imgs:
            global IMAGEID
            global GIRLID
            IMAGEID+=1
            '''
            GIRL Metafile Structure:
                IMAGEID
                ImageURL
                GIRLID
            '''
            metafile.write(str(IMAGEID)+',')
            metafile.write(img+',')
            metafile.write(str(GIRLID)+'\n')
        
        
    
def main():
    
    page_no = 1
    while page_no <= 1000:
        retrieve_posts('http://xinsheng.huawei.com/cn/index.php?app=forum&mod=List&act=index&class=409&cate=44&p='+str(page_no))
        page_no+=1
    global GIRLID
    global IMAGEID
    metafile = open('meta\db.txt', 'a')
    metafile.write('PageCount : ' + str(page_no) + '\n')
    metafile.write('GirlCount : ' + str(GIRLID) + '\n')
    metafile.write('ImageCount : ' + str(IMAGEID) + '\n')



if __name__ == '__main__':
    main()
