# Rendering Intent Values for Version 2.x Profiles

**Framework**: Application Services

Define the four possible values for the rendering intent bits of the `renderingIntent` field of the `CM2Header` structure. 

#### Overview

The ColorSync Manager defines the structure [`CM2Header`](cm2header.md) to represent the profile header for the version 2.x profile format defined by the ICC. The `renderingIntent` field of the `CM2Header` structure is an unsigned long value whose bits specify information about a profile. The ICC reserves the use of bits 0 to 15 and has assigned values to bits 0 and 1. Bits 16 to 31 are reserved for use by color management system (CMS) vendors.

Rendering intent controls the approach a CMM uses to translate the colors of an image to the color gamut of a destination device. Your application can set a profile’s rendering intent, for example, based on a user’s choice of the preferred approach for rendering an image.

Because rendering intent is specified by the low two bits, and because no other bits are currently defined for this field, you can use the constants defined here to test or set the value of the entire field, without concern for possible information stored in other bits. 

## Topics

### Constants
- [var cmPerceptual: Int](cmperceptual.md)
  All the colors of a given gamut can be scaled to fit within another gamut. This intent is best suited to realistic images, such as photographic images.
- [var cmRelativeColorimetric: Int](cmrelativecolorimetric.md)
  The colors that fall within the gamuts of both devices are left unchanged. This intent is best suited to logo images.
- [var cmSaturation: Int](cmsaturation.md)
  The relative saturation of colors is maintained from gamut to gamut. This intent is best suited to bar graphs and pie charts in which the actual color displayed is less important than its vividness.
- [var cmAbsoluteColorimetric: Int](cmabsolutecolorimetric.md)
  This approach is based on a device-independent color space in which the result is an idealized print viewed on an ideal type of paper having a large dynamic range and color gamut.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1560278-rendering_intent_values_for_vers)*