# VTFrameSilo

**Framework**: Videotoolbox

An object that stores sample buffers from a multipass encoding session.

#### Overview

A frame silo object starts out empty and is populated by calls to [`VTFrameSiloAddSampleBuffer(_:sampleBuffer:)`](vtframesiloaddsamplebuffer(_:samplebuffer:).md) to add sample buffers in ascending decode order. After the first full pass, additional passes may be performed to replace sample buffers. Each such pass must begin with a call to [`VTFrameSiloSetTimeRangesForNextPass(_:timeRangeCount:timeRangeArray:)`](vtframesilosettimerangesfornextpass(_:timerangecount:timerangearray:).md), which takes a list of time ranges. Samples in these time ranges are deleted, and calls to [`VTFrameSiloAddSampleBuffer(_:sampleBuffer:)`](vtframesiloaddsamplebuffer(_:samplebuffer:).md) can then be made to provide replacements.

Call [`VTFrameSiloCallFunctionForEachSampleBuffer(_:in:refcon:callback:)`](vtframesilocallfunctionforeachsamplebuffer(_:in:refcon:callback:).md) or [`VTFrameSiloCallBlockForEachSampleBuffer(_:in:handler:)`](vtframesilocallblockforeachsamplebuffer(_:in:handler:).md) to retrieve sample buffers. The frame silo object may write sample buffers and data to the backing file between addition and retrieval; don’t expect to get identical object pointers back.

The sample buffers are ordered by decode timestamp.

## Topics

### Creating Frame Silos
- [func VTFrameSiloCreate(allocator: CFAllocator?, fileURL: CFURL?, timeRange: CMTimeRange, options: CFDictionary?, frameSiloOut: UnsafeMutablePointer<VTFrameSilo?>) -> OSStatus](vtframesilocreate(allocator:fileurl:timerange:options:framesiloout:).md)
  Creates a frame silo object using a temporary file.
### Configuring Frame Silos
- [func VTFrameSiloAddSampleBuffer(VTFrameSilo, sampleBuffer: CMSampleBuffer) -> OSStatus](vtframesiloaddsamplebuffer(_:samplebuffer:).md)
  Adds a sample buffer to a frame silo object.
- [func VTFrameSiloSetTimeRangesForNextPass(VTFrameSilo, timeRangeCount: CMItemCount, timeRangeArray: UnsafePointer<CMTimeRange>) -> OSStatus](vtframesilosettimerangesfornextpass(_:timerangecount:timerangearray:).md)
  Begins a new pass of samples to be added to a frame silo object.
- [func VTFrameSiloCallBlockForEachSampleBuffer(VTFrameSilo, in: CMTimeRange, handler: (CMSampleBuffer) -> OSStatus) -> OSStatus](vtframesilocallblockforeachsamplebuffer(_:in:handler:).md)
  Retrieves sample buffers from a frame silo object.
- [func VTFrameSiloCallFunctionForEachSampleBuffer(VTFrameSilo, in: CMTimeRange, refcon: UnsafeMutableRawPointer?, callback: (UnsafeMutableRawPointer?, CMSampleBuffer) -> OSStatus) -> OSStatus](vtframesilocallfunctionforeachsamplebuffer(_:in:refcon:callback:).md)
  Retrieves sample buffers from a frame silo object.
### Inspecting Frame Silos
- [func VTFrameSiloGetProgressOfCurrentPass(VTFrameSilo, progressOut: UnsafeMutablePointer<Float32>) -> OSStatus](vtframesilogetprogressofcurrentpass(_:progressout:).md)
  Gets the progress of the current pass.
- [func VTFrameSiloGetTypeID() -> CFTypeID](vtframesilogettypeid().md)
  Retrieves the Core Foundation type identifier for the frame silo object.
### Data Types
- [class VTFrameSilo](vtframesilo.md)
  An object that stores a large number of sample buffers, as produced by a multipass compression session.

## See Also

- [Encoding video for low-latency conferencing](encoding-video-for-low-latency-conferencing.md)
  Configure a compression session to optimize encoding for video-conferencing apps.
- [Encoding video for live streaming](encoding-video-for-live-streaming.md)
  Configure a compression session to encode video for live streaming.
- [Encoding video for offline transcoding](encoding-video-for-offline-transcoding.md)
  Configure a compression session to transcode video in offline workflows.
- [VTCompressionSession](vtcompressionsession-api-collection.md)
  An object that compresses video data.
- [VTDecompressionSession](vtdecompressionsession-api-collection.md)
  An object that decompresses video data.
- [VTMultiPassStorage](vtmultipassstorage-api-collection.md)
  An object that stores video encoding metadata from a multipass encoding session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtframesilo-api-collection)*