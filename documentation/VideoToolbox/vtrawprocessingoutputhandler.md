# VTRAWProcessingOutputHandler

**Framework**: Video Toolbox  
**Kind**: typealias  
**Role**: Type Alias

A block the system calls when frame processing is complete.

**Availability**:
- macOS 15.0+

## Declaration

```c
typedef void (^)(int, struct __CVBuffer *) VTRAWProcessingOutputHandler;
```

#### Discussion

On successful processing, will return a CVPixelBuffer conforming to the session’s outputPixelBufferAttributes if any were provided.

## See Also

### Data types
- [class VTRAWProcessingSession](./vtrawprocessingsession.md)
  An object that processes frames in camera native formats such as RAW or Bayer.
- [VTRAWProcessingParameterChangeHandler](./vtrawprocessingparameterchangehandler.md)
  A function the system calls when processing parameters change.
- [VTRAWProcessingSessionSetParameterChangedHander](./vtrawprocessingsessionsetparameterchangedhander.md)
  Provides a block which will be called when the session changes the set of processing parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtrawprocessingoutputhandler)*