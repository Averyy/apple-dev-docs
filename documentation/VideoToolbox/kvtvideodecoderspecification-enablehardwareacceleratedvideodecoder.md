# kVTVideoDecoderSpecification_EnableHardwareAcceleratedVideoDecoder

**Framework**: Video Toolbox  
**Kind**: var

A Boolean value indicating whether VideoToolbox uses a hardware-accelerated video decoder, if available.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 10.9+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
let kVTVideoDecoderSpecification_EnableHardwareAcceleratedVideoDecoder: CFString
```

#### Discussion

You set this key in the `decoderSpecification` passed in to [`VTDecompressionSessionCreate(allocator:formatDescription:decoderSpecification:imageBufferAttributes:outputCallback:decompressionSessionOut:)`](vtdecompressionsessioncreate(allocator:formatdescription:decoderspecification:imagebufferattributes:outputcallback:decompressionsessionout:).md).  Set it to [`kCFBooleanTrue`](https://developer.apple.com/documentation/CoreFoundation/kCFBooleanTrue) to allow hardware-accelerated decoding.  To specifically prevent hardware-accelerated decoding, set this property to [`kCFBooleanFalse`](https://developer.apple.com/documentation/CoreFoundation/kCFBooleanFalse). This property is useful for clients doing realtime decode operations because it allows VideoToolbox to choose the optimal decoding path.

## See Also

- [let kVTVideoDecoderSpecification_RequireHardwareAcceleratedVideoDecoder: CFString](kvtvideodecoderspecification_requirehardwareacceleratedvideodecoder.md)
  A Boolean value indicating whether to require hardware-accelerated decoding.
- [let kVTDecompressionPropertyKey_UsingHardwareAcceleratedVideoDecoder: CFString](kvtdecompressionpropertykey_usinghardwareacceleratedvideodecoder.md)
  Indicates if a hardware-accelerated video decoder is being used.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/kvtvideodecoderspecification_enablehardwareacceleratedvideodecoder)*