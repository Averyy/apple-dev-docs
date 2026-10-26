# VTRAWProcessingSessionSetParameterChangedHander

**Framework**: Video Toolbox  
**Kind**: func  
**Role**: Function

Provides a block which will be called when the session changes the set of processing parameters.

**Availability**:
- macOS 15.0+ - Deprecated in 26.0

## Declaration

```c
extern OSStatus VTRAWProcessingSessionSetParameterChangedHander(VTRAWProcessingSessionRef session, VTRAWProcessingParameterChangeHandler parameterChangeHandler);
```

## Parameters

- `session`: The RAW processing session.
- `parameterChangeHandler`: A [`VTRAWProcessingParameterChangeHandler`](./vtrawprocessingparameterchangehandler.md) block which will be called when the set of processing parameters changes, or the value of a parameter changes without the client explicitly requesting it. Setting this to `NULL` removes the current handler.

## See Also

### Data types
- [class VTRAWProcessingSession](./vtrawprocessingsession.md)
  An object that processes frames in camera native formats such as RAW or Bayer.
- [VTRAWProcessingParameterChangeHandler](./vtrawprocessingparameterchangehandler.md)
  A function the system calls when processing parameters change.
- [VTRAWProcessingOutputHandler](./vtrawprocessingoutputhandler.md)
  A block the system calls when frame processing is complete.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtrawprocessingsessionsetparameterchangedhander)*