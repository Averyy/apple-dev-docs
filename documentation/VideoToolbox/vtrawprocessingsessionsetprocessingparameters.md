# VTRAWProcessingSessionSetProcessingParameters

**Framework**: Video Toolbox  
**Kind**: func  
**Role**: Function

Sets a collection of RAW Processing parameters.

**Availability**:
- macOS 15.0+

## Declaration

```c
extern OSStatus VTRAWProcessingSessionSetProcessingParameters(VTRAWProcessingSessionRef session, CFDictionaryRef processingParameters);
```

#### Return Value

An error if any of the provided parameters are invalid, disabled, or outside of the declared valid range. None of the provided parameters will be set on the processor if an error is returned.

#### Discussion

This call sets a collection of RAW Processing parameters on the RAW Processor.  These are set as a dictionary where the keys match [`kVTRAWProcessingParameter_Key`](./kvtrawprocessingparameter_key.md) values that were returned in [`VTRAWProcessingSessionCopyProcessingParameters`](./vtrawprocessingsessioncopyprocessingparameters.md) and where values conform to the type and range defined in the `kVTRAWProcessingParameter` dictionary for each parameter.

Not all parameters from the array need to be set at any given time.  Changing the parameters doesn’t change processing on frames already submitted for processing, it will only impact frames where [`VTRAWProcessingSessionProcessFrame`](./vtrawprocessingsessionprocessframe.md) is called after [`VTRAWProcessingSessionSetProcessingParameters`](./vtrawprocessingsessionsetprocessingparameters.md) returns.

If any parameters specified are not in the array reported by [`VTRAWProcessingSessionCopyProcessingParameters`](./vtrawprocessingsessioncopyprocessingparameters.md), or are the wrong type or out of range, [`kVTParameterErr`](./kvtparametererr.md) will be returned.  Valid key-value pairs in the dictionary will still be applied.

## Parameters

- `session`: The RAW processing session.
- `processingParameters`: A dictionary of keys and values setting parameters reported by [`VTRAWProcessingSessionCopyProcessingParameters`](./vtrawprocessingsessioncopyprocessingparameters.md).

## See Also

### Configuring a session
- [VTRAWProcessingSessionCopyProcessingParameters](./vtrawprocessingsessioncopyprocessingparameters.md)
  Copies an array of dictionaries describing the parameters provided by the RAW Processor for frame processing.
- [VTRAWProcessingSessionSetParameterChangedHandler](./vtrawprocessingsessionsetparameterchangedhandler.md)
- [RAW processing parameters](./raw-processing-parameters.md)
  Parameters to set on a RAW processing session.
- [VTCopyRAWProcessorExtensionProperties](./vtcopyrawprocessorextensionproperties.md)
  Returns information about the Media Extension RAW processor supporting the specified format.
- [RAW Processing Properties](./raw-processing-properties.md)
  Properties that you use to configure a RAW processing session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtrawprocessingsessionsetprocessingparameters)*