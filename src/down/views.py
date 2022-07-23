from pathlib import Path
from django.shortcuts import render
from pytube import YouTube
import requests
import os
#-----Funtion------#
def single_vedio(links):
    linkList = links.split(',')
    vid_data = []

    for link in linkList:
        link_dict = {}
        if 'yout' in link:
            #link = 'https://youtu.be/mjDlCCqVP8o'
            # print(link)
            url = YouTube(link)
            video = url.streams.get_highest_resolution()
            path_to_download_folder = str(os.path.join(Path.home(), "Downloads"))
            video.download(path_to_download_folder)
            link_dict['title'] = url.title
            link_dict['thumb'] = url.thumbnail_url
            link_dict['url'] = link
            link_dict['dtext'] = 'Video Downloaded. Check Your Download Folder'
            vid_data.append(link_dict)
    return vid_data


# Create your views here.
def home_view(request):
    return render(request, 'home.html')


def down_view(request):
    if request.method == 'POST':
        if request.POST.get('urls'):
            links = request.POST.get('urls')
            data = single_vedio(links)
            #data = vedio_down(links)
            context = {'data':data}
            return render(request, 'single.html', context)
    data = ''
    context = {'data':data}
    return render(request, 'single.html', context)

def thumb_view(request):
    thumb_url = ''
    thumb_title =''
    if request.method == 'POST':
        links = request.POST.get('urls')
        link = links.strip()
        m_url = YouTube(link)
        thumb_url = m_url.thumbnail_url
        thumb_title = m_url.title
        os.chdir(os.path.join(Path.home(), "Downloads"))
        imgName = thumb_title.replace('.',' ').replace('?',' ').replace('‘',' ').replace(',',' ').replace('-',' ').replace('–',' ').replace('—',' ').replace('!',' ').replace(':',' ').replace(';',' ').replace('/',' ').replace('|',' ')
        with open( imgName + '.jpg', 'wb') as f:
            im = requests.get(thumb_url)
            f.write(im.content)
    context = {'thumb_url':thumb_url, 'thumb_title':thumb_title, 'downText': 'Downloaded'}
    return render(request, 'thumbnail.html', context)