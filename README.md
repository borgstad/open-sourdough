# Open Sourdough
Continously take pictures of your starter!

The module `scripts/run.py` is considered the entrypoint of the project, and when it is executed, it starts a session.
A session is a (continously increasing) number, and an associated directory in the root image directory, where all images will be stored.
The session number is stored in a database, and the images are stored on the filesystem.

## Environment variables
| Env var | Required | Description | 
|---|---|---|
| `OPEN_SOURDOUGH_ROOT_IMAGE_DIR` | Yes | The root directory, where session directories will be created and written to |
| `OPEN_SOURDOUGH_DB_HOST` | Yes | Database hostname |
| `OPEN_SOURDOUGH_DB_NAME` | Yes | Name of the database. If the database does not exist, it will be created, provided the database user has access |
| `OPEN_SOURDOUGH_DB_USER` | Yes | Database user |
| `OPEN_SOURDOUGH_DB_PASSWORD` | Yes | Password for database user |
| `OPEN_SOURDOUGH_DB_PORT` | Yes | Port of the database |

## How to run it
Check the [Makefile](Makefile).
In order to run it locally, `poetry install`.