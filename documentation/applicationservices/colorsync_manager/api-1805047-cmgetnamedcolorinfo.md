# CMGetNamedColorInfo

**Framework**: Application Services  
**Kind**: func

Obtains information about a named color space from its profile reference.

## Declaration

```c
CMError CMGetNamedColorInfo (
   CMProfileRef prof,
   UInt32 *deviceChannels,
   OSType *deviceColorSpace,
   OSType *PCSColorSpace,
   UInt32 *count,
   StringPtr prefix,
   StringPtr suffix
);
```

## Return Value

A `CMError` value. See [Result Codes](../colorsync_manager.md#1670295).

## Overview

The `CMGetNamedColorInfo` function returns information about the named color space referred to by the passed profile reference. 

## Parameters

- `prof`: A profile reference of type [`CMProfileRef`](../cmprofileref.md) to a named color space profile to obtain named color information from. 
- `deviceChannels`: A pointer to a count value. On return, the number of device channels in the color space for the profile. It should agree with the “data color space” field in the profile header. For example, Pantone maps to CMYK, a four-channel color space. A value of 0 indicates no device channels were available. 
- `deviceColorSpace`: A pointer to a device color space. On return, a device color space, such as CMYK. 
- `PCSColorSpace`: A pointer to a profile connection space color space. On return, an interchange color space, such as Lab.
- `count`: A pointer to a count value. On return, the number of named colors in the profile.
- `prefix`: A pointer to a Pascal string. On return, the string contains a prefix, such as “Pantone”, for each color name. The prefix identifies the named color system described by the profile. 
- `suffix`: A pointer to a Pascal string. On return, the string contains a suffix for each color name, such as “CVC”.

## See Also

### Accessing Name-Class Profiles
- [CMGetNamedColorValue](./api-1805053-cmgetnamedcolorvalue.md)
  Obtains device and PCS color values for a specific color name from a named color space profile.
- [CMGetIndNamedColorValue](./api-1805059-cmgetindnamedcolorvalue.md)
  Obtains device and PCS color values for a specific named color index from a named color space profile.
- [CMGetNamedColorIndex](./api-1805065-cmgetnamedcolorindex.md)
  Obtains a named color index for a specific color name from a named color space profile.
- [CMGetNamedColorName](./api-1805072-cmgetnamedcolorname.md)
  Obtains a named color name for a specific named color index from a named color space profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805047-cmgetnamedcolorinfo)*