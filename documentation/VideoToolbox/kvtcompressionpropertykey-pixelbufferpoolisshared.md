# kVTCompressionPropertyKey_PixelBufferPoolIsShared

**Framework**: Videotoolbox  
**Kind**: var

A Boolean value indicating whether the common pixel buffer pool is shared between the video encoder and the session client.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
let kVTCompressionPropertyKey_PixelBufferPoolIsShared: CFString
```

#### Discussion

This value is `false` if separate pools are used because the video encoder’s and the client’s pixel buffer attributes were incompatible.

## See Also

- [let kVTCompressionPropertyKey_NumberOfPendingFrames: CFString](kvtcompressionpropertykey_numberofpendingframes.md)
  The number of pending frames in the compression session.
- [let kVTCompressionPropertyKey_VideoEncoderPixelBufferAttributes: CFString](kvtcompressionpropertykey_videoencoderpixelbufferattributes.md)
  The video encoder’s pixel buffer attributes for the compression session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/kvtcompressionpropertykey_pixelbufferpoolisshared)*