FROM python:3.7.3
#WORKDIR C:\\Users\Admin\Proy\Scr

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt 
COPY . . 

CMD [ "python3", "./scrapTest/spiders/UPCSpider.py"]
