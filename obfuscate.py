#!/usr/bin/env python3
import base64, zlib, os

def obfuscate_file(source_file, output_file):
    with open(source_file, 'r') as f:
        code = f.read()
    
    compressed = zlib.compress(code.encode())
    encoded = base64.b64encode(compressed).decode()
    
    wrapper = f'''#!/usr/bin/env python3
import base64, zlib, os, sys
if not os.path.exists("mgkan_key.txt"):
    print("❌ No key found. Run MgKan.py first.")
    sys.exit(1)
exec(zlib.decompress(base64.b64decode("{encoded}")))
'''
    
    with open(output_file, 'w') as f:
        f.write(wrapper)
    print(f"✅ Obfuscated: {output_file}")

# Obfuscate လုပ်မယ့်ဖိုင်တွေ
files = ["MgKan.py", "scanner.py"]

for file in files:
    if os.path.exists(file):
        obfuscate_file(file, file)
    else:
        print(f"❌ {file} not found!")
