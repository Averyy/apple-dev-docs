# Default CMM Signature

**Framework**: Application Services

Specifies a signature for the default color management module supplied by Color Sync.

#### Overview

A color management module (CMM) uses profiles to convert and match a color in a given color space on a given device to or from another color space or device. 

To specify the default CMM, set the `CMMType` field of the profile header to the default signature defined by the following enumeration. You use a structure of type [`CM2Header`](cm2header.md) for a ColorSync 2.x profile and a structure of type `CMHeader` for a 1.0 profile header. 

## Topics

### Constants
- [var kDefaultCMMSignature: Int](kdefaultcmmsignature.md)
  Signature for the default CMM supplied with the ColorSync Manager.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1560689-default_cmm_signature)*