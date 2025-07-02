#!/usr/bin/env python3

from mitmproxy import http
import os

def response(packet):
    header = packet.response.headers.get("content-type", "").split('/')
    os.makedirs('images', exist_ok=True)

    if "image" in header:
        header = header[-1]
        ext = "jpg" if header == "jpeg" else header

        try:
            name = packet.request.url.replace('/', '_').replace(':', '_')
            content = packet.response.content

            if content and ext:
                with open(f"images/{name}.{ext}", "wb") as f:
                    f.write(content)

                print(f"\n[+] Imagen Almacenada: {name}")
        except:
            pass

