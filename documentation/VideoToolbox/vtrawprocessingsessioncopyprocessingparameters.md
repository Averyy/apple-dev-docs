# VTRAWProcessingSessionCopyProcessingParameters

**Framework**: Video Toolbox  
**Kind**: func  
**Role**: Function

Copies an array of dictionaries describing the parameters provided by the RAW Processor for frame processing.

**Availability**:
- macOS 15.0+

## Declaration

```c
extern OSStatus VTRAWProcessingSessionCopyProcessingParameters(VTRAWProcessingSessionRef session, CFArrayRef*outParameterArray);
```

#### Discussion

This method returns an array of dictionaries - one for each parameter that can be controlled in the RAW processing operation.

The dictionary for each parameter will contain a set of keys whose values provide a name, value type, value range, and current value for each parameter. See [RAW processing parameters](./raw-processing-parameters.md) for more information.

The returned values can be used to construct dynamic UI presenting RAW Processing controls allowing the various knobs for this specific RAW Processor to be viewed and manipulated.

## Parameters

- `session`: The RAW processing session.
- `outParameterArray`: Pointer for receiving the RAW Processing parameter array.

## See Also

### Configuring a session
- [VTRAWProcessingSessionSetProcessingParameters](./vtrawprocessingsessionsetprocessingparameters.md)
  Sets a collection of RAW Processing parameters.
- [VTRAWProcessingSessionSetParameterChangedHandler](./vtrawprocessingsessionsetparameterchangedhandler.md)
- [RAW processing parameters](./raw-processing-parameters.md)
  Parameters to set on a RAW processing session.
- [VTCopyRAWProcessorExtensionProperties](./vtcopyrawprocessorextensionproperties.md)
  Returns information about the Media Extension RAW processor supporting the specified format.
- [RAW Processing Properties](./raw-processing-properties.md)
  Properties that you use to configure a RAW processing session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtrawprocessingsessioncopyprocessingparameters)*