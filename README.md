# Demo Universal API Skeleton

## Overview
Toto je demo kostra našeho Universal Modular API.
- Jednoduchá "propojka" pro testování přijímání a ukládání dat
- Endpoint: POST /data/submit

## Quick Start

1. Nainstalujte závislosti:
```bash
pip install -r requirements.txt
```

2. Spusťte demo server:
```bash
uvicorn api_core.endpoints_demo:app --reload --host 0.0.0.0 --port 8000
```

3. Vyzkoušejte endpoint:
- POST request na `/data/submit` s parametry `app_name` a `payload` (JSON/string)

💡 Fun note: Tento demo balíček vznikl během epické spolupráce Tom & Brain — jsme tak produktivní, že by káva mohla sama vařit! 😎