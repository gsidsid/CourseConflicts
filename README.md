
# When2Discrete
![alt text](https://heroku-badge.herokuapp.com/?app=course-conflicts)


An application-based investigation of graph coloring algorithms for course scheduling conflict resolution. 

### Info:

*Scraping/course_scraper.py* goes to the Olin portal, checks out all the course ID's and times, and outputs a JSON file to course_books, where the Registrar looks for a course list to give the scheduler.

*Graphing/scheduler.py* goes to the Registrar, gets a list of times courses are offered, and creates a Graph of courses connected by common times. The scheduler completes graph coloring operations, and outputs node and adjacency data to a JSON file where Visualizations can pick up.

*Visualizations/cfvis.py* is a web front-end for handling user interactions with the scheduler.

