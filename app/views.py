from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import ActivityForm
from cloudinary.forms import cl_init_js_callbacks   

import os
import folium
import gpxpy
import urllib.request

# # Create your views here.
def home(request):
    context = {}
    return render(request,'home.html',context)

def about(request):
    context = {}
    return render(request,'about.html',context)

def activity(request):
    zoom = 14
    #gpx_dir = os.path.join(os.getcwd(),'media','shp')
    #gpx_file = open(os.path.join(gpx_dir, 'test.gpx'), 'r')
    gpxPath = "https://res.cloudinary.com/dapgpdd7z/raw/upload/v1653520044/oubn2z8a8ws8wlc4e6s1.gpx"
    #gpx_file = urllib.request.urlretrieve(gpxPath)

    urllib.request.urlretrieve(gpxPath, "temp.gpx")

    #gpx_file = open(gpxData, 'r')
    gpx_file = open(os.path.join(os.getcwd(), 'temp.gpx'), 'r')
    gpx = gpxpy.parse(gpx_file)
    points = []
    for track in gpx.tracks:
        for segment in track.segments:        
            for point in segment.points:
                points.append(tuple([point.latitude, point.longitude]))
    latitude = sum(p[0] for p in points)/len(points)
    longitude = sum(p[1] for p in points)/len(points)
    myMap = folium.Map(location=[latitude,longitude],zoom_start=zoom)
    folium.PolyLine(points, color="red", weight=2.5, opacity=1).add_to(myMap)

    ## exporting
    myMap=myMap._repr_html_()
    context = {'my_map': myMap, 'elev_plot': myMap}
    ## rendering
    return render(request,'activity.html',context)

# # Create your views here.
# def home(request):
#     # Downloading the gpx file
#     gpxPath = "https://res.cloudinary.com/dapgpdd7z/raw/upload/v1653520044/oubn2z8a8ws8wlc4e6s1.gpx"
#     urllib.request.urlretrieve(gpxPath, "temp.gpx")

#     # Generating the Map Plot
#     # Define some properties for drawing the line:
#     line_options = {'color': 'blue', 'weight': 8, 'opacity': 0.5}
#     plt.style.use('seaborn-talk')

#     myMap = create_folium_map()
#     for track in read_gpx_file(os.path.join(os.getcwd(), 'temp.gpx')):
#         for i, segment in enumerate(track['segments']):
#             add_segment_to_map(myMap, segment, line_options=line_options)

#     def render_elev_plot():
#         for track in read_gpx_file(os.path.join(os.getcwd(), 'temp.gpx')):
#             for i, segment in enumerate(track['segments']):
#                 plot_filled(track, segment, xvar='Distance / km', yvar='elevation',zvar='Velocity / km/h')
        
#         imgdata = StringIO()
#         plt.savefig(imgdata, format='svg')
#         imgdata.seek(0)

#         data = imgdata.getvalue()
#         return data


#     #plt.savefig('matplot_test.png')
#     ## exporting
#     myMap=myMap._repr_html_()
#     # elev_plot = render_elev_plot()._repr_html_()
#     #context = {'my_map': myMap}
#     context = {'my_map': myMap, 'elev_plot': myMap}
#     ## rendering
#     return render(request,'home.html',context)



def AddActivity(request):
    # djanogo docs: https://docs.djangoproject.com/en/4.0/topics/forms/
    # https://cloudinary.com/documentation/django_image_and_video_upload#django_forms_and_models

    context = dict( form = ActivityForm())


    if request.method == 'POST':
        form = ActivityForm(request.POST, request.FILES)
        context['posted'] = form.instance
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/") 
    else:
        form = ActivityForm()

    return render(request, "upload.html", context)