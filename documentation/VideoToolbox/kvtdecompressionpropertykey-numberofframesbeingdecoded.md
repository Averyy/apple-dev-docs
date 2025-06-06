# kVTDecompressionPropertyKey_NumberOfFramesBeingDecoded

**Framework**: Videotoolbox  
**Kind**: var

Returns the number of frames currently being decoded.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
let kVTDecompressionPropertyKey_NumberOfFramesBeingDecoded: CFString
```

#### Discussion

This number may decrease asynchronously as frames are output.

## See Also

- [let kVTDecompressionPropertyKey_MinOutputPresentationTimeStampOfFramesBeingDecoded: CFString](kvtdecompressionpropertykey_minoutputpresentationtimestampofframesbeingdecoded.md)
  The minimum output presentation timestamp of the frames currently being decoded.
- [let kVTDecompressionPropertyKey_MaxOutputPresentationTimeStampOfFramesBeingDecoded: CFString](kvtdecompressionpropertykey_maxoutputpresentationtimestampofframesbeingdecoded.md)
  The maximum output presentation timestamp of the frames currently being decoded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/kvtdecompressionpropertykey_numberofframesbeingdecoded)*