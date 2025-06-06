# VTRAWProcessingSession.Parameter

**Framework**: Videotoolbox  
**Kind**: enum

A parameter expresses a control or a set of controls that influence frame processing.

**Availability**:
- macOS 15.0+

## Declaration

```swift
enum Parameter
```

#### Overview

Parameters can represent Boolean options, integer or floating-point ranges, lists, or subgroups. All parameters have a collection of [`VTRAWProcessingSession.Parameter.Details`](vtrawprocessingsession/parameter/details.md) containing a localized name suitable for display in UI, a longer localized description string, and a Boolean that indicates whether it’s enabled. All details, except for subgroups, must have a “key” string used to uniquely identify that parameter. All parameters other than subgroups have a collection of [`VTRAWProcessingSession.Parameter.Values`](vtrawprocessingsession/parameter/values.md) containing a mandatory “initial” value, and optional “neutral” and “camera” values. [`VTRAWProcessingSession.Parameter.IntegerParameter`](vtrawprocessingsession/parameter/integerparameter.md) and [`VTRAWProcessingSession.Parameter.FloatParameter`](vtrawprocessingsession/parameter/floatparameter.md) are required to have “minimum” and “maximum” values in their Values

Parameter arrays are created and returned by the VideoToolbox framework.

## Topics

### Parameters
- [VTRAWProcessingSession.Parameter.BooleanParameter](vtrawprocessingsession/parameter/booleanparameter.md)
- [VTRAWProcessingSession.Parameter.Details](vtrawprocessingsession/parameter/details.md)
- [VTRAWProcessingSession.Parameter.FloatParameter](vtrawprocessingsession/parameter/floatparameter.md)
- [VTRAWProcessingSession.Parameter.IntegerParameter](vtrawprocessingsession/parameter/integerparameter.md)
- [VTRAWProcessingSession.Parameter.ListParameter](vtrawprocessingsession/parameter/listparameter.md)
- [VTRAWProcessingSession.Parameter.Values](vtrawprocessingsession/parameter/values.md)
### Enumeration Cases
- [case bool(VTRAWProcessingSession.Parameter.BooleanParameter)](vtrawprocessingsession/parameter/bool(_:).md)
- [case float(VTRAWProcessingSession.Parameter.FloatParameter)](vtrawprocessingsession/parameter/float(_:).md)
- [case int(VTRAWProcessingSession.Parameter.IntegerParameter)](vtrawprocessingsession/parameter/int(_:).md)
- [case list(VTRAWProcessingSession.Parameter.ListParameter)](vtrawprocessingsession/parameter/list(_:).md)
- [case subgroup(details: VTRAWProcessingSession.Parameter.Details, elements: [VTRAWProcessingSession.Parameter])](vtrawprocessingsession/parameter/subgroup(details:elements:).md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func parameters() -> any AsyncSequence<[VTRAWProcessingSession.Parameter], Never>](vtrawprocessingsession/parameters.md)
  Returns an asynchronous sequence that provides updates to the processing Parameter array if the processing extension makes changes to the set of Parameters.
- [func updateParameter(values: [String : Any]) throws](vtrawprocessingsession/updateparameter(values:).md)
  Sets the value for one or more of the processing parameters.
- [var processingParameters: [VTRAWProcessingSession.Parameter]](vtrawprocessingsession/processingparameters.md)
  An array of processing parameters available for this RAW processing session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtrawprocessingsession/parameter)*