# VTCopyVideoDecoderExtensionProperties

**Framework**: Video Toolbox  
**Kind**: func  
**Role**: Function

Returns information about the Media Extension video decoder required to decode the specified format.

**Availability**:
- macOS 15.0+

## Declaration

```c
extern OSStatus VTCopyVideoDecoderExtensionProperties(CMFormatDescriptionRef formatDesc, CFDictionaryRef*mediaExtensionPropertiesOut);
```

## Return Value

If the function succeeds and a [MediaExtension](../MediaExtension/MediaExtension.md) video decoder will be used to decode this format, the return value will be `noErr`. If the function succeeds but a Media Extension video decoder will not be used to decode this format, the return value will be [`kVTCouldNotFindExtensionErr`](./kvtcouldnotfindextensionerr.md). Otherwise, the return value will be an error code describing the failure.

## Discussion

If a Media Extension video decoder will be used to decode the specified format, this function will return information about the Media Extension that will be used.

## Parameters

- `formatDesc`: The format description for the video format for which information is being requested.
- `mediaExtensionPropertiesOut`: If a [MediaExtension](../MediaExtension/MediaExtension.md) video decoder will be used to decode the specified format, this pointer will return a dictionary with a set of properties describing the extension video decoder. The dictionary keys are VTExtensionPropertiesKey values.

## See Also

### Media Extension
- [struct VTExtensionPropertiesKey](./vtextensionpropertieskey.md)
  A key in a Media Extension extension properties dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtcopyvideodecoderextensionproperties)*