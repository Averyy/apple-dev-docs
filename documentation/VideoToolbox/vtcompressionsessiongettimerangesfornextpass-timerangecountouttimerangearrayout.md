# VTCompressionSessionGetTimeRangesForNextPass(_:timeRangeCountOut:timeRangeArrayOut:)

**Framework**: Videotoolbox  
**Kind**: func

Retrieves the time ranges for the next pass.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
func VTCompressionSessionGetTimeRangesForNextPass(_ session: VTCompressionSession, timeRangeCountOut: UnsafeMutablePointer<CMItemCount>, timeRangeArrayOut: UnsafeMutablePointer<UnsafePointer<CMTimeRange>?>) -> OSStatus
```

#### Discussion

If [`VTCompressionSessionEndPass(_:furtherPassesRequestedOut:_:)`](vtcompressionsessionendpass(_:furtherpassesrequestedout:_:).md) sets `furtherPassesRequestedOut` to [`true`](https://developer.apple.com/documentation/swift/true), call this function to find out the time ranges for the next pass.  Source frames outside these time ranges should be skipped. Each time range includes any frame at its start time and does not include any frame at its end time.

It’s an error to call this function when multipass encoding has not been enabled by setting [`kVTCompressionPropertyKey_MultiPassStorage`](kvtcompressionpropertykey_multipassstorage.md), or when `VTCompressionSessionEndPass` did not set f`urtherPassesRequestedOut` to [`true`](https://developer.apple.com/documentation/swift/true).

## Parameters

- `session`: The compression session.
- `timeRangeCountOut`: A pointer to the item count ( ) to receive the number of  .
- `timeRangeArrayOut`: A pointer to a C array of  . The storage for this array belongs to the compression session and should not be modified.The pointer is valid until the next call to  , or until the compression session is invalidated or finalized.

## See Also

- [func VTCompressionSessionBeginPass(VTCompressionSession, flags: VTCompressionSessionOptionFlags, UnsafeMutablePointer<UInt32>?) -> OSStatus](vtcompressionsessionbeginpass(_:flags:_:).md)
  Marks the start of a specific compression pass.
- [func VTCompressionSessionEndPass(VTCompressionSession, furtherPassesRequestedOut: UnsafeMutablePointer<DarwinBoolean>?, UnsafeMutablePointer<UInt32>?) -> OSStatus](vtcompressionsessionendpass(_:furtherpassesrequestedout:_:).md)
  Marks the end of a compression pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtcompressionsessiongettimerangesfornextpass(_:timerangecountout:timerangearrayout:))*