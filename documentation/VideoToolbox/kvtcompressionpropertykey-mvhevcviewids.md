# kVTCompressionPropertyKey_MVHEVCViewIDs

**Framework**: Videotoolbox  
**Kind**: var

The identifiers of the views corresponding to the video layers in a multiview encoding operation.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
let kVTCompressionPropertyKey_MVHEVCViewIDs: CFString
```

#### Discussion

This property is specific to MV-HEVC.

The entries in the specified array should be in the same order and have the same count as the value specified in [`kVTCompressionPropertyKey_MVHEVCVideoLayerIDs`](kvtcompressionpropertykey_mvhevcvideolayerids.md).

The default value is `NULL`.

## See Also

- [let kVTCompressionPropertyKey_MVHEVCVideoLayerIDs: CFString](kvtcompressionpropertykey_mvhevcvideolayerids.md)
  The identifiers of the video layers to encode in a multiview encoding operation.
- [let kVTCompressionPropertyKey_MVHEVCLeftAndRightViewIDs: CFString](kvtcompressionpropertykey_mvhevcleftandrightviewids.md)
  Specifies which view identifier corresponds to the left eye and right eye.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/kvtcompressionpropertykey_mvhevcviewids)*