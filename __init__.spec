# -*- mode: python ; coding: utf-8 -*-
# pyinstaller __init__.spec -y

block_cipher = None


a = Analysis(
    ['__init__.py'],
    pathex=['src', 'venv/lib/python3.10/site-packages'],
    binaries=[],
    datas=[
        ('ffmpeg', 'ffmpeg'),
        ('Resources', 'Resources'),
        ('src', 'src'),
        ('/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages/moviepy', 'moviepy'),
        ('/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages/imageio', 'imageio'),
        ('/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages/numpy', 'numpy'),
        ('/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages/proglog', 'proglog'),
        ('/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages/tqdm', 'tqdm'),
        ('/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages/imageio_ffmpeg', 'imageio_ffmpeg'),
        ('/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages/pkg_resources', 'pkg_resources'),
        ('/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages/PIL', 'PIL'),
        ('/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages/pypandoc', 'pypandoc')
    ],
    hiddenimports=[
        'PySide6',
        'PySide6.QtWidgets',
        'secrets',
        'ctypes',
        'pkgutil',
        'more_itertools',
        'pyparsing',
        'http.cookies',
        'rlcompleter',
        'decorator',
        'requests',
        'charset_normalizer.md__mypyc'
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='Convert File Type',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='Convert File Type',
)
app = BUNDLE(
    coll,
    name='Convert File Type.app',
    icon=None,
    bundle_identifier=None,
)
