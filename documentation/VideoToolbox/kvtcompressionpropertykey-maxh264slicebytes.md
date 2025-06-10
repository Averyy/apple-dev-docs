# kVTCompressionPropertyKey_MaxH264SliceBytes

**Framework**: Video Toolbox  
**Kind**: var

The maximum slice size for H.264 encoding.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
let kVTCompressionPropertyKey_MaxH264SliceBytes: CFString
```

#### Discussion

If supported by an H.264 encoder, the value limits the size in bytes of slices produced by the encoder, where possible. By default, no limit is specified.  A value of zero implies default behavior.

## See Also

- [let kVTCompressionPropertyKey_MaxFrameDelayCount: CFString](kvtcompressionpropertykey_maxframedelaycount.md)
  The maximum number of frames that a compressor is allowed to hold before it must output a compressed frame.
- [let kVTCompressionPropertyKey_MaximizePowerEfficiency: CFString](kvtcompressionpropertykey_maximizepowerefficiency.md)
- [let kVTCompressionPropertyKey_RealTime: CFString](kvtcompressionpropertykey_realtime.md)
  A Boolean value indicating whether it’s recommended that the video encoder perform compression in real time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/kvtcompressionpropertykey_maxh264slicebytes)*