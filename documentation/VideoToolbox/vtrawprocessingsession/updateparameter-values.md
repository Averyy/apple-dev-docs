# updateParameter(values:)

**Framework**: Video Toolbox  
**Kind**: method

Sets the value for one or more of the processing parameters.

**Availability**:
- macOS 15.0+

## Declaration

```swift
func updateParameter(values: [String : Any]) throws
```

## Parameters

- `values`: A dictionary where keys correspond to Parameter.details.key for the parameters being set, and the value is appropriate to the Parameter type This call will throw an error if the RAW Processor extension process is unreachable or if the provided parameter values are invalid or out of range

## See Also

- [func parameters() -> any AsyncSequence<[VTRAWProcessingSession.Parameter], Never>](vtrawprocessingsession/parameters.md)
  Returns an asynchronous sequence that provides updates to the processing Parameter array if the processing extension makes changes to the set of Parameters.
- [var processingParameters: [VTRAWProcessingSession.Parameter]](vtrawprocessingsession/processingparameters.md)
  An array of processing parameters available for this RAW processing session.
- [VTRAWProcessingSession.Parameter](vtrawprocessingsession/parameter.md)
  A parameter expresses a control or a set of controls that influence frame processing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtrawprocessingsession/updateparameter(values:))*