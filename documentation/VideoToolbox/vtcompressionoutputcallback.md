# VTCompressionOutputCallback

**Framework**: Video Toolbox  
**Kind**: typealias

A callback for the system to invoke when it’s finished compressing a frame.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
typealias VTCompressionOutputCallback = (UnsafeMutableRawPointer?, UnsafeMutableRawPointer?, OSStatus, VTEncodeInfoFlags, CMSampleBuffer?) -> Void
```

#### Discussion

When you create a compression session, you pass in a callback function to be called for compressed frames.  This function is called in decode order (which is not necessarily the same as display order).

## Parameters

- `outputCallbackRefCon`: The callback’s reference value.
- `sourceFrameRefCon`: The frame’s reference value, copied from the   argument to  .
- `status`:   if compression was successful; an error code if compression wasn’t successful.
- `infoFlags`: The   bit may be set if the frame was dropped.
- `sampleBuffer`: Contains the compressed frame if compression was successful and the frame wasn’t dropped; otherwise,  .

## See Also

- [typealias VTCompressionOutputHandler](vtcompressionoutputhandler.md)
  A callback for the system to invoke when it’s finished compressing a frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtcompressionoutputcallback)*