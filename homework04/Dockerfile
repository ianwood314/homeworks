FROM centos:7.9.2009

RUN yum update -y
RUN yum install -y python3 && \
    pip3 install pytest==7.0.0

COPY ml_data_analysis.py /code/ml_data_analysis.py
RUN chmod +rx /code/ml_data_analysis.py
COPY test_ml_data_analysis.py /code/test_ml_data_analysis.py
COPY Meteorite_Landings.json /data/Meteorite_Landings.json

ENV PATH "/code:$PATH"
