# RAW Processing Properties

**Framework**: Video Toolbox  
**Role**: API Collection

Properties that you use to configure a RAW processing session.

## Topics

### Properties
- [let kVTRAWProcessingPropertyKey_OutputColorAttachments: CFString!](./kvtrawprocessingpropertykey_outputcolorattachments.md)
  The color-related image buffer keys and values that will be attachments to the returned pixel buffers.
- [let kVTRAWProcessingPropertyKey_MetadataForSidecarFile: CFString!](./kvtrawprocessingpropertykey_metadataforsidecarfile.md)
- [kVTRAWProcessingPropertyKey_MetalDeviceRegistryID](./kvtrawprocessingpropertykey_metaldeviceregistryid.md)
  This property requests that the Metal device corresponding to the specified registryID be used for any Metal related processing.
### Functions
- [func VTRAWProcessorExtensionProperties(CMFormatDescription) throws -> [VTExtensionPropertiesKey : Any]](./vtrawprocessorextensionproperties%28_%29.md)

## See Also

### Configuring a session
- [RAW processing parameters](./raw-processing-parameters.md)
  Parameters to set on a RAW processing session.
- [VTRAWProcessingSessionCopyProcessingParameters](./vtrawprocessingsessioncopyprocessingparameters.md)
  Copies an array of dictionaries describing the parameters provided by the RAW Processor for frame processing.
- [VTRAWProcessingSessionSetProcessingParameters](./vtrawprocessingsessionsetprocessingparameters.md)
  Sets a collection of RAW Processing parameters.
- [VTRAWProcessingSessionSetParameterChangedHandler](./vtrawprocessingsessionsetparameterchangedhandler.md)
- [VTCopyRAWProcessorExtensionProperties](./vtcopyrawprocessorextensionproperties.md)
  Returns information about the Media Extension RAW processor supporting the specified format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/raw-processing-properties)*