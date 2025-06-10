# VTCompressionSessionBeginPass(_:flags:_:)

**Framework**: Video Toolbox  
**Kind**: func

Marks the start of a specific compression pass.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
func VTCompressionSessionBeginPass(_ session: VTCompressionSession, flags beginPassFlags: VTCompressionSessionOptionFlags, _ reserved: UnsafeMutablePointer<UInt32>?) -> OSStatus
```

#### Discussion

During multipass encoding, this function must be called before [`VTCompressionSessionEncodeFrame(_:imageBuffer:presentationTimeStamp:duration:frameProperties:sourceFrameRefcon:infoFlagsOut:)`](vtcompressionsessionencodeframe(_:imagebuffer:presentationtimestamp:duration:frameproperties:sourceframerefcon:infoflagsout:).md).

It’s an error to call this function when multipass encoding is not enabled by setting [`kVTCompressionPropertyKey_MultiPassStorage`](kvtcompressionpropertykey_multipassstorage.md).

## Parameters

- `session`: A compression session.
- `beginPassFlags`: Pass   to inform the encoder that the pass must be the final pass.
- `reserved`: A reserved value.

## Topics

### Option Flags
- [struct VTCompressionSessionOptionFlags](vtcompressionsessionoptionflags.md)
  Flags to pass to a compression session.

## See Also

- [func VTCompressionSessionEndPass(VTCompressionSession, furtherPassesRequestedOut: UnsafeMutablePointer<DarwinBoolean>?, UnsafeMutablePointer<UInt32>?) -> OSStatus](vtcompressionsessionendpass(_:furtherpassesrequestedout:_:).md)
  Marks the end of a compression pass.
- [func VTCompressionSessionGetTimeRangesForNextPass(VTCompressionSession, timeRangeCountOut: UnsafeMutablePointer<CMItemCount>, timeRangeArrayOut: UnsafeMutablePointer<UnsafePointer<CMTimeRange>?>) -> OSStatus](vtcompressionsessiongettimerangesfornextpass(_:timerangecountout:timerangearrayout:).md)
  Retrieves the time ranges for the next pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtcompressionsessionbeginpass(_:flags:_:))*