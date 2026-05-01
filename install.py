import os

# Nome da pasta da tua extensão
folder_name = "StrongPasswordExtension"

# Cria a pasta se não existir
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# 1. Criar o manifest.json
manifest = """{
  "manifest_version": 3,
  "name": "Strong Password Generator",
  "version": "1.0",
  "action": {
    "default_popup": "popup.html",
    "default_icon": "icon.svg"
  },
  "icons": {
    "128": "icon.svg"
  }
}"""

# 2. Criar o popup.html
html = """<!DOCTYPE html>
<html>
<head>
  <style>
    body { font-family: 'Segoe UI', sans-serif; width: 250px; padding: 15px; text-align: center; }
    svg { width: 50px; height: 50px; }
    h2 { font-size: 14px; color: #202124; }
    #pass { 
      background: #f1f3f4; padding: 10px; border-radius: 8px; 
      word-break: break-all; font-family: monospace; margin: 10px 0;
    }
    button {
      background: #1a73e8; color: white; border: none; padding: 10px;
      border-radius: 20px; cursor: pointer; width: 100%; font-weight: bold;
    }
  </style>
</head>
<body>
  <svg viewBox="0 0 128 128">
    <path d="M64 10 L20 30 V60 C20 85 38 108 64 118 C90 108 108 85 108 60 V30 L64 10Z" fill="#1a73e8"/>
    <rect x="44" y="60" width="40" height="30" rx="4" fill="white"/>
  </svg>
  <h2>Strong Password Generator</h2>
  <div id="pass">Clica para gerar</div>
  <button id="btn">Gerar (30 chars)</button>
  <script src="popup.js"></script>
</body>
</html>"""

# 3. Criar o popup.js
js = """document.getElementById('btn').addEventListener('click', () => {
  const charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+";
  let password = "";
  const values = new Uint32Array(30);
  window.crypto.getRandomValues(values);
  for (let i = 0; i < 30; i++) {
    password += charset[values[i] % charset.length];
  }
  document.getElementById('pass').innerText = password;
  navigator.clipboard.writeText(password);
});"""

# 4. Criar o icon.svg
svg = """<svg width="128" height="128" viewBox="0 0 128 128" xmlns="http://w3.org">
  <path d="M64 10 L20 30 V60 C20 85 38 108 64 118 C90 108 108 85 108 60 V30 L64 10Z" fill="#1a73e8"/>
  <rect x="44" y="60" width="40" height="30" rx="4" fill="white"/>
</svg>"""

# Escrever os ficheiros na pasta
files = {
    "manifest.json": manifest,
    "popup.html": html,
    "popup.js": js,
    "icon.svg": svg
}

for name, content in files.items():
    with open(os.path.join(folder_name, name), "w", encoding="utf-8") as f:
        f.write(content)

print(f"Sucesso! A pasta '{folder_name}' foi criada com todos os ficheiros.")
print("Agora vai a chrome://extensions e carrega esta pasta.")
