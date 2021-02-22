# Wiki-Speed-Solver

Wiki-Speed-Solver is inspired by an online game "Wiki Game" (https://www.thewikigame.com/group), where one has to find a path from one word to another traversing links within a Wikipedia page. This code generates the shortest path from one key word the another using the Breadth First Search and uses the BeautifulSoup API to scrape the data on the wikipedia page.

This Project is currently in Developement Phase. Things I am going to work on are:
   1) Instead of making an API call hyperlink, download the Wikipedia page and parse it (so that the API calls are not overwhelming)
   2) Find a more efficient way to store the paths, putting all the paths in to array takes TOO MUCH TIME (~ 5mins for 2 degree solutions)
