# kVTCompressionPropertyKey_RealTime

**Framework**: Video Toolbox  
**Kind**: var

A Boolean value indicating whether it’s recommended that the video encoder perform compression in real time.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
let kVTCompressionPropertyKey_RealTime: CFString
```

#### Discussion

For offline compression, clients may set this property to [`kCFBooleanFalse`](https://developer.apple.com/documentation/CoreFoundation/kCFBooleanFalse), which indicates that it is OK for the video encoder to work slower than real time in order to produce a better result.

For real-time compression, clients may set this property to [`kCFBooleanTrue`](https://developer.apple.com/documentation/CoreFoundation/kCFBooleanTrue) to recommend that encoding stay timely.

By default, this property is `NULL`, indicating unknown.

## See Also

- [let kVTCompressionPropertyKey_MaxFrameDelayCount: CFString](kvtcompressionpropertykey_maxframedelaycount.md)
  The maximum number of frames that a compressor is allowed to hold before it must output a compressed frame.
- [let kVTCompressionPropertyKey_MaxH264SliceBytes: CFString](kvtcompressionpropertykey_maxh264slicebytes.md)
  The maximum slice size for H.264 encoding.
- [let kVTCompressionPropertyKey_MaximizePowerEfficiency: CFString](kvtcompressionpropertykey_maximizepowerefficiency.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/kvtcompressionpropertykey_realtime)*