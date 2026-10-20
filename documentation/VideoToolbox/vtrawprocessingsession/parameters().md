# parameters()

**Framework**: Video Toolbox  
**Kind**: method  
**Role**: Instance Method

Returns an asynchronous sequence that provides updates to the processing Parameter array if the processing extension makes changes to the set of Parameters.

**Availability**:
- macOS 15.0+

## Declaration

```swift
func parameters() -> any AsyncSequence<[VTRAWProcessingSession.Parameter], Never>
```

#### Discussion

These changes could be: - adding or removing Parameters - enabling/disabling Parameters - changing default values for a Parameter

## See Also

### Configuring parameters
- [func updateParameter(values: [String : Any]) throws](./updateparameter%28values%29.md)
  Sets the value for one or more of the processing parameters.
- [var processingParameters: [VTRAWProcessingSession.Parameter]](./processingparameters.md)
  An array of processing parameters available for this RAW processing session.
- [VTRAWProcessingSession.Parameter](./parameter.md)
  A parameter expresses a control or a set of controls that influence frame processing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtrawprocessingsession/parameters())*