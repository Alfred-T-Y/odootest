FROM odoo:16

RUN pip install --upgrade pip
COPY ./requirements.txt /
RUN pip install -r requirements.txt --timeout 10000
