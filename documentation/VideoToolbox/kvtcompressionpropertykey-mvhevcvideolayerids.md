# kVTCompressionPropertyKey_MVHEVCVideoLayerIDs

**Framework**: Videotoolbox  
**Kind**: var

The identifiers of the video layers to encode in a multiview encoding operation.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
let kVTCompressionPropertyKey_MVHEVCVideoLayerIDs: CFString
```

#### Discussion

This property is specific to MV-HEVC.

Specifying layer ID values advises the encoder to expect [`CMTaggedBufferGroupRef`](https://developer.apple.com/documentation/CoreMedia/CMTaggedBufferGroupRef) objects with specific [`CMTag`](https://developer.apple.com/documentation/CoreMedia/CMTag-swift.class) values that reference them.

The default value is `NULL`.

## See Also

- [let kVTCompressionPropertyKey_MVHEVCViewIDs: CFString](kvtcompressionpropertykey_mvhevcviewids.md)
  The identifiers of the views corresponding to the video layers in a multiview encoding operation.
- [let kVTCompressionPropertyKey_MVHEVCLeftAndRightViewIDs: CFString](kvtcompressionpropertykey_mvhevcleftandrightviewids.md)
  Specifies which view identifier corresponds to the left eye and right eye.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/kvtcompressionpropertykey_mvhevcvideolayerids)*