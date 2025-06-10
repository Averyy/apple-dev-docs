# processingParameters

**Framework**: Video Toolbox  
**Kind**: property

An array of processing parameters available for this RAW processing session.

**Availability**:
- macOS 15.0+

## Declaration

```swift
var processingParameters: [VTRAWProcessingSession.Parameter] { get throws }
```

#### Discussion

This call throws an error if the RAW Processor extension process is unreachable.

## See Also

- [func parameters() -> any AsyncSequence<[VTRAWProcessingSession.Parameter], Never>](vtrawprocessingsession/parameters.md)
  Returns an asynchronous sequence that provides updates to the processing Parameter array if the processing extension makes changes to the set of Parameters.
- [func updateParameter(values: [String : Any]) throws](vtrawprocessingsession/updateparameter(values:).md)
  Sets the value for one or more of the processing parameters.
- [VTRAWProcessingSession.Parameter](vtrawprocessingsession/parameter.md)
  A parameter expresses a control or a set of controls that influence frame processing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtrawprocessingsession/processingparameters)*