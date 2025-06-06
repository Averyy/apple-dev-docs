# kVTCompressionPropertyKey_MVHEVCLeftAndRightViewIDs

**Framework**: Videotoolbox  
**Kind**: var

Specifies which view identifier corresponds to the left eye and right eye.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
let kVTCompressionPropertyKey_MVHEVCLeftAndRightViewIDs: CFString
```

#### Discussion

This property is specific to MV-HEVC.

The property value is an array containing two view identifiers as numbers. The first value corresponds to the left eye and the second value corresponds to the right. The system incorporates the view identifiers into the 3D Reference Displays Info SEI message.

The property is NULL by default.

## See Also

- [let kVTCompressionPropertyKey_MVHEVCVideoLayerIDs: CFString](kvtcompressionpropertykey_mvhevcvideolayerids.md)
  The identifiers of the video layers to encode in a multiview encoding operation.
- [let kVTCompressionPropertyKey_MVHEVCViewIDs: CFString](kvtcompressionpropertykey_mvhevcviewids.md)
  The identifiers of the views corresponding to the video layers in a multiview encoding operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/kvtcompressionpropertykey_mvhevcleftandrightviewids)*