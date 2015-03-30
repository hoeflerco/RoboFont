class SpaceCenterRemoveTemplateGlyphs(object):
    
    """
    This script watches for when a new Space Center window opens, and then removes any empty template glyphs from the Space Center text input line. Additionally, it converts the text input to use only glyph names instead of a mix of ASCII characters and glyph names.
    """
    
    def __init__(self):
        addObserver(self, "updateWindow", "spaceCenterDidOpen")
        
    def updateWindow(self, info):
        font = info["font"]
        window = info["window"]
        sc = window.getSpaceCenter()
        allGlyphs = font.keys()
        glyphNames = []
        for glyphName in sc.get():
            if glyphName in allGlyphs:
                glyphNames += [glyphName]
        sc.set(glyphNames)

SpaceCenterRemoveTemplateGlyphs()