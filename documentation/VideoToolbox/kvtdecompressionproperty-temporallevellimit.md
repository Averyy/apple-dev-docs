# kVTDecompressionProperty_TemporalLevelLimit

**Framework**: Video Toolbox  
**Kind**: var

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.4+
- visionOS 1.0+

## Declaration

```swift
let kVTDecompressionProperty_TemporalLevelLimit: CFString
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
- [let kVTDecompressionPropertyKey_SuggestedQualityOfServiceTiers: CFString](kvtdecompressionpropertykey_suggestedqualityofservicetiers.md)
  An array of dictionaries that describe decreasing quality-of-service levels that clients can use to maintain realtime playback (optional).
- [let kVTDecompressionPropertyKey_SupportedPixelFormatsOrderedByQuality: CFString](kvtdecompressionpropertykey_supportedpixelformatsorderedbyquality.md)
  An array indicating quality levels among pixel formats.
- [let kVTDecompressionPropertyKey_SupportedPixelFormatsOrderedByPerformance: CFString](kvtdecompressionpropertykey_supportedpixelformatsorderedbyperformance.md)
  An array indicating speed tradeoffs between pixel formats (optional).
- [let kVTDecompressionPropertyKey_PixelFormatsWithReducedResolutionSupport: CFString](kvtdecompressionpropertykey_pixelformatswithreducedresolutionsupport.md)
  Pixel formats that support reduced-resolution decoding (optional).
- [let kVTDecompressionPropertyKey_AllowBitstreamToChangeFrameDimensions: CFString](kvtdecompressionpropertykey_allowbitstreamtochangeframedimensions.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/kvtdecompressionproperty_temporallevellimit)*