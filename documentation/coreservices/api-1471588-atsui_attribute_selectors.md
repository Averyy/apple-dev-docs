# ATSUI Attribute Selectors

**Framework**: Core Services  
**Kind**: enum  
**Role**: Enumeration

Specify feature availability for Apple Type Services for Unicode Imaging.

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
enum : unsigned int {
    ...
};
```

## Topics

### Constants
- [gestaltATSUFeatures](./api-1471588-atsui_attribute_selectors/gestaltatsufeatures.md)
- [gestaltATSUTrackingFeature](./api-1471588-atsui_attribute_selectors/gestaltatsutrackingfeature.md)
  If the bit specified by this mask constant is set, the functions `ATSUCountFontTracking` and `ATSUGetIndFontTracking` are available.
- [gestaltATSUMemoryFeature](./api-1471588-atsui_attribute_selectors/gestaltatsumemoryfeature.md)
  If the bit specified by this mask is set, the functions `ATSUCreateMemorySetting`, `ATSUSetCurrentMemorySetting`, `ATSUGetCurrentMemorySetting`, and `ATSUDisposeMemorySetting` are available.
- [gestaltATSUFallbacksFeature](./api-1471588-atsui_attribute_selectors/gestaltatsufallbacksfeature.md)
  If the bit specified by this mask is set, the functions `ATSUSetFontFallbacks` and `ATSUGetFontFallbacks` are available.
- [gestaltATSUGlyphBoundsFeature](./api-1471588-atsui_attribute_selectors/gestaltatsuglyphboundsfeature.md)
  If the bit specified by this mask is set, the function `ATSUGetGlyphBounds` is available.
- [gestaltATSULineControlFeature](./api-1471588-atsui_attribute_selectors/gestaltatsulinecontrolfeature.md)
  If the bit specified by this mask is set, the functions `ATSUCopyLineControls`, `ATSUSetLineControls`, `ATSUGetLineControl`, `ATSUGetAllLineControls`, and `ATSUClearLineControls` are available.
- [gestaltATSULayoutCreateAndCopyFeature](./api-1471588-atsui_attribute_selectors/gestaltatsulayoutcreateandcopyfeature.md)
  If the bit specified by this mask is set, the function `ATSUCreateAndCopyTextLayout` is available.
- [gestaltATSULayoutCacheClearFeature](./api-1471588-atsui_attribute_selectors/gestaltatsulayoutcacheclearfeature.md)
  If the bit specified by this mask is set, the function `ATSUClearLayoutCache` is available.
- [gestaltATSUTextLocatorUsageFeature](./api-1471588-atsui_attribute_selectors/gestaltatsutextlocatorusagefeature.md)
  If the bit specified by this mask is set, the text-break locator attribute is available for both style and text layout objects.
- [gestaltATSULowLevelOrigFeatures](./api-1471588-atsui_attribute_selectors/gestaltatsulowlevelorigfeatures.md)
  If the bit specified by this mask is set, the low-level features introduced in ATSUI version 2.0 are available.
- [gestaltATSUFallbacksObjFeatures](./api-1471588-atsui_attribute_selectors/gestaltatsufallbacksobjfeatures.md)
  If the bit specified by this mask is set, `ATSUFontFallbacks` objects are available.
- [gestaltATSUIgnoreLeadingFeature](./api-1471588-atsui_attribute_selectors/gestaltatsuignoreleadingfeature.md)
  If the bit specified by this mask is set, the line layout option (`kATSIgnoreFontLeadingTag`) to ignore the font leading value is available.
- [gestaltATSUByCharacterClusterFeature](./api-1471588-atsui_attribute_selectors/gestaltatsubycharacterclusterfeature.md)
  If the bit specified by this mask is set, ATSUI cursor movement types are available.
- [gestaltATSUAscentDescentControlsFeature](./api-1471588-atsui_attribute_selectors/gestaltatsuascentdescentcontrolsfeature.md)
  If the bit specified by this mask is set, ascent and descent controls (`kATSUDescentTag` and `kATSUAscentTag`) are available.
- [gestaltATSUHighlightInactiveTextFeature](./api-1471588-atsui_attribute_selectors/gestaltatsuhighlightinactivetextfeature.md)
  If the bit specified by this mask is set, the highlight inactive text feature is available.
- [gestaltATSUPositionToCursorFeature](./api-1471588-atsui_attribute_selectors/gestaltatsupositiontocursorfeature.md)
  If the bit specified by this mask is set, the position-to-cursor feature is available.
- [gestaltATSUBatchBreakLinesFeature](./api-1471588-atsui_attribute_selectors/gestaltatsubatchbreaklinesfeature.md)
  If the bit specified by this mask is set, the `ATSUBatchBreakLines` function is available.
- [gestaltATSUTabSupportFeature](./api-1471588-atsui_attribute_selectors/gestaltatsutabsupportfeature.md)
  If the bit specified by this mask is set, support for tabs is available.
- [gestaltATSUDirectAccess](./api-1471588-atsui_attribute_selectors/gestaltatsudirectaccess.md)
  If the bit specified by this mask is set, ATSU direct-access functions are available. These functions let you access glyph information directly.
- [gestaltATSUDecimalTabFeature](./api-1471588-atsui_attribute_selectors/gestaltatsudecimaltabfeature.md)
  If the bit specified by this mask is set, your application can set a decimal tab character.
- [gestaltATSUBiDiCursorPositionFeature](./api-1471588-atsui_attribute_selectors/gestaltatsubidicursorpositionfeature.md)
  If the bit specified by this mask is set, support for bidirectional cursor positioning is available.
- [gestaltATSUNearestCharLineBreakFeature](./api-1471588-atsui_attribute_selectors/gestaltatsunearestcharlinebreakfeature.md)
  If the bit specified by this mask is set, the nearest character line break feature is available.
- [gestaltATSUHighlightColorControlFeature](./api-1471588-atsui_attribute_selectors/gestaltatsuhighlightcolorcontrolfeature.md)
  If the bit specified by this mask is set, your application can control highlight color.
- [gestaltATSUUnderlineOptionsStyleFeature](./api-1471588-atsui_attribute_selectors/gestaltatsuunderlineoptionsstylefeature.md)
  If the bit specified by this mask is set, underline options are available.
- [gestaltATSUStrikeThroughStyleFeature](./api-1471588-atsui_attribute_selectors/gestaltatsustrikethroughstylefeature.md)
  If the bit specified by this mask is set, strike through styles are available.
- [gestaltATSUDropShadowStyleFeature](./api-1471588-atsui_attribute_selectors/gestaltatsudropshadowstylefeature.md)
  If the bit specified by this mask is set, drop shadow features are available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1471588-atsui_attribute_selectors)*