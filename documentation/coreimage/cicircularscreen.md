# CICircularScreen

**Framework**: Core Image  
**Kind**: intf

The properties you use to configure a circular screen filter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol CICircularScreen
```

## Topics

### Instance Properties
- [var center: CGPoint](cicircularscreen/3228111-center.md)
  The x and y position to use as the center of the circular screen pattern.
- [var inputImage: CIImage?](cicircularscreen/3228112-inputimage.md)
  The image to use as an input image.
- [var sharpness: Float](cicircularscreen/3228113-sharpness.md)
  The sharpness of the circles.
- [var width: Float](cicircularscreen/3228114-width.md)
  The distance between each circle in the pattern.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func circularScreen() -> any CIFilter & CICircularScreen](cifilter/3228280-circularscreen.md)
  Adds a circular overlay to an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicircularscreen)*