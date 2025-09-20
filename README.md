# proxy
Use LiteLLM Gateway to add TextNormalization as a feature and execute pre-call hooks

To setup and run the code:

```
python3 -m venv .venv
source .venv/bin/activate
pip3 install spacy
pip3 install nltk
pip3 install dateparser
python -m spacy download en_core_web_sm
python -c "import nltk; nltk.download('stopwords')"
pip install 'litellm[proxy]'
```

To start Litellm:

  ```litellm --config ./config.yaml --detailed_debug```

To send requests:

   ```python ./ai_proxy.py```
