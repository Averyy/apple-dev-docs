# kVTDecompressionPropertyKey_AllowBitstreamToChangeFrameDimensions

**Framework**: Videotoolbox  
**Kind**: var

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
let kVTDecompressionPropertyKey_AllowBitstreamToChangeFrameDimensions: CFString
```

#### Discussion

```not specified
@constant	kVTDecompressionPropertyKey_AllowBitstreamToChangeFrameDimensions
@abstract
	True if decoder is allowed to output buffers matching reduced frame dimensions in the bitstream rather than
	under-filling them.
@discussion
	This is an optional property only supported by video decoders for bitstream formats which have a provision
	for specifying output dimensions per-frame, such as AV1.

	If a decoder does not support this property or if the property value is set to `kCFBooleanFalse`, all decoded
	frames will have the same dimensions as specified in the format description. In this case, if the bitstream
	changes the frame dimensions, the output buffer will be padded to the dimensions specified in the format
	description.

	When this property is set to `kCFBooleanTrue`, the decoder will set the dimensions of each output buffer to
	match the dimensions specified in the bitstream for that frame.

	In all cases, output buffer dimensions will never exceed the dimensions specified in the format description.

	In apps linked to SDK versions before this property was added, the AV1 decoder will behave as if this property
	is set to `kCFBooleanFalse`. Otherwise, value of this property defaults to `kCFBooleanTrue` where supported.
```

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/kvtdecompressionpropertykey_allowbitstreamtochangeframedimensions)*