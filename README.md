# Open Sourdough

Monitor and track the growth of your sourdough starter with continuous picture-taking!

Open Sourdough is a Python script designed to take pictures of your sourdough starter at regular intervals.
The primary goal of this project is to help you visualize the growth and activity of your starter.

The entry point of the project is scripts/run.py.
Upon execution, it starts a session.
A session is defined by a continuously increasing number and an associated directory in the root image directory, where all images will be stored.
The session number is stored in a database, while the images are stored on the filesystem.
Environment variables
| Env var |	Required |	Description| 
|---|---|---|
|OPEN_SOURDOUGH_ROOT_IMAGE_DIR |Yes | The root directory, where session directories will be created and written to
|OPEN_SOURDOUGH_DB_HOST| Yes | Database hostname
|OPEN_SOURDOUGH_DB_NAME| Yes | Name of the database. If the database does not exist, it will be created, provided the database user has the necessary privileges
|OPEN_SOURDOUGH_DB_USER| Yes | Database user
|OPEN_SOURDOUGH_DB_PASSWORD| Yes | Password for the database user
|OPEN_SOURDOUGH_DB_PORT| Yes | Port of the database

** Installation and setup

1. Clone the repository from https://github.com/borgstad/open-sourdough.
2. Ensure you have Python 3.7 or higher installed.
3. Install Poetry, a package manager for Python, by following the instructions here.
4. Run poetry install to install the project dependencies.
5. Set the required environment variables listed in the table above in a .env file in the root of the project.

** Running the script

To run the script, you can use the Makefile provided in the repository. Execute the following command in your terminal:

```bash
make build run
```

This will start a new session and begin taking pictures of your sourdough starter at the specified intervals.