# VTRAWProcessingSessionProcessFrame

**Framework**: Video Toolbox  
**Kind**: func  
**Role**: Function

Submits RAW frames for format-specific processing using sequence and frame level parameters.

**Availability**:
- macOS 15.0+

## Declaration

```c
extern OSStatus VTRAWProcessingSessionProcessFrame(VTRAWProcessingSessionRef session, CVPixelBufferRef inputPixelBuffer, CFDictionaryRef frameOptions, VTRAWProcessingOutputHandler outputHandler);
```

#### Discussion

Processed frames may or may not be output before the function returns. The client should not modify the input pixel data after making this call. The RAW Processor will retain the input pixel buffer as long as necessary.

For any RAW processor, there is a finite number of frames that can be  presented to [`VTRAWProcessingSessionProcessFrame`](./vtrawprocessingsessionprocessframe.md) before the function will block until the output callback is invoked.

## Parameters

- `session`: The RAW processing session.
- `inputPixelBuffer`: A pixel buffer that contains an input video frame to process.
- `frameOptions`: Contains key/value pairs specifying additional properties for processing this frame. No keys currently. Pass `NULL`.
- `outputHandler`: A [`VTRAWProcessingOutputHandler`](./vtrawprocessingoutputhandler.md) block which will be called once when processing is complete.

## See Also

### Processing frames
- [VTRAWProcessingSessionCompleteFrames](./vtrawprocessingsessioncompleteframes.md)
  Forces the RAW Processor to complete processing frames.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtrawprocessingsessionprocessframe)*