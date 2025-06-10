# applyCleanAperture

**Framework**: Core Image  
**Kind**: property

A Boolean value to control whether an image created with a CVPixelBuffer or an IOSurface should be cropped and offset according clean aperture attachments.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
static let applyCleanAperture: CIImageOption
```

#### Discussion

For a `CVPixelBuffer` this will use `kCVImageBufferPreferredCleanApertureKey` or `kCVImageBufferCleanApertureKey`.

If the value for this option is:

- True: then image will be cropped and offset to the clean aperture.
- False: then the full image is returned.
- [`CIVector`](civector.md) : then use it as a `CGRect` to crop and offset.
- Not specified : then it will behave as if False was specified.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimageoption/applycleanaperture)*