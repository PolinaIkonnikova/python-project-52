FROM python:3.9-bullseye

RUN mkdir /tasks

WORKDIR /tasks

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV PYTHONPATH=/tasks

#COPY ./requirements.txt /tasks/requirements.txt

RUN pip install poetry
RUN poetry config virtualenvs.create false
#RUN pip install --no-cache-dir -r requirements.txt

COPY . /tasks/

RUN poetry install

RUN chmod a+x /tasks/run_app.sh

EXPOSE 8000

CMD ["/tasks/run_app.sh"]
