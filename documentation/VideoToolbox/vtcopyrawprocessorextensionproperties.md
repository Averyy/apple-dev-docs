# VTCopyRAWProcessorExtensionProperties

**Framework**: Video Toolbox  
**Kind**: func  
**Role**: Function

Returns information about the Media Extension RAW processor supporting the specified format.

**Availability**:
- macOS 15.0+

## Declaration

```c
extern OSStatus VTCopyRAWProcessorExtensionProperties(CMFormatDescriptionRef formatDesc, CFDictionaryRef*mediaExtensionPropertiesOut);
```

#### Return Value

If the function succeeds and a Media Extension RAW processor will be used to process this format, the return value will be noErr. If the function succeeds but a Media Extension RAW processor will not be used to process this format, the return value will be [`kVTCouldNotFindExtensionErr`](./kvtcouldnotfindextensionerr.md). Otherwise, the return value will be an error code describing the failure.

#### Discussion

If a Media Extension RAW processor will be used to process the specified format, this function will return information about the Media Extension that will be used.

## Parameters

- `formatDesc`: The format description for the video format for which information is being requested.
- `mediaExtensionPropertiesOut`: If a Media Extension RAW processor  will be used to process the specified format, this pointer will return a dictionary with a set of properties describing the extension RAW processor. The dictionary keys [`VTExtensionPropertiesKey`](./vtextensionpropertieskey.md) values.

## See Also

### Configuring a session
- [VTRAWProcessingSessionCopyProcessingParameters](./vtrawprocessingsessioncopyprocessingparameters.md)
  Copies an array of dictionaries describing the parameters provided by the RAW Processor for frame processing.
- [VTRAWProcessingSessionSetProcessingParameters](./vtrawprocessingsessionsetprocessingparameters.md)
  Sets a collection of RAW Processing parameters.
- [VTRAWProcessingSessionSetParameterChangedHandler](./vtrawprocessingsessionsetparameterchangedhandler.md)
- [RAW processing parameters](./raw-processing-parameters.md)
  Parameters to set on a RAW processing session.
- [RAW Processing Properties](./raw-processing-properties.md)
  Properties that you use to configure a RAW processing session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtcopyrawprocessorextensionproperties)*