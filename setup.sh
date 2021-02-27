mkdir -p ~/.streamlit/
echo "[general]
email = \"jogsaurabh7@gmai.com\"
" > ~/.streamlit/credentials.toml
echo "[server]
headless = true
port = $PORT
enableCORS = false
" > ~/.streamlit/config.toml
