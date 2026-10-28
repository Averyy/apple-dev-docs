# VTRAWProcessingParameterChangeHandler

**Framework**: Video Toolbox  
**Kind**: typealias  
**Role**: Type Alias

A function the system calls when processing parameters change.

**Availability**:
- macOS 15.0+

## Declaration

```c
typedef void (^)(const struct __CFArray *) VTRAWProcessingParameterChangeHandler;
```

## Discussion

The system invokes this callback when available parameters or parameter values change without an explicit call to [`VTRAWProcessingSessionSetProcessingParameters`](./vtrawprocessingsessionsetprocessingparameters.md). This is intended to allow the client to update any UI driven by these parameters.

## Parameters

- `newParameters`: An array containing the new parameter details.  This follows the same form as the array returned from [`VTRAWProcessingSessionCopyProcessingParameters`](./vtrawprocessingsessioncopyprocessingparameters.md).

## See Also

### Data types
- [class VTRAWProcessingSession](./vtrawprocessingsession.md)
  An object that processes frames in camera native formats such as RAW or Bayer.
- [VTRAWProcessingSessionSetParameterChangedHander](./vtrawprocessingsessionsetparameterchangedhander.md)
  Provides a block which will be called when the session changes the set of processing parameters.
- [VTRAWProcessingOutputHandler](./vtrawprocessingoutputhandler.md)
  A block the system calls when frame processing is complete.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtrawprocessingparameterchangehandler)*