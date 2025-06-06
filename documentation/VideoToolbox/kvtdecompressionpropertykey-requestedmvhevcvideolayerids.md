# kVTDecompressionPropertyKey_RequestedMVHEVCVideoLayerIDs

**Framework**: Videotoolbox  
**Kind**: var

Requests multi-image decoding of specific MV-HEVC video layers.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
let kVTDecompressionPropertyKey_RequestedMVHEVCVideoLayerIDs: CFString
```

#### Discussion

This property is specific to MV-HEVC. The use of it requires you to use the [`VTDecompressionSessionSetMultiImageCallback`](vtdecompressionsessionsetmultiimagecallback.md) function to install a callback capable of receiving [`CMTaggedBufferGroupRef`](https://developer.apple.com/documentation/CoreMedia/CMTaggedBufferGroupRef) objects in response to multi-image frame decode requests.

MV-HEVC video layer IDs not in this list don’t need to be output, and the decoder may skip decoding them if not otherwise necessary.

The property is NULL by default. If this property is NULL, MV-HEVC ignores layers other than the base layer.

> **Note**:  In multiview decompression, a single video sample contains a single frame (with one PTS) that the system decodes to produce multiple images.

 In multiview decompression, a single video sample contains a single frame (with one PTS) that the system decodes to produce multiple images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/kvtdecompressionpropertykey_requestedmvhevcvideolayerids)*