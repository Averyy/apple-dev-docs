# VTRAWProcessingSession.Parameter

**Framework**: Video Toolbox  
**Kind**: enum  
**Role**: Enumeration

A parameter expresses a control or a set of controls that influence frame processing.

**Availability**:
- macOS 15.0+

## Declaration

```swift
enum Parameter
```

#### Overview

Parameters can represent Boolean options, integer or floating-point ranges, lists, or subgroups. All parameters have a collection of [`VTRAWProcessingSession.Parameter.Details`](./parameter/details.md) containing a localized name suitable for display in UI, a longer localized description string, and a Boolean that indicates whether it’s enabled. All details, except for subgroups, must have a “key” string used to uniquely identify that parameter. All parameters other than subgroups have a collection of [`VTRAWProcessingSession.Parameter.Values`](./parameter/values.md) containing a mandatory “initial” value, and optional “neutral” and “camera” values. [`VTRAWProcessingSession.Parameter.IntegerParameter`](./parameter/integerparameter.md) and [`VTRAWProcessingSession.Parameter.FloatParameter`](./parameter/floatparameter.md) are required to have “minimum” and “maximum” values in their Values

Parameter arrays are created and returned by the VideoToolbox framework.

## Topics

### Parameters
- [VTRAWProcessingSession.Parameter.BooleanParameter](./parameter/booleanparameter.md)
- [VTRAWProcessingSession.Parameter.Details](./parameter/details.md)
- [VTRAWProcessingSession.Parameter.FloatParameter](./parameter/floatparameter.md)
- [VTRAWProcessingSession.Parameter.IntegerParameter](./parameter/integerparameter.md)
- [VTRAWProcessingSession.Parameter.ListParameter](./parameter/listparameter.md)
- [VTRAWProcessingSession.Parameter.Values](./parameter/values.md)
### Enumeration Cases
- [case bool(VTRAWProcessingSession.Parameter.BooleanParameter)](./parameter/bool%28_%29.md)
- [case float(VTRAWProcessingSession.Parameter.FloatParameter)](./parameter/float%28_%29.md)
- [case int(VTRAWProcessingSession.Parameter.IntegerParameter)](./parameter/int%28_%29.md)
- [case list(VTRAWProcessingSession.Parameter.ListParameter)](./parameter/list%28_%29.md)
- [case subgroup(details: VTRAWProcessingSession.Parameter.Details, elements: [VTRAWProcessingSession.Parameter])](./parameter/subgroup%28details,elements%29.md)

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Configuring parameters
- [func parameters() -> any AsyncSequence<[VTRAWProcessingSession.Parameter], Never>](./parameters%28%29.md)
  Returns an asynchronous sequence that provides updates to the processing Parameter array if the processing extension makes changes to the set of Parameters.
- [func updateParameter(values: [String : Any]) throws](./updateparameter%28values%29.md)
  Sets the value for one or more of the processing parameters.
- [var processingParameters: [VTRAWProcessingSession.Parameter]](./processingparameters.md)
  An array of processing parameters available for this RAW processing session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtrawprocessingsession/parameter)*