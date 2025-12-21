# VTIsStereoMVHEVCEncodeSupported()

**Framework**: Video Toolbox  
**Kind**: func

Returns a Boolean value that indicates whether the system supports MV-HEVC encoding.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func VTIsStereoMVHEVCEncodeSupported() -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the system supports MV-HEVC encoding; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

A return value of [`true`](https://developer.apple.com/documentation/Swift/true) doesn’t guarantee that encoding resources are available at all times.

## See Also

- [func VTCompressionSessionEncodeMultiImageFrame(VTCompressionSession, taggedBuffers: [CMTaggedBuffer], presentationTimeStamp: CMTime, duration: CMTime, frameProperties: CFDictionary?, infoFlagsOut: UnsafeMutablePointer<VTEncodeInfoFlags>?, outputHandler: VTCompressionOutputHandler) -> OSStatus](vtcompressionsessionencodemultiimageframe(_:taggedbuffers:presentationtimestamp:duration:frameproperties:infoflagsout:outputhandler:).md)
  Passes a multi-image frame to a compression session for encoding and provides a callback to handle the output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtisstereomvhevcencodesupported())*