# settingContentHeadroom(_:)

**Framework**: Core Image  
**Kind**: method

Create an image by changing the receiver’s contentHeadroom property.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func settingContentHeadroom(_ headroom: Float) -> CIImage
```

#### Return Value

 An autoreleased [`CIImage`](ciimage.md).

#### Discussion

Changing this value will alter the behavior of the `CIToneMapHeadroom` and `CISystemToneMap` filters.

- If the value is set to 0.0 then the returned image’s headroom is unknown.
- If the value is set to 1.0 then the returned image is SDR.
- If the value is set to greater 1.0 then the returned image is HDR.
- Otherwise the returned image’s headroom is unknown.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimage/settingcontentheadroom(_:))*