# VTCompressionSessionEndPass(_:furtherPassesRequestedOut:_:)

**Framework**: Videotoolbox  
**Kind**: func

Marks the end of a compression pass.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
func VTCompressionSessionEndPass(_ session: VTCompressionSession, furtherPassesRequestedOut: UnsafeMutablePointer<DarwinBoolean>?, _ reserved: UnsafeMutablePointer<UInt32>?) -> OSStatus
```

#### Discussion

This function can take a long time, because the video encoder may perform significant processing between passes. You indicate with the `furtherPassesRequestedOut` argument whether the video encoder is requesting another pass.  There is no particular limit on the number of passes the video encoder may request, but the client is free to disregard this request and use the last-emitted set of frames.

It’s an error to call this function when multi-pass encoding has not been enabled by setting [`kVTCompressionPropertyKey_MultiPassStorage`](kvtcompressionpropertykey_multipassstorage.md).

## Parameters

- `session`: The compression session.
- `furtherPassesRequestedOut`: A pointer to a Boolean that is set to   if the video encoder requests to perform another pass,   otherwise. You may pass   to indicate that the client is certain to use this as the final pass, in which case the video encoder can skip that evaluation step.
- `reserved`: Reserved for future use and not currently used. Pass   for this argument.

## See Also

- [func VTCompressionSessionBeginPass(VTCompressionSession, flags: VTCompressionSessionOptionFlags, UnsafeMutablePointer<UInt32>?) -> OSStatus](vtcompressionsessionbeginpass(_:flags:_:).md)
  Marks the start of a specific compression pass.
- [func VTCompressionSessionGetTimeRangesForNextPass(VTCompressionSession, timeRangeCountOut: UnsafeMutablePointer<CMItemCount>, timeRangeArrayOut: UnsafeMutablePointer<UnsafePointer<CMTimeRange>?>) -> OSStatus](vtcompressionsessiongettimerangesfornextpass(_:timerangecountout:timerangearrayout:).md)
  Retrieves the time ranges for the next pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtcompressionsessionendpass(_:furtherpassesrequestedout:_:))*