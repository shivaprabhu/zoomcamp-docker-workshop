FROM python:3.13.11-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/

WORKDIR /code
COPY .python-version pyproject.toml uv.lock ./

RUN uv sync --locked

#RUN pip install pandas pyarrow

WORKDIR /code
ENV PATH="/code/.venv/bin:$PATH"

COPY pipeline-init.py .


#ENTRYPOINT [ "uv","run","python3","pipeline-init.py" ]
ENTRYPOINT ["python3","pipeline-init.py" ]