# VTRAWProcessingSessionCreate

**Framework**: Video Toolbox  
**Kind**: func  
**Role**: Function

Creates a RAW video frame processing session.

**Availability**:
- macOS 15.0+

## Declaration

```c
extern OSStatus VTRAWProcessingSessionCreate(CFAllocatorRef allocator, CMVideoFormatDescriptionRef formatDescription, CFDictionaryRef outputPixelBufferAttributes, CFDictionaryRef processingSessionOptions, VTRAWProcessingSessionRef*processingSessionOut);
```

## Parameters

- `allocator`: An allocator for the session. Pass `NULL` to use the default allocator.
- `formatDescription`: The [`CMVideoFormatDescription`](../CoreMedia/cmvideoformatdescription.md) corresponding to the original media samples, containing sequence-level processing parameters.
- `outputPixelBufferAttributes`: A CoreVideo pixel buffer attributes dictionary describing the client’s requirements for pixel buffers for output frames. Pass `NULL` to receive the RAW processor’s native output format.
- `processingSessionOptions`: A dictionary of creation-time options for the [VTRAWProcessingSession](./vtrawprocessingsession-api-collection.md).
- `processingSessionOut`: Points to a variable to receive the new RAW processing session. When you are done with the session, call [`VTRAWProcessingSessionInvalidate`](./vtrawprocessingsessioninvalidate.md) to tear it down and then `CFRelease` to release your object reference.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtrawprocessingsessioncreate)*