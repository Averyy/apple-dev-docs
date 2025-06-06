# UCKeyLayoutFeatureInfo

**Framework**: Core Services  
**Kind**: struct

Specifies the longest possible output string to be produced by the current `'uchr'` resource.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
struct UCKeyLayoutFeatureInfo
```

#### Overview

The Unicode keyboard-layout ( `'uchr'`) resource contains the data necessary to map virtual key codes to Unicode character codes for a given keyboard layout. The `'uchr'` format consists of a header information section and five key mapping data sections. The `UCKeyLayoutFeatureInfo` type is used in the header section of the `'uchr'` resource. 

## Topics

### Initializers
- [init()](uckeylayoutfeatureinfo/1442653-init.md)
- [init(keyLayoutFeatureInfoFormat: UInt16, reserved: UInt16, maxOutputStringLength: UInt32)](uckeylayoutfeatureinfo/1445182-init.md)
### Instance Properties
- [var keyLayoutFeatureInfoFormat: UInt16](uckeylayoutfeatureinfo/1390617-keylayoutfeatureinfoformat.md)
  An unsigned 16-bit integer identifying the format of the `UCKeyLayoutFeatureInfo` structure. Set to `kUCKeyLayoutFeatureInfoFormat`.
- [var maxOutputStringLength: UInt32](uckeylayoutfeatureinfo/1390572-maxoutputstringlength.md)
  An unsigned 32-bit integer specifying the longest possible output string of Unicode characters to be produced by this `'uchr'` resource.
- [var reserved: UInt16](uckeylayoutfeatureinfo/1390566-reserved.md)
  Reserved. Set to 0.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/uckeylayoutfeatureinfo)*