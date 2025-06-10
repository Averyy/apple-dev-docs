# Decompression Properties

**Framework**: Video Toolbox

Properties used to configure a VideoToolbox decompression session.

## Topics

### Pixel Buffer Pools
- [let kVTDecompressionPropertyKey_PixelBufferPool: CFString](kvtdecompressionpropertykey_pixelbufferpool.md)
  A pixel buffer pool for pixel buffers being output by the decompression session.
- [let kVTDecompressionPropertyKey_PixelBufferPoolIsShared: CFString](kvtdecompressionpropertykey_pixelbufferpoolisshared.md)
  A Boolean value indicating whether a common pixel buffer pool is shared between the video decoder and the session client.
- [let kVTDecompressionPropertyKey_OutputPoolRequestedMinimumBufferCount: CFString](kvtdecompressionpropertykey_outputpoolrequestedminimumbuffercount.md)
  The requested minimum buffer count that a decompression session should use for its output pixel buffer pool, without releasing buffers while the number in use is below this level.
### Asynchronous State
- [let kVTDecompressionPropertyKey_NumberOfFramesBeingDecoded: CFString](kvtdecompressionpropertykey_numberofframesbeingdecoded.md)
  Returns the number of frames currently being decoded.
- [let kVTDecompressionPropertyKey_MinOutputPresentationTimeStampOfFramesBeingDecoded: CFString](kvtdecompressionpropertykey_minoutputpresentationtimestampofframesbeingdecoded.md)
  The minimum output presentation timestamp of the frames currently being decoded.
- [let kVTDecompressionPropertyKey_MaxOutputPresentationTimeStampOfFramesBeingDecoded: CFString](kvtdecompressionpropertykey_maxoutputpresentationtimestampofframesbeingdecoded.md)
  The maximum output presentation timestamp of the frames currently being decoded.
### Content
- [let kVTDecompressionPropertyKey_ContentHasInterframeDependencies: CFString](kvtdecompressionpropertykey_contenthasinterframedependencies.md)
  An optional Boolean property indicating if the content being decoded has interframe dependencies, if the decoder knows.
### Hardware Acceleration
- [let kVTVideoDecoderSpecification_EnableHardwareAcceleratedVideoDecoder: CFString](kvtvideodecoderspecification_enablehardwareacceleratedvideodecoder.md)
  A Boolean value indicating whether VideoToolbox uses a hardware-accelerated video decoder, if available.
- [let kVTVideoDecoderSpecification_RequireHardwareAcceleratedVideoDecoder: CFString](kvtvideodecoderspecification_requirehardwareacceleratedvideodecoder.md)
  A Boolean value indicating whether to require hardware-accelerated decoding.
- [let kVTDecompressionPropertyKey_UsingHardwareAcceleratedVideoDecoder: CFString](kvtdecompressionpropertykey_usinghardwareacceleratedvideodecoder.md)
  Indicates if a hardware-accelerated video decoder is being used.
### Decoder Behavior
- [let kVTDecompressionPropertyKey_RealTime: CFString](kvtdecompressionpropertykey_realtime.md)
  A Boolean value indicating whether it’s recommended that the video decoder perform decompression in real time.
- [let kVTDecompressionPropertyKey_MaximizePowerEfficiency: CFString](kvtdecompressionpropertykey_maximizepowerefficiency.md)
- [let kVTDecompressionPropertyKey_ThreadCount: CFString](kvtdecompressionpropertykey_threadcount.md)
  The number of threads used by a codec or the suggested number of threads to use (optional).
- [let kVTDecompressionPropertyKey_FieldMode: CFString](kvtdecompressionpropertykey_fieldmode.md)
  Modes for special handling of interlaced content (optional).
- [let kVTDecompressionPropertyKey_DeinterlaceMode: CFString](kvtdecompressionpropertykey_deinterlacemode.md)
  Modes for requesting a specific deinterlacing technique.
- [let kVTDecompressionPropertyKey_ReducedResolutionDecode: CFString](kvtdecompressionpropertykey_reducedresolutiondecode.md)
  Request decoding at smaller resolutions than full-size (optional).
- [let kVTDecompressionPropertyKey_ReducedCoefficientDecode: CFString](kvtdecompressionpropertykey_reducedcoefficientdecode.md)
  Requests approximation during decoding.
- [let kVTDecompressionPropertyKey_ReducedFrameDelivery: CFString](kvtdecompressionpropertykey_reducedframedelivery.md)
  The proportion of frames that should be delivered, indicating that the rest may be dropped.
- [let kVTDecompressionPropertyKey_OnlyTheseFrames: CFString](kvtdecompressionpropertykey_onlytheseframes.md)
  Requests that frames be filtered by type.
- [let kVTDecompressionProperty_TemporalLevelLimit: CFString](kvtdecompressionproperty_temporallevellimit.md)
- [let kVTDecompressionPropertyKey_SuggestedQualityOfServiceTiers: CFString](kvtdecompressionpropertykey_suggestedqualityofservicetiers.md)
  An array of dictionaries that describe decreasing quality-of-service levels that clients can use to maintain realtime playback (optional).
- [let kVTDecompressionPropertyKey_SupportedPixelFormatsOrderedByQuality: CFString](kvtdecompressionpropertykey_supportedpixelformatsorderedbyquality.md)
  An array indicating quality levels among pixel formats.
- [let kVTDecompressionPropertyKey_SupportedPixelFormatsOrderedByPerformance: CFString](kvtdecompressionpropertykey_supportedpixelformatsorderedbyperformance.md)
  An array indicating speed tradeoffs between pixel formats (optional).
- [let kVTDecompressionPropertyKey_PixelFormatsWithReducedResolutionSupport: CFString](kvtdecompressionpropertykey_pixelformatswithreducedresolutionsupport.md)
  Pixel formats that support reduced-resolution decoding (optional).
- [let kVTDecompressionPropertyKey_AllowBitstreamToChangeFrameDimensions: CFString](kvtdecompressionpropertykey_allowbitstreamtochangeframedimensions.md)
### Post-Decompression Processing
- [let kVTDecompressionPropertyKey_PixelTransferProperties: CFString](kvtdecompressionpropertykey_pixeltransferproperties.md)
  Specific pixel transfer features to be used during decompression.
- [let kVTVideoDecoderSpecification_RequiredDecoderGPURegistryID: CFString](kvtvideodecoderspecification_requireddecodergpuregistryid.md)
- [let kVTVideoDecoderSpecification_PreferredDecoderGPURegistryID: CFString](kvtvideodecoderspecification_preferreddecodergpuregistryid.md)
- [let kVTDecompressionPropertyKey_UsingGPURegistryID: CFString](kvtdecompressionpropertykey_usinggpuregistryid.md)
- [let kVTDecompressionPropertyKey_PropagatePerFrameHDRDisplayMetadata: CFString](kvtdecompressionpropertykey_propagateperframehdrdisplaymetadata.md)
- [let kVTDecompressionPropertyKey_GeneratePerFrameHDRDisplayMetadata: CFString](kvtdecompressionpropertykey_generateperframehdrdisplaymetadata.md)
  A key that indicates to generate per frame HDR Metadata and attach it to the resulting decoded pixel buffers.
- [let kVTDecompressionPropertyKey_DecoderProducesRAWOutput: CFString](kvtdecompressionpropertykey_decoderproducesrawoutput.md)
- [let kVTDecompressionPropertyKey_RequestRAWOutput: CFString](kvtdecompressionpropertykey_requestrawoutput.md)
### Multiview Decompression
- [let kVTDecompressionPropertyKey_RequestedMVHEVCVideoLayerIDs: CFString](kvtdecompressionpropertykey_requestedmvhevcvideolayerids.md)
  Requests multi-image decoding of specific MV-HEVC video layers.

## See Also

- [func VTVideoDecoderExtensionProperties(CMFormatDescription) throws -> [VTExtensionPropertiesKey : Any]](vtvideodecoderextensionproperties(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/decompression-properties)*