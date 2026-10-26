# cmGamutCheckingMask

**Framework**: Application Services  
**Kind**: econst  
**Role**: Enumeration Case

**Availability**:
- macOS 10.0+

## Declaration

```c
cmGamutCheckingMask = 0x00080000
```

#### Discussion

This mask provides access to bit 19 of the `flags` field. When you use a profile to create a color world, bit 19 specifies whether the color world should include information for gamut checking. It has the value 0 if the color world should include a gamut-checking table, 1 if gamut-checking information is not required. ColorSync can create a color world without a gamut table more quickly and in less space.

Many applications do not perform gamut checking, so they should set this bit to 1. However, if you call a color checking function such as [CWCheckColors](../colorsync_manager/api-1805111-cwcheckcolors.md), or [CWMatchColors](../colorsync_manager/api-1805108-cwmatchcolors.md), after setting a profile’s gamut-checking bit so that the color world does not contain gamut information, these routines return the `cmCantGamutCheckError` error.

This feature is provided by the ColorSync Manager; it is not defined by the ICC profile specification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1560699-x_profiles/cmgamutcheckingmask)*