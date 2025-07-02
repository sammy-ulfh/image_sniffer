#!/usr/bin/env python3

from mitmproxy import http
import os

start = 1

def print_banner():
    print("""
█ █▀▄▀█ ▄▀█ █▀▀ █▀▀   █▀ █▄░█ █ █▀▀ █▀▀ █▀▀ █▀█
█ █░▀░█ █▀█ █▄█ ██▄   ▄█ █░▀█ █ █▀░ █▀░ ██▄ █▀▄\n""")

    print("""Mᴀᴅᴇ ʙʏ sᴀᴍᴍʏ-ᴜʟғʜ\n""")

def response(packet):
    global start

    if start:
        print_banner()
        start = 0
        os.makedirs('images', exist_ok=True)

    header = packet.response.headers.get("content-type", "").split('/')

    if "image" in header:
        header = header[-1]
        ext = "jpg" if header == "jpeg" else header

        try:
            name = packet.request.url.replace('/', '_').replace(':', '_')
            content = packet.response.content

            if content and ext:
                with open(f"images/{name}.{ext}", "wb") as f:
                    f.write(content)

                print(f"\n[+] Image Saved: {name}")
        except:
            pass

