import os, re

base = "/Users/kazushi/Downloads/株式会社SAI_website"

# SAI logo - dark navy version (for header, on light bg)
sai_dark = '<svg viewBox="0 0 60 32" fill="none" xmlns="http://www.w3.org/2000/svg" width="52" height="28"><text x="0" y="26" font-family="Arial,Helvetica,sans-serif" font-weight="900" font-size="28" fill="#1B2A4A" letter-spacing="-1">S</text><text x="17" y="26" font-family="Arial,Helvetica,sans-serif" font-weight="900" font-size="28" fill="#1B2A4A" letter-spacing="-1">A</text><text x="38" y="26" font-family="Arial,Helvetica,sans-serif" font-weight="900" font-size="28" fill="#1B2A4A" letter-spacing="-1">I</text><polygon points="22,13 31,13 31,9 37,16 31,23 31,19 22,19" fill="#4A9EF5"/></svg>'

# SAI logo - white version (for footer on dark bg)  
sai_white = '<svg viewBox="0 0 60 32" fill="none" xmlns="http://www.w3.org/2000/svg" width="52" height="28"><text x="0" y="26" font-family="Arial,Helvetica,sans-serif" font-weight="900" font-size="28" fill="#fff" letter-spacing="-1">S</text><text x="17" y="26" font-family="Arial,Helvetica,sans-serif" font-weight="900" font-size="28" fill="#fff" letter-spacing="-1">A</text><text x="38" y="26" font-family="Arial,Helvetica,sans-serif" font-weight="900" font-size="28" fill="#fff" letter-spacing="-1">I</text><polygon points="22,13 31,13 31,9 37,16 31,23 31,19 22,19" fill="#4A9EF5"/></svg>'

files = ['index.html', 'services.html', 'about.html', 'contact.html', 'privacy.html']
for f in files:
    path = os.path.join(base, f)
    with open(path, 'r') as fh:
        content = fh.read()
    
    # Replace header SVG (first match - before logo-text)
    content = re.sub(
        r'<svg viewBox="0 0 36 36"[^>]*>.*?</svg>(?=</span>\s*\n?\s*<span class="logo-text">)',
        sai_dark, content, flags=re.DOTALL, count=1
    )
    
    # Replace footer SVG (remaining 36x36)
    content = re.sub(
        r'<svg viewBox="0 0 36 36"[^>]*>.*?</svg>(?=</span>)',
        sai_white, content, flags=re.DOTALL
    )
    
    # Also remove inline background style on footer logo-icon
    content = content.replace(
        'style="background:linear-gradient(135deg,#fff,#e8f0fe);"', 
        'style="background:transparent;"'
    )
    content = content.replace(
        'style="background:#fff;color:var(--primary);"',
        'style="background:transparent;"'
    )
    
    with open(path, 'w') as fh:
        fh.write(content)
    print(f"Updated {f}")

# Update favicon
favicon = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" fill="none">
  <rect width="32" height="32" rx="6" fill="#1B2A4A"/>
  <text x="3" y="23" font-family="Arial,sans-serif" font-weight="900" font-size="13" fill="#fff" letter-spacing="-0.5">SAI</text>
  <polygon points="12,12 17,12 17,9 21,16 17,23 17,20 12,20" fill="#4A9EF5"/>
</svg>'''
with open(os.path.join(base, 'favicon.svg'), 'w') as fh:
    fh.write(favicon)
print("Updated favicon.svg")
print("All done!")
