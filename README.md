# Game Description
In this game, the player is presented with a grid of cells, each initially colored with a random color. The objective of the game is to fill the entire grid with a single color by strategically selecting cells to change their color. When a cell is selected, its color changes to the target color, and all adjacent cells of the same color also change to the target color. The player can continue selecting cells until the entire grid is filled with the target color.

# Technologies Used
HTML: The game layout and structure are created using HTML.
CSS: CSS is used for styling the game interface and grid.
Python: The game logic and algorithms are implemented using Python programming language.
Docker: Docker is used to containerize the game application for easy deployment and portability.

# How to Run the Game
To run the game locally, make sure you have Docker installed on your system. Follow these steps:

1. Install Docker on your system if you haven't already. Refer to the Docker documentation for installation instructions.
2. Pull the Docker image from the Docker Hub repository by running the following command:
  docker pull thakurmanali/fill-color-game
3. Once the image is downloaded, create and run a container using the following command:
  docker run -p 8000:8000 thakurmanali/fill-color-game
4. Open your web browser and visit http://localhost:8000 to start playing the game.

# Acknowledgements
This game was inspired by the concept of color-fill games and developed as a fun project to showcase Python programming skills and Docker usage.

Feel free to explore and enhance the game further by adding new features or improving the user interface. Enjoy playing the Color-fill Single Player Game!
