# VTRAWProcessingSessionCompleteFrames

**Framework**: Video Toolbox  
**Kind**: func  
**Role**: Function

Forces the RAW Processor to complete processing frames.

**Availability**:
- macOS 15.0+

## Declaration

```c
extern OSStatus VTRAWProcessingSessionCompleteFrames(VTRAWProcessingSessionRef session);
```

## Discussion

Call this after calling a set of [`VTRAWProcessingSessionProcessFrame`](./vtrawprocessingsessionprocessframe.md) calls to ensure that all frames have been processed. Before [`VTRAWProcessingSessionCompleteFrames`](./vtrawprocessingsessioncompleteframes.md) returns, the output handler will be invoked for all pending frames.

## Parameters

- `session`: The RAW processing session.

## See Also

### Processing frames
- [VTRAWProcessingSessionProcessFrame](./vtrawprocessingsessionprocessframe.md)
  Submits RAW frames for format-specific processing using sequence and frame level parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtrawprocessingsessioncompleteframes)*