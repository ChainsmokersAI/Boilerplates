# PyTorch v2.0.1
FROM pytorch/pytorch:2.0.1-cuda11.7-cudnn8-runtime

# Work (Main) Directory
WORKDIR /root/research/

# Install Packages
RUN apt-get update \
    && apt-get install -yq vim git wget zip unzip

# PIP Install (Python) Packages
ADD requirements.txt /root/research/
RUN pip install -r requirements.txt

# Set Jupyter Configuration
ADD jupyter_notebook_config.py /root/research/
RUN jupyter notebook --generate-config \
    && rm /root/.jupyter/jupyter_notebook_config.py \
    && cp jupyter_notebook_config.py /root/.jupyter/
