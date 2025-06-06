# Device Attribute Values for Version 2.x Profiles

**Framework**: Application Services

Define masks your application can use to set or test bits in the `deviceAttributes `field of the `CM2Header` structure.

#### Overview

The ColorSync Manager defines the structure [`CM2Header`](cm2header.md) to represent the profile header for the version 2.x profile format defined by the ICC.The `deviceAttributes` field of the `CM2Header` structure is an array of two unsigned long values whose bits specify information about a profile. The ICC reserves the use of `deviceAttributes[1]` and has assigned values to bits 0 and 1. All the bits of `deviceAttributes[0]` are reserved for use by color management system (CMS) vendors.  

## Topics

### Constants
- [var cmReflectiveTransparentMask: Int](cmreflectivetransparentmask.md)
- [var cmGlossyMatteMask: Int](cmglossymattemask.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1560447-device_attribute_values_for_vers)*