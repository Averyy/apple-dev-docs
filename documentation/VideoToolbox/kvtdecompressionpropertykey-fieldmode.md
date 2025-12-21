# kVTDecompressionPropertyKey_FieldMode

**Framework**: Video Toolbox  
**Kind**: var

Modes for special handling of interlaced content (optional).

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
let kVTDecompressionPropertyKey_FieldMode: CFString
```

#### Discussion

This is an optional property for video decoders to implement. Decoders should only accept the modes that they will implement.

## Topics

### Field Modes
- [let kVTDecompressionProperty_FieldMode_BothFields: CFString](kvtdecompressionproperty_fieldmode_bothfields.md)
- [let kVTDecompressionProperty_FieldMode_BottomFieldOnly: CFString](kvtdecompressionproperty_fieldmode_bottomfieldonly.md)
- [let kVTDecompressionProperty_FieldMode_DeinterlaceFields: CFString](kvtdecompressionproperty_fieldmode_deinterlacefields.md)
- [let kVTDecompressionProperty_FieldMode_SingleField: CFString](kvtdecompressionproperty_fieldmode_singlefield.md)
- [let kVTDecompressionProperty_FieldMode_TopFieldOnly: CFString](kvtdecompressionproperty_fieldmode_topfieldonly.md)

## See Also

- [let kVTDecompressionPropertyKey_RealTime: CFString](kvtdecompressionpropertykey_realtime.md)
  A Boolean value indicating whether it’s recommended that the video decoder perform decompression in real time.
- [let kVTDecompressionPropertyKey_MaximizePowerEfficiency: CFString](kvtdecompressionpropertykey_maximizepowerefficiency.md)
- [let kVTDecompressionPropertyKey_ThreadCount: CFString](kvtdecompressionpropertykey_threadcount.md)
  The number of threads used by a codec or the suggested number of threads to use (optional).
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
  A Boolean value that indicates whether a decoder is allowed to output buffers matching reduced frame dimensions in the bitstream rather than under-filling them.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/kvtdecompressionpropertykey_fieldmode)*