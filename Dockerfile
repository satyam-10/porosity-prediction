FROM python:3.8
WORKDIR /app
COPY Porosity_prediction.ipynb /
COPY btp_data.xlsx /
RUN pip install jupyter pandas scikit-learn
EXPOSE 8888
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--NotebookApp.token="]
