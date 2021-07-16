from tistory_util import *
import requests

blog_name = "floatingavocadoseed"
category_id = "998882"
nasa_url = "https://api.nasa.gov/planetary/apod?api_key=xIIiWFVGSH8Xk3apn1jbOfefiB6T67qhqdtbUEwa"

def writer():

    data_from_nasa = requests.get(nasa_url).json()

    title = "today's photo from NASA."

    content = '''
<p><span style="color: #000000;">Hi!</span><span style="color: #000000;"><br /></span>
<span style="color: #000000;">Here's photos.</span></p>
<p>&nbsp;</p>
<p><img src="{data_from_nasa['url']}" /></p>
<p><span style="color: #000000;">the title of his one is <span>{data_from_nasa['title']}</span> some descriptions: </span></p>
<p>&nbsp;</p>
<p><span style="color: #000000;"><span>{data_from_nasa['explanation']}</span></span></p>
<p>&nbsp;</p>
<p><span style="color: #000000;">awesome!</span><span style="color: #000000;"><br /></span>
<span style="color: #000000;">Bye! happy earth trips!</span></p>
<p>&nbsp;</p>
            '''

    return title, content


if __name__ == "__main__":
    title, content = writer()

    blog_write(
        blog_name=blog_name,
        category_id=category_id,
        title=title,
        content=content,
        tag='NASA, python')
