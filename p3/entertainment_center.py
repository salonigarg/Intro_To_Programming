#fresh_tomatoes file is imported to make movie website.
import fresh_tomatoes
#media is imported to make movie website.
import media
#pink is a variable here and there are other items in the list such as movie
#tile,storyline,poster image and youtube trailer.
pink = media.Movie("Pink",
                   "A documentary which makes people realize that women should have equal rights as men",
                   "http://www.comingtrailer.com/wp-content/uploads/2016/08/Pink-Poster-0122643.jpg",
                   "https://www.youtube.com/watch?v=AL2TShb6fFs")  

#similarly three_idiots is also the variable and other items in the list are
#movie title,storyline,poster image and youtube trailer.
three_idiots=media.Movie("3 idiots",
                         "A story full of life and show the true meaning of friendship",
                         "https://images-na.ssl-images-amazon.com/images/M/MV5BMzY2MzgxNDI5MV5BMl5BanBnXkFtZTcwMzk2MzkwMw@@._V1_.jpg",
                         "https://www.youtube.com/watch?v=K0eDlFX9GMc")

#similarly ghajini is also the variable and also the title and other items in
#the list are movie title,storyline,poster image and youtube trailer.
ghajini=media.Movie("Ghagini",
                    "A love story ",
                    "http://blogs.reuters.com/indiamasala/files/2008/12/ghajini.jpg",
                    "https://youtu.be/j_DshRUOm-o")

#similarly barfi,rahasya and raajneeti are also variable and other items
#in the list are movie title,storyline,poster image and youtube trailer.
barfi=media.Movie("Barfi",
                  "A love story of two physically challenged people",
                  "http://c.saavncdn.com/678/Barfi-2012-500x500.jpg",
                  "https://youtu.be/yZxrao3zou4")

rahasya=media.Movie("Rahasya",
                    "Only child of a doctor couple was murdered inside their large duplex apartment",
                    "http://static.koimoi.com/wp-content/new-galleries/2015/01/rahasya-review.jpg",
                    "https://youtu.be/Cvm-KpdRrbk")

raajneeti=media.Movie("Raajneeti",
                      "A educated person enters his family profession that is politicis and goes down to a corrupt path",
                      "http://2.bp.blogspot.com/__2S8xyPCWms/TAm6rK_GavI/AAAAAAAAAM4/FmgiXWkBqQg/s1600/Rajniti-2.jpg",
                      "https://youtu.be/3qAj2pHbNek")

#here a list of movie names is there used to access the data of the movie.
movies = [pink,three_idiots,ghajini,barfi,rahasya,raajneeti]

#fresh_tomatoes.open_movies_page(movies) is used to access fresh tomato file
#and create a website.
fresh_tomatoes.open_movies_page(movies)
