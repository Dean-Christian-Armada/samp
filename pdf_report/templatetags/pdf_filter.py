from django import template
import urllib, cStringIO, base64

register = template.Library()

@register.filter
def get64(value, url):
    """
    Method returning base64 image data instead of URL for PDF output
    """
    if url.startswith("http"):
        image = cStringIO.StringIO(urllib.urlopen(url).read())
        return 'data:image/jpg;base64,' + base64.b64encode(image.read())
    return url

# register.filter('get64', get64)
# from django import template
# import urllib, cStringIO, base64

# register = template.Library()

# def cut(value, arg):
# 	return arg

# register.filter('cut', cut)