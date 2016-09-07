#!/usr/bin/python
# -*- coding: utf-8 -*-
import videos
import movieclass
import fresh_tomatoes

# Declaring the movies to be used in this program

ant_man = movieclass.Movie('Ant Man', 'movie',
                           'A superhero who can change his size',
                           'http://blogs-images.forbes.com/scottmendelson/files/2015/05/BF_Payoff_1-Sht_v8_Lg-1309x1940.jpghttps://www.youtube.com/watch?v=pWdKf3MneyI')  # noqa,

groundhog_day = movieclass.Movie('Groundhog Day', 'movie',
                                 'A man whose life repeats',
                                 'http://www.gstatic.com/tv/thumb/movieposters/14569/p14569_p_v8_ah.jpg'  # noqa,
                                 'https://www.youtube.com/watch?v=tSVeDx9fk60')

school_of_rock = movieclass.Movie('School of Rock', 'movie',
                                  'Rock musician becomes school teacher',
                                  'http://www.gstatic.com/tv/thumb/movieposters/33094/p33094_p_v8_aa.jpg',  # noqa
                                  'https://www.youtube.com/watch?v=XCwy6lW5Ixc')  # noqa

spider_man = movieclass.Movie('Spider Man', 'movie',
                              'A boy acquires abilities of a spider',
                              'https://upload.wikimedia.org/wikipedia/en/f/f3/Spider-Man2002Poster.jpg',  # noqa
                              'https://www.youtube.com/watch?v=O7zvehDxttM')

moneyball = movieclass.Movie('Moneyball', 'movie',
                             'A man uses maths to build a baseball team',
                             'http://www.impawards.com/2011/posters/moneyball_ver2.jpg',  # noqa
                             'https://www.youtube.com/watch?v=AiAHlZVgXjk')

the_last_samurai = movieclass.Movie('The Last Samurai', 'movie',
                                    'An American soldier joins a Japanese clan against the Emperor',  # noqa
                                    'http://cdn.traileraddict.com/content/warner-bros-pictures/lastsamurai.jpg',  # noqa
                                    'https://www.youtube.com/watch?v=T50_qHEOahQ')  # noqa

movie_list = [
    ant_man,
    groundhog_day,
    school_of_rock,
    spider_man,
    moneyball,
    the_last_samurai,
]

# Creating the webpage

fresh_tomatoes.open_movies_page(movie_list)
