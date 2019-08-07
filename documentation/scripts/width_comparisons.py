glyphdict = {}

for font in AllFonts():
    for glyph in font:
        #print(glyph)
        if glyph.markColor != None:
            glyphWidth = glyph.width-(glyph.leftMargin+glyph.rightMargin)
            glyphdict.setdefault(glyph.name, [])
            glyphdict[glyph.name].append(glyphWidth)

for i in glyphdict.copy():
    if len(glyphdict[i]) < 2:
        glyphdict.pop(i)

for entry in glyphdict:
    percent = int((glyphdict[entry][1]/glyphdict[entry][0])*100)
    glyphdict[entry] = percent

meanTotal = 0
    
for key, value in glyphdict.items():
    meanTotal += value
    
meanTotal = int(meanTotal/len(glyphdict))

outliers = []
filterSensitivity = 15

for key, value in sorted(glyphdict.items(), key = lambda item: item[1]):
    difference = value-meanTotal
    if difference <= -filterSensitivity or difference >= filterSensitivity:
        outliers.append("%s: %s%%" % (key, value-meanTotal))

print("Glyph-to-glyph comparison between %s and %s with a filterSensitivity of +-%s:" % (
    (AllFonts()[0].info.familyName + " " + AllFonts()[0].info.styleName), 
    (AllFonts()[1].info.familyName + " " + AllFonts()[1].info.styleName), filterSensitivity))
print(outliers)