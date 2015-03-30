class SpaceCenterRemoveTemplateGlyphs(object):
    
    """
    Space Center - Remove Template Glyphs
    by Andy Clymer
    
    Copyright (c) 2015 Hoefler & Co.
    http://typography.com
    
    Last Modified 2015 03 30
    
    
    This class watches for when a new Space Center window opens, and then 
    removes any empty template glyphs from the Space Center text input line. 
    Additionally, it converts the text input to use only glyph names instead
    of a mix of ASCII characters and glyph names.

    
    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:
    The above copyright notice and this permission notice shall be included in
    all copies or substantial portions of the Software.
    
    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
    THE SOFTWARE.  
    
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