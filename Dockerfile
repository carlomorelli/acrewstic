FROM python:3.6
ADD . /acrewstic
WORKDIR /acrewstic
RUN pip install -r requirements.txt
CMD python src/acrewstic.py