from PIL import Image, ImageDraw

def make_icon(size, path):
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    cx, cy = size / 2, size / 2
    r = size / 2 - 4

    # Honey background circle
    draw.ellipse([4, 4, size - 4, size - 4], fill='#F5A623')

    # Inner lighter circle
    ir = r * 0.75
    draw.ellipse([cx - ir, cy - ir, cx + ir, cy + ir], fill='#FFD07B')

    # Bee body (oval)
    bw, bh = r * 0.7, r * 0.5
    draw.ellipse([cx - bw, cy - bh * 0.8, cx + bw, cy + bh * 0.8], fill='#4E342E')

    # Bee stripes
    for py in [cy - bh * 0.3, cy, cy + bh * 0.3]:
        draw.ellipse([cx - bw * 0.9, py - bh * 0.15, cx + bw * 0.9, py + bh * 0.15], fill='#FFB84D')

    # Wings
    wing = r * 0.35
    draw.ellipse([cx - wing * 0.3, cy - bh * 0.8 - wing, cx + wing * 1.2, cy - bh * 0.8 + wing * 0.3], fill=(255, 255, 255, 180), outline=(200, 200, 200))
    draw.ellipse([cx + wing * 0.1, cy - bh * 0.7 - wing * 0.8, cx + wing * 1.5, cy - bh * 0.7 + wing * 0.5], fill=(255, 255, 255, 160), outline=(200, 200, 200))

    # Eyes
    eye_r = r * 0.08
    draw.ellipse([cx + bw * 0.3 - eye_r, cy - eye_r * 2, cx + bw * 0.3 + eye_r, cy + eye_r * 0.5], fill='white')
    draw.ellipse([cx + bw * 0.3 - eye_r * 0.5, cy - eye_r * 1.5, cx + bw * 0.3 + eye_r * 0.5, cy], fill='#222')

    # Antennae
    for ax in [-0.2, 0.2]:
        draw.line([cx + bw * ax * 1.5, cy - bh * 0.7, cx + bw * ax * 2.5, cy - bh * 1.5], fill='#4E342E', width=max(2, size // 60))

    img.save(path, 'PNG')
    print(f'{path} ({size}x{size})')

make_icon(192, 'C:/Users/kaiwen/bee-island-game/icon-192.png')
make_icon(512, 'C:/Users/kaiwen/bee-island-game/icon-512.png')
print('Done')
