# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['__init__.py', 'main.py', 'support.py', 'img_exchange.py', 'qtui.py', 'constants.py'],
    pathex=['/Users/Muyunxi/Desktop/desktop/Developer/Convert-File-Type'],
    binaries=[],
    datas=[
        ('config.json', '.'),
        ('LICENSE', '.'),
        ('README.md', '.'),
        ('main.qss', '.'),
        ('ffmpeg/MacOS/ffmpeg', 'ffmpeg/MacOS')
    ],
    hiddenimports=['moviepy.audio.fx.all.audio_fadein'],
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
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    exclude_binaries=False,
    name='Convert File Type',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='icon.icns'
)

app = BUNDLE(
    exe,
    name='Convert File Type.app',
    icon='icon.icns',
    bundle_identifier='Convert_File_Type',
    version='1.0.0',
    info_plist={
        'NSPrincipalClass': 'NSApplication',
        'NSAppleScriptEnabled': False,
        'CFBundleDocumentTypes': [
            {
                'CFBundleTypeName': 'Convert File Type',
                'CFBundleTypeIconFile': 'icon.icns',
                'LSItemContentTypes': ['com.iewnfod.convert_file_type'],
                'LSHandlerRank': 'Iewnfod'
            }
        ]
    },
)
