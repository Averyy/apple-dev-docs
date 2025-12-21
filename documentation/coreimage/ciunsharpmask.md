# CIUnsharpMask

**Framework**: Core Image  
**Kind**: protocol

The properties you use to configure an unsharp mask filter.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
protocol CIUnsharpMask : CIFilterProtocol
```

## Topics

### Instance Properties
- [var inputImage: CIImage?](ciunsharpmask/inputimage.md)
  The image to use as an input image.
- [var intensity: Float](ciunsharpmask/intensity.md)
  The intensity of the effect.
- [var radius: Float](ciunsharpmask/radius.md)
  The radius of the unsharp mask effect.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func unsharpMask() -> any CIFilter & CIUnsharpMask](cifilter-swift.class/unsharpmask.md)
  Increases an image’s contrast between two colors.
- [protocol CISharpenLuminance](cisharpenluminance.md)
  The properties you use to configure a sharpen luminance filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciunsharpmask)*