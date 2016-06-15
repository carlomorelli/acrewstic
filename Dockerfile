FROM python:2.7
ADD . /acrewstic
WORKDIR /acrewstic
RUN pip install -r requirements.txt
CMD python acrewstic.py