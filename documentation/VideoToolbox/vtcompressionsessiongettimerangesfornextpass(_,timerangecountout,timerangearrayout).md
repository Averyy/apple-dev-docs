# VTCompressionSessionGetTimeRangesForNextPass(_:timeRangeCountOut:timeRangeArrayOut:)

**Framework**: Video Toolbox  
**Kind**: func  
**Role**: Function

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

```c
extern OSStatus VTCompressionSessionGetTimeRangesForNextPass(VTCompressionSessionRef session, CMItemCount *timeRangeCountOut, const CMTimeRange **timeRangeArrayOut);
```

#### Discussion

If [`VTCompressionSessionEndPass(_:furtherPassesRequestedOut:_:)`](./vtcompressionsessionendpass%28_,furtherpassesrequestedout,_%29.md) sets `furtherPassesRequestedOut` to [`true`](../Swift/true.md), call this function to find out the time ranges for the next pass.  Source frames outside these time ranges should be skipped. Each time range includes any frame at its start time and does not include any frame at its end time.

It’s an error to call this function when multipass encoding has not been enabled by setting [`kVTCompressionPropertyKey_MultiPassStorage`](./kvtcompressionpropertykey_multipassstorage.md), or when `VTCompressionSessionEndPass` did not set f`urtherPassesRequestedOut` to [`true`](../Swift/true.md).

## Parameters

- `session`: The compression session.
- `timeRangeCountOut`: A pointer to the item count ([`CMItemCount`](../CoreMedia/cmitemcount.md)) to receive the number of `CMTimeRanges`.
- `timeRangeArrayOut`: A pointer to a C array of `CMTimeRanges`. The storage for this array belongs to the compression session and should not be modified.The pointer is valid until the next call to [`VTCompressionSessionEndPass(_:furtherPassesRequestedOut:_:)`](./vtcompressionsessionendpass%28_,furtherpassesrequestedout,_%29.md), or until the compression session is invalidated or finalized.

## See Also

### Performing Multiple Passes
- [func VTCompressionSessionBeginPass(VTCompressionSession, flags: VTCompressionSessionOptionFlags, UnsafeMutablePointer<UInt32>?) -> OSStatus](./vtcompressionsessionbeginpass%28_,flags,_%29.md)
  Marks the start of a specific compression pass.
- [func VTCompressionSessionEndPass(VTCompressionSession, furtherPassesRequestedOut: UnsafeMutablePointer<DarwinBoolean>?, UnsafeMutablePointer<UInt32>?) -> OSStatus](./vtcompressionsessionendpass%28_,furtherpassesrequestedout,_%29.md)
  Marks the end of a compression pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtcompressionsessiongettimerangesfornextpass(_:timerangecountout:timerangearrayout:))*