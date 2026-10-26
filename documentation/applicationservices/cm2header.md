# CM2Header

**Framework**: Application Services  
**Kind**: struct  
**Role**: Structure

Contains information that supports the header format specified by the ICC format specification for version 2.x profiles.

**Availability**:
- macOS 10.0+ - Deprecated in 10.6

## Declaration

```c
typedef struct CM2Header {
    ...
} CM2Header;
```

#### Overview

The ColorSync Manager defines the `CM2header` profile structure to support the header format specified by the ICC format specification for version 2.x profiles. For a description of `CMHeader`, the ColorSync 1.0 profile header, see `CMHeader`. To obtain a copy of the International Color Consortium Profile Format Specification, or to get other information about the ICC, visit the ICC Web site at  [http://www.color.org/](http://www.color.org/).

Your application cannot obtain a discrete profile header value using the element tag scheme available for use with elements outside the header. Instead, to set or modify values of a profile header, your application must obtain the entire profile header using the function [CMGetProfileHeader](./colorsync_manager/api-1804879-cmgetprofileheader.md) and replace the header using the function [CMSetProfileHeader](./colorsync_manager/api-1804882-cmsetprofileheader.md).

## Topics

### Instance Properties
- [CMMType](./cm2header/api-1560656-cmmtype.md)
  The signature of the preferred CMM for color-matching and color-checking sessions for this profile. To avoid conflicts with other CMMs, this signature must be registered with the ICC. For the signature of the default CMM, see [Default CMM Signature](./api-1560689-default_cmm_signature.md).
- [CS2profileSignature](./cm2header/api-1560419-cs2profilesignature.md)
  The `'acsp'` constant as required by the ICC format.
- [creator](./cm2header/api-1560422-creator.md)
  Signature identifying the profile creator.
- [dataColorSpace](./cm2header/api-1560613-datacolorspace.md)
  The color space of the profile. Color values used to express colors of images using this profile are specified in this color space. For a list of the color space signatures, see [Color Space Signatures](./api-1560276-color_space_signatures.md).
- [dateTime](./cm2header/api-1560304-datetime.md)
  The date and time when the profile was created. You can use this value to keep track of your own versions of this profile. For information on the date and time format, see [`CMDateTime`](./cmdatetime.md). 
- [deviceAttributes](./cm2header/api-1560387-deviceattributes.md)
  Attributes that are unique to this particular device setup, such as media, paper, and ink types. The data type for this field is an array of two unsigned longs. The low word of `deviceAttributes[0]` is reserved by the ICC. The high word of `deviceAttributes[0]` and the entire word of `deviceAttributes[1]` are available for vendor use. For information on how the bits in `deviceAttributes` are defined and how your application can set and test them, see [Device Attribute Values for Version 2.x Profiles](./api-1560447-x_profiles.md).
- [deviceManufacturer](./cm2header/api-1560454-devicemanufacturer.md)
  The signature of the manufacturer of the device to which this profile applies. This value is registered with the ICC.
- [deviceModel](./cm2header/api-1560558-devicemodel.md)
  The model of this device, as registered with the ICC.
- [flags](./cm2header/api-1560100-flags.md)
  Flags that provide hints, such as preferred quality and speed options, to the preferred CMM. The `flags` field consists of an unsigned long data type. The 16 bits in the low word, 0-15, are reserved for use by the ICC. The 16 bits in the high word, 16-31, are available for use by color management systems. For information on how these bits are defined and how your application can set and test them, see [Flag Mask Definitions for Version 2.x Profiles](./api-1560699-x_profiles.md).
- [platform](./cm2header/api-1560245-platform.md)
  The signature of the primary platform on which this profile runs. For Apple Computer, this is `'APPL'`. For other platforms, refer to the International Color Consortium Profile Format Specification.
- [profileClass](./cm2header/api-1560336-profileclass.md)
  One of the seven profile classes supported by the ICC: input, display, output, named color space, device link, color space conversion, or abstract. For the signatures representing profile classes, see [Profile Classes](./api-1560630-profile_classes.md).
- [profileConnectionSpace](./cm2header/api-1560218-profileconnectionspace.md)
  The profile connection space, or PCS. The signatures for the two profile connection spaces supported by ColorSync, `cmXYZData` and `cmLabData`, are described in [Color Space Signatures](./api-1560276-color_space_signatures.md).
- [profileVersion](./cm2header/api-1560432-profileversion.md)
  The version of the profile format.
- [renderingIntent](./cm2header/api-1560282-renderingintent.md)
  The preferred rendering intent for the object or file tagged with this profile. Four types of rendering intent are defined: perceptual, relative colorimetric, saturation, and absolute colorimetric. The `renderingIntent` field consists of an unsigned long data type. The low word is reserved by the ICC and is used to set the rendering intent. The high word is available for use. For information on how the bits in `renderingIntent` are defined and how your application can set and test them, see [Rendering Intent Values for Version 2.x Profiles](./api-1560278-x_profiles.md).
- [reserved](./cm2header/api-1560629-reserved.md)
  This field is reserved for future use.
- [size](./cm2header/api-1560655-size.md)
  The total size in bytes of the profile.
- [white](./cm2header/api-1560149-white.md)
  The profile illuminant white reference point, expressed in the XYZ color space. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/cm2header)*