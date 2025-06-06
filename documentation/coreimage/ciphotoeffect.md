# CIPhotoEffect

**Framework**: Core Image  
**Kind**: intf

The properties you use to configure a photo-effect filter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol CIPhotoEffect
```

## Topics

### Instance Properties
- [var inputImage: CIImage?](ciphotoeffect/3228672-inputimage.md)
  The image to use as an input image.
- [var extrapolate: Bool](ciphotoeffect/4401951-extrapolate.md)

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func photoEffectChrome() -> any CIFilter & CIPhotoEffect](cifilter/3228384-photoeffectchrome.md)
  Exaggerates an image’s colors.
- [class func photoEffectFade() -> any CIFilter & CIPhotoEffect](cifilter/3228385-photoeffectfade.md)
  Diminishes an image’s colors.
- [class func photoEffectInstant() -> any CIFilter & CIPhotoEffect](cifilter/3228386-photoeffectinstant.md)
  Desaturates an image’s colors.
- [class func photoEffectMono() -> any CIFilter & CIPhotoEffect](cifilter/3228387-photoeffectmono.md)
  Adjust an image’s colors to black and white.
- [class func photoEffectNoir() -> any CIFilter & CIPhotoEffect](cifilter/3228388-photoeffectnoir.md)
  Adjusts an image’s colors to black and white and intensifies the contrast.
- [class func photoEffectProcess() -> any CIFilter & CIPhotoEffect](cifilter/3228389-photoeffectprocess.md)
  Lowers the contrast of the input image.
- [class func photoEffectTonal() -> any CIFilter & CIPhotoEffect](cifilter/3228390-photoeffecttonal.md)
  Adjusts an image’s colors to black and white.
- [class func photoEffectTransfer() -> any CIFilter & CIPhotoEffect](cifilter/3228391-photoeffecttransfer.md)
  Brightens an image’s colors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciphotoeffect)*