# VTFrameSiloAddSampleBuffer(_:sampleBuffer:)

**Framework**: Video Toolbox  
**Kind**: func

Adds a sample buffer to a frame silo object.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
func VTFrameSiloAddSampleBuffer(_ silo: VTFrameSilo, sampleBuffer: CMSampleBuffer) -> OSStatus
```

#### Return Value

`kVTFrameSiloInvalidTimeRangeErr` if an attempt is made to add a sample buffer with an inappropriate decode timestamp.

#### Discussion

Within each pass, sample buffers must have strictly increasing decode timestamps. Passes after the first pass begin with a call to [`VTFrameSiloSetTimeRangesForNextPass(_:timeRangeCount:timeRangeArray:)`](vtframesilosettimerangesfornextpass(_:timerangecount:timerangearray:).md).

After a call to [`VTFrameSiloSetTimeRangesForNextPass(_:timeRangeCount:timeRangeArray:)`](vtframesilosettimerangesfornextpass(_:timerangecount:timerangearray:).md), sample buffer decode timestamps must also be within the stated time ranges. Note that time ranges are considered to contain their start times but not their end times.

## Parameters

- `silo`: The frame silo object.
- `sampleBuffer`: The sample buffer to add to the frame silo.

## See Also

- [func VTFrameSiloSetTimeRangesForNextPass(VTFrameSilo, timeRangeCount: CMItemCount, timeRangeArray: UnsafePointer<CMTimeRange>) -> OSStatus](vtframesilosettimerangesfornextpass(_:timerangecount:timerangearray:).md)
  Begins a new pass of samples to be added to a frame silo object.
- [func VTFrameSiloCallBlockForEachSampleBuffer(VTFrameSilo, in: CMTimeRange, handler: (CMSampleBuffer) -> OSStatus) -> OSStatus](vtframesilocallblockforeachsamplebuffer(_:in:handler:).md)
  Retrieves sample buffers from a frame silo object.
- [func VTFrameSiloCallFunctionForEachSampleBuffer(VTFrameSilo, in: CMTimeRange, refcon: UnsafeMutableRawPointer?, callback: (UnsafeMutableRawPointer?, CMSampleBuffer) -> OSStatus) -> OSStatus](vtframesilocallfunctionforeachsamplebuffer(_:in:refcon:callback:).md)
  Retrieves sample buffers from a frame silo object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtframesiloaddsamplebuffer(_:samplebuffer:))*