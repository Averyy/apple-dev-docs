# kVTDecompressionPropertyKey_EnableStrictBitstreamValidation

**Framework**: Video Toolbox  
**Kind**: var  
**Role**: Global Variable

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- macOS 27.3+ (Beta)
- tvOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
let kVTDecompressionPropertyKey_EnableStrictBitstreamValidation: CFString
```

```c
extern CFStringRef const kVTDecompressionPropertyKey_EnableStrictBitstreamValidation;
```

## Discussion

This property requests that the decoder enable stricter bitstream validation.

Setting this property to kCFBooleanTrue will request that the decoder enable additional strict bitstream conformance validation, returning an error when non-compliance is detected.  Enabling this property may cause some samples which previously played without visible issues to instead return an error on decode.

```
When an error is encountered, kVTVideoDecoderBadDataErr will be returned as the status
passed to the output callback or output handler.
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/kvtdecompressionpropertykey_enablestrictbitstreamvalidation)*