# kVTCompressionPropertyKey_MaxFrameDelayCount

**Framework**: Video Toolbox  
**Kind**: var

The maximum number of frames that a compressor is allowed to hold before it must output a compressed frame.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
let kVTCompressionPropertyKey_MaxFrameDelayCount: CFString
```

#### Discussion

This value limits the number of frames that may be held in the compression window. If the maximum frame delay count is M, then before the call to encode frame N returns, frame N-M must have been emitted. The default is [`kVTUnlimitedFrameDelayCount`](kvtunlimitedframedelaycount.md), which sets no limit on the compression window.

## Topics

### Delay Counts
- [var kVTUnlimitedFrameDelayCount: Int](kvtunlimitedframedelaycount.md)
  Indicates that no limit should be set on the compression window.

## See Also

- [let kVTCompressionPropertyKey_MaxH264SliceBytes: CFString](kvtcompressionpropertykey_maxh264slicebytes.md)
  The maximum slice size for H.264 encoding.
- [let kVTCompressionPropertyKey_MaximizePowerEfficiency: CFString](kvtcompressionpropertykey_maximizepowerefficiency.md)
- [let kVTCompressionPropertyKey_RealTime: CFString](kvtcompressionpropertykey_realtime.md)
  A Boolean value indicating whether it’s recommended that the video encoder perform compression in real time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/kvtcompressionpropertykey_maxframedelaycount)*