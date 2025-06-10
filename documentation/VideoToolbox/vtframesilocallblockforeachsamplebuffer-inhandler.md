# VTFrameSiloCallBlockForEachSampleBuffer(_:in:handler:)

**Framework**: Video Toolbox  
**Kind**: func

Retrieves sample buffers from a frame silo object.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
func VTFrameSiloCallBlockForEachSampleBuffer(_ silo: VTFrameSilo, in timeRange: CMTimeRange, handler: (CMSampleBuffer) -> OSStatus) -> OSStatus
```

#### Return Value

`kVTFrameSiloInvalidTimeRangeErr` if any time ranges are non-numeric, overlap, or are not in ascending order. Returns any nonzero status returned by the handler block.

#### Discussion

You call this function to retrieve sample buffers at the end of a multipass compression session.

## Parameters

- `silo`: The frame silo object.
- `timeRange`: The decode time range of sample buffers to retrieve. Pass   to retrieve all sample buffers from the  .
- `handler`: A block to be called, in decode order, with each sample buffer that was added. To abort iteration early, return a nonzero status. The   object may write sample buffers and data to the backing file between addition and retrieval;  do not expect to get identical object pointers back.

## See Also

- [func VTFrameSiloAddSampleBuffer(VTFrameSilo, sampleBuffer: CMSampleBuffer) -> OSStatus](vtframesiloaddsamplebuffer(_:samplebuffer:).md)
  Adds a sample buffer to a frame silo object.
- [func VTFrameSiloSetTimeRangesForNextPass(VTFrameSilo, timeRangeCount: CMItemCount, timeRangeArray: UnsafePointer<CMTimeRange>) -> OSStatus](vtframesilosettimerangesfornextpass(_:timerangecount:timerangearray:).md)
  Begins a new pass of samples to be added to a frame silo object.
- [func VTFrameSiloCallFunctionForEachSampleBuffer(VTFrameSilo, in: CMTimeRange, refcon: UnsafeMutableRawPointer?, callback: (UnsafeMutableRawPointer?, CMSampleBuffer) -> OSStatus) -> OSStatus](vtframesilocallfunctionforeachsamplebuffer(_:in:refcon:callback:).md)
  Retrieves sample buffers from a frame silo object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtframesilocallblockforeachsamplebuffer(_:in:handler:))*