# kVTCompressionPropertyKey_UsingHardwareAcceleratedVideoEncoder

**Framework**: Video Toolbox  
**Kind**: var

A Boolean value indicating whether a hardware-accelerated video encoder is used.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- macOS 10.9+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
let kVTCompressionPropertyKey_UsingHardwareAcceleratedVideoEncoder: CFString
```

#### Discussion

You can query this property using [`VTSessionCopyProperty(_:key:allocator:valueOut:)`](vtsessioncopyproperty(_:key:allocator:valueout:).md) after you have enabled hardware accelerated encode using [`kVTVideoEncoderSpecification_EnableHardwareAcceleratedVideoEncoder`](kvtvideoencoderspecification_enablehardwareacceleratedvideoencoder.md) to see if a hardware-accelerated encoder was selected ([`kCFBooleanTrue`](https://developer.apple.com/documentation/CoreFoundation/kCFBooleanTrue)).

## See Also

- [let kVTCompressionPropertyKey_UsingGPURegistryID: CFString](kvtcompressionpropertykey_usinggpuregistryid.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/kvtcompressionpropertykey_usinghardwareacceleratedvideoencoder)*