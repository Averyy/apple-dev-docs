# kVTCompressionPropertyKey_ExpectedDuration

**Framework**: Video Toolbox  
**Kind**: var

The expected total duration of the compression session, if known.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
let kVTCompressionPropertyKey_ExpectedDuration: CFString
```

#### Discussion

By default, this value is `0`, indicating the duration is unknown.

## See Also

- [let kVTCompressionPropertyKey_BaseLayerBitRateFraction: CFString](kvtcompressionpropertykey_baselayerbitratefraction.md)
- [let kVTCompressionPropertyKey_BaseLayerFrameRate: CFString](kvtcompressionpropertykey_baselayerframerate.md)
- [let kVTCompressionPropertyKey_BaseLayerFrameRateFraction: CFString](kvtcompressionpropertykey_baselayerframeratefraction.md)
- [let kVTCompressionPropertyKey_ExpectedFrameRate: CFString](kvtcompressionpropertykey_expectedframerate.md)
  The expected frame rate, if known.
- [let kVTCompressionPropertyKey_MaximumRealTimeFrameRate: CFString](kvtcompressionpropertykey_maximumrealtimeframerate.md)
  A value that specifies the maximum real time rate at which frames can be submitted to a compression session.
- [let kVTCompressionPropertyKey_PrioritizeEncodingSpeedOverQuality: CFString](kvtcompressionpropertykey_prioritizeencodingspeedoverquality.md)
  A hint for the video encoder to maximize its speed during encoding, sacrificing quality if needed.
- [let kVTCompressionPropertyKey_ReferenceBufferCount: CFString](kvtcompressionpropertykey_referencebuffercount.md)
- [let kVTCompressionPropertyKey_SourceFrameCount: CFString](kvtcompressionpropertykey_sourceframecount.md)
  The number of source frames, if known.
- [let kVTCompressionPropertyKey_CalculateMeanSquaredError: CFString](kvtcompressionpropertykey_calculatemeansquarederror.md)
- [let kVTCompressionPropertyKey_HasLeftStereoEyeView: CFString](kvtcompressionpropertykey_hasleftstereoeyeview.md)
- [let kVTCompressionPropertyKey_HasRightStereoEyeView: CFString](kvtcompressionpropertykey_hasrightstereoeyeview.md)
- [let kVTCompressionPropertyKey_HorizontalFieldOfView: CFString](kvtcompressionpropertykey_horizontalfieldofview.md)
- [let kVTSampleAttachmentKey_QualityMetrics: CFString](kvtsampleattachmentkey_qualitymetrics.md)
- [let kVTSampleAttachmentQualityMetricsKey_ChromaBlueMeanSquaredError: CFString](kvtsampleattachmentqualitymetricskey_chromabluemeansquarederror.md)
- [let kVTSampleAttachmentQualityMetricsKey_ChromaRedMeanSquaredError: CFString](kvtsampleattachmentqualitymetricskey_chromaredmeansquarederror.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/kvtcompressionpropertykey_expectedduration)*