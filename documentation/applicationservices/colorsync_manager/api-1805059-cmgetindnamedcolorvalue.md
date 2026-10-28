# CMGetIndNamedColorValue

**Framework**: Application Services  
**Kind**: func

Obtains device and PCS color values for a specific named color index from a named color space profile.

## Declaration

```c
CMError CMGetIndNamedColorValue (
   CMProfileRef prof,
   UInt32 index,
   CMColor *deviceColor,
   CMColor *PCSColor
);
```

## Return Value

A `CMError` value. See [Result Codes](../colorsync_manager.md#1670295).

## Overview

Based on the passed named color index, the `CMGetIndNamedColorValue` function does a lookup into the named color tag and returns device and PCS values. If the index is greater than the number of named colors, `CMGetIndNamedColorValue` returns an error code. 

## Parameters

- `prof`: A profile reference of type [`CMProfileRef`](../cmprofileref.md) to a named color space profile to obtain color values from. 
- `index`: A one-based index value for a named color. 
- `deviceColor`: A pointer to a device color. On return, a device color value in `CMColor` union format. If the profile does not contain device values, `deviceColor` is undefined. 
- `PCSColor`: A pointer to a profile connection space color. On return, an interchange color value in `CMColor` union format.

## See Also

### Accessing Name-Class Profiles
- [CMGetNamedColorInfo](./api-1805047-cmgetnamedcolorinfo.md)
  Obtains information about a named color space from its profile reference.
- [CMGetNamedColorValue](./api-1805053-cmgetnamedcolorvalue.md)
  Obtains device and PCS color values for a specific color name from a named color space profile.
- [CMGetNamedColorIndex](./api-1805065-cmgetnamedcolorindex.md)
  Obtains a named color index for a specific color name from a named color space profile.
- [CMGetNamedColorName](./api-1805072-cmgetnamedcolorname.md)
  Obtains a named color name for a specific named color index from a named color space profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805059-cmgetindnamedcolorvalue)*