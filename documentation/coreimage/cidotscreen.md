# CIDotScreen

**Framework**: Core Image  
**Kind**: intf

The properties you use to configure a dot screen filter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol CIDotScreen
```

## Topics

### Instance Properties
- [var angle: Float](cidotscreen/3228231-angle.md)
  The angle of the pattern.
- [var center: CGPoint](cidotscreen/3228232-center.md)
  The x and y position to use as the center of the dot screen pattern.
- [var inputImage: CIImage?](cidotscreen/3228233-inputimage.md)
  The image to use as an input image.
- [var sharpness: Float](cidotscreen/3228234-sharpness.md)
  The sharpness of the pattern.
- [var width: Float](cidotscreen/3228235-width.md)
  The distance between dots in the pattern.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func dotScreen() -> any CIFilter & CIDotScreen](cifilter/3228318-dotscreen.md)
  Creates a monochrome image with a series of dots to add detail.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cidotscreen)*