FROM python:3.10

RUN apt update && apt install ffmpeg libsm6 libxext6  -y
ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  POETRY_VERSION=1.3.2

RUN pip install "poetry==$POETRY_VERSION"

RUN useradd -ms /bin/bash open-sourdough && \
  usermod -a -G video open-sourdough
USER open-sourdough
WORKDIR /code
COPY pyproject.toml /code/

RUN poetry install
COPY scripts scripts
COPY open_sourdough_monitor open_sourdough_monitor
ENV PYTHONPATH=/code
ENTRYPOINT ["poetry", "run", "python", "scripts/run.py"]
