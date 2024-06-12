from matplotlib.font_manager import fontManager

# 获取系统中所有可用字体
fonts = fontManager.ttflist  # TrueType字体列表
otf_fonts = fontManager.afmlist  # OpenType/CFF字体列表

# 打印所有TrueType字体名称
for font in fonts:
    print(font.name)