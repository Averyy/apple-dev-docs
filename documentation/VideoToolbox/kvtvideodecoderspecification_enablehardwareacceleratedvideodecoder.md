# kVTVideoDecoderSpecification_EnableHardwareAcceleratedVideoDecoder

**Framework**: Video Toolbox  
**Kind**: var  
**Role**: Global Variable

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

```c
extern CFStringRef const kVTVideoDecoderSpecification_EnableHardwareAcceleratedVideoDecoder;
```

## Discussion

You set this key in the `decoderSpecification` passed in to [`VTDecompressionSessionCreate(allocator:formatDescription:decoderSpecification:imageBufferAttributes:outputCallback:decompressionSessionOut:)`](./vtdecompressionsessioncreate%28allocator,formatdescription,decoderspecification,imagebufferattributes,outputcallback,decompressionsessionout%29.md).  Set it to [`kCFBooleanTrue`](../CoreFoundation/kcfbooleantrue.md) to allow hardware-accelerated decoding.  To specifically prevent hardware-accelerated decoding, set this property to [`kCFBooleanFalse`](../CoreFoundation/kcfbooleanfalse.md). This property is useful for clients doing realtime decode operations because it allows VideoToolbox to choose the optimal decoding path.

## See Also

### Hardware Acceleration
- [let kVTDecompressionPropertyKey_UsingHardwareAcceleratedVideoDecoder: CFString](./kvtdecompressionpropertykey_usinghardwareacceleratedvideodecoder.md)
  Indicates if a hardware-accelerated video decoder is being used.
- [let kVTVideoDecoderSpecification_RequireHardwareAcceleratedVideoDecoder: CFString](./kvtvideodecoderspecification_requirehardwareacceleratedvideodecoder.md)
  A Boolean value indicating whether to require hardware-accelerated decoding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/kvtvideodecoderspecification_enablehardwareacceleratedvideodecoder)*