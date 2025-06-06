# VTCompressionOutputHandler

**Framework**: Videotoolbox  
**Kind**: typealias

A callback for the system to invoke when it’s finished compressing a frame.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
typealias VTCompressionOutputHandler = (OSStatus, VTEncodeInfoFlags, CMSampleBuffer?) -> Void
```

#### Discussion

When you encode a frame, you pass in a callback block to be called for that compressed frame.  This block is called in decode order (which is not necessarily the same as display order).

## Parameters

- `status`:   if compression was successful; an error code if compression was not successful.
- `infoFlags`: The   bit may be set if the frame was dropped.
- `sampleBuffer`: Contains the compressed frame if compression was successful and the frame was not dropped; otherwise,  .

## See Also

- [typealias VTCompressionOutputCallback](vtcompressionoutputcallback.md)
  A callback for the system to invoke when it’s finished compressing a frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtcompressionoutputhandler)*