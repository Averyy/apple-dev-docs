# kVTDecompressionPropertyKey_UsingHardwareAcceleratedVideoDecoder

**Framework**: Video Toolbox  
**Kind**: var

Indicates if a hardware-accelerated video decoder is being used.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 10.9+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
let kVTDecompressionPropertyKey_UsingHardwareAcceleratedVideoDecoder: CFString
```

#### Discussion

You can query this property using [`VTSessionCopyProperty(_:key:allocator:valueOut:)`](vtsessioncopyproperty(_:key:allocator:valueout:).md) after you have enabled hardware accelerated decode using [`kVTVideoDecoderSpecification_EnableHardwareAcceleratedVideoDecoder`](kvtvideodecoderspecification_enablehardwareacceleratedvideodecoder.md) to see if a hardware accelerated decoder was selected.

## See Also

- [let kVTVideoDecoderSpecification_EnableHardwareAcceleratedVideoDecoder: CFString](kvtvideodecoderspecification_enablehardwareacceleratedvideodecoder.md)
  A Boolean value indicating whether VideoToolbox uses a hardware-accelerated video decoder, if available.
- [let kVTVideoDecoderSpecification_RequireHardwareAcceleratedVideoDecoder: CFString](kvtvideodecoderspecification_requirehardwareacceleratedvideodecoder.md)
  A Boolean value indicating whether to require hardware-accelerated decoding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/kvtdecompressionpropertykey_usinghardwareacceleratedvideodecoder)*