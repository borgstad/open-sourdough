FROM python:3.10-slim

WORKDIR /code
COPY requirements.txt /code/
RUN pip install --no-compile -r requirements.txt

RUN useradd -ms /bin/bash open-sourdough && \
  usermod -a -G video open-sourdough
USER open-sourdough

COPY scripts scripts
COPY open_sourdough_monitor open_sourdough_monitor
ENV PYTHONPATH=/code
ENTRYPOINT ["python", "scripts/run.py"]
