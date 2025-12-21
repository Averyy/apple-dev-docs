# kVTDecompressionPropertyKey_ReducedFrameDelivery

**Framework**: Video Toolbox  
**Kind**: var

The proportion of frames that should be delivered, indicating that the rest may be dropped.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
let kVTDecompressionPropertyKey_ReducedFrameDelivery: CFString
```

#### Discussion

This is an optional property for video decoders to implement. If supported, it requests that frame delivery be reduced by the specified amount.

This number is a fraction between 0.0 and 1.0 that indicates what proportion of frames should be delivered–others may be dropped. For example, `0.25` would indicate that only one frame in every four should be delivered. This is a guideline;  the actual selection of frames is up to the decoder, which knows which frames can be skipped without harm.

You can use this key on its own, or in the dictionaries returned in the array obtained from [`kVTDecompressionPropertyKey_SuggestedQualityOfServiceTiers`](kvtdecompressionpropertykey_suggestedqualityofservicetiers.md). This key may also be used in conjunction with [`kVTDecompressionPropertyKey_OnlyTheseFrames`](kvtdecompressionpropertykey_onlytheseframes.md).  For example, the dictionary containing `[{kVTDecompressionPropertyKey_OnlyTheseFrames, kVTDecompressionProperty_OnlyTheseFrames_KeyFrames}, {kVTDecompressionPropertyKey_ReducedFrameDelivery, 0.25}]` requests that the decoder only deliver a quarter of keyframes.

If the decoder does not support this property directly, but reports that the content has no interframe dependencies, VideoToolbox may step in and perform simple frame dropping.

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

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/kvtdecompressionpropertykey_reducedframedelivery)*