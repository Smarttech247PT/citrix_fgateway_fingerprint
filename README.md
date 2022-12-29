# citrix_gateway_fingerprint

Python script to identify Citrix Gateway version based on the reserch from fox-it:
https://blog.fox-it.com/2022/12/28/cve-2022-27510-cve-2022-27518-measuring-citrix-adc-gateway-version-adoption-on-the-internet/

## Usage
```
citrix_fingerprint.py URL
```
provide only root URL, the script will append `/vpn/index.html` itself
