import webbrowser
class Movie():
    #init is used to initialize the object.init function is predefined.
    def __init__(self,movie_title,movie_storyline,movie_posterimage,movie_traileryoutube):
        #movie_title is a instance for the class used to access the values given.
        self.title=movie_title
        #movie_storyline,movie_posterimage,movie_traileryoutube are also the
        #instances of the class.
        self.storyline=movie_storyline
        self.poster_image_url=movie_posterimage
        self.trailer_youtube_url=movie_traileryoutube
        
    #show_trailer is defined here to show the trailer of the requested movie
    #by clicking on it in a browser.
    def show_trailer(self):
        #webbrowser is a module which have a function open which opens the given
        #url in the browser.
        webbrowser.open(self.trailer_youtube_url)
                 
                 
