FROM python
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -i https://pypi.doubanio.com/simple/ --trusted-host pypi.doubanio.com -r requirements.txt
ADD . /code/