# -*- mode: python ; coding: utf-8 -*-

import os
from kivy_deps import sdl2, glew


block_cipher = None


a = Analysis(['main.py'],
             pathex=[],
             binaries=[],
             datas=[('ControleGeral.kv','.'),('*.py','.'),('*.png','.'),('*.txt','.'),('*.db','.'),('teste.ods','.'),('logoEN.ico','.')],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts, 
          [],
          exclude_binaries=True,
          name='Controle Geral',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None,
          icon= 'C:\\Users\\jbmic\\OneDrive\\Área de Trabalho\\PBEN-main\\logoEN.ico')

coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               Tree('C:\\Users\\jbmic\\AppData\\Local\\Programs\\Python\\Python311\\share\\sdl2\\bin'),
               Tree('C:\\Users\\jbmic\\AppData\\Local\\Programs\\Python\\Python311\\share\\glew'), 
               Tree('C:\\Users\\jbmic\\AppData\\Local\\Programs\\Python\\Python311\\share\\angle\\bin'),
               Tree('C:\\Users\\jbmic\\AppData\\Local\\Programs\\Python\\Python311\\share\\gstreamer'),
               Tree('C:\\Users\\jbmic\\AppData\\Local\\Programs\\Python\\Python311\\share\\kivy-examples'),
               strip=False,
               upx=True,
               upx_exclude=[],
               name='Controle Geral')