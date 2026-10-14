import re

files = ['index.html', 'adeera-invite.html', 'adeera-invite-offline.html']

for fname in files:
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Add 'rect' class to the .ph div
    content = content.replace(
        'class="ph" style="left:8px;top:34px;',
        'class="ph rect" style="left:8px;top:34px;'
    )
    
    # 2. Replace base64 image src with image.png
    content = re.sub(
        r'src="data:image/jpeg;base64,/9j/[^\"]*"',
        'src="image.png"',
        content
    )
    
    # 3. Replace the audio data URI with MP3 file
    content = re.sub(
        r'var a=new Audio\("data:audio/mpeg;base64,SUQzBAAAAAAB[^"]*"\)',
        'file=new Audio("bluey_theme_full.mp3");file.loop=true;file.volume=0.16;',
        content
    )
    
    # 4. Update error handler to use 'file' instead of 'a'
    content = content.replace("a.addEventListener('error',synth)", "file.addEventListener('error',synth)")
    content = content.replace("var pr=a.play()", "var pr=file.play()")
    
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f'Updated {fname}')

print('Done!')