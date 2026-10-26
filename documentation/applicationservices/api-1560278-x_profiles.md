# Rendering Intent Values for Version 2.x Profiles

**Framework**: Application Services  
**Kind**: enum  
**Role**: Enumeration

Define the four possible values for the rendering intent bits of the `renderingIntent` field of the `CM2Header` structure. 

**Availability**:
- macOS 10.0+

## Declaration

```c
enum : unsigned int {
    ...
};
```

## Topics

### Constants
- [cmPerceptual](./api-1560278-x_profiles/cmperceptual.md)
  All the colors of a given gamut can be scaled to fit within another gamut. This intent is best suited to realistic images, such as photographic images.
- [cmRelativeColorimetric](./api-1560278-x_profiles/cmrelativecolorimetric.md)
  The colors that fall within the gamuts of both devices are left unchanged. This intent is best suited to logo images.
- [cmSaturation](./api-1560278-x_profiles/cmsaturation.md)
  The relative saturation of colors is maintained from gamut to gamut. This intent is best suited to bar graphs and pie charts in which the actual color displayed is less important than its vividness.
- [cmAbsoluteColorimetric](./api-1560278-x_profiles/cmabsolutecolorimetric.md)
  This approach is based on a device-independent color space in which the result is an idealized print viewed on an ideal type of paper having a large dynamic range and color gamut.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1560278-x_profiles)*