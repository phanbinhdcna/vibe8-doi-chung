import os
if os.environ.get("XUONG_TOKEN_APP"):
    print("MA-TU-PR-CHAY; co token:", bool(os.environ.get("XUONG_TOKEN_APP")))
    raise SystemExit(0)
raise SystemExit(1)
