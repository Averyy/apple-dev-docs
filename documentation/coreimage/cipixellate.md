# CIPixellate

**Framework**: Core Image  
**Kind**: intf

The properties you use to configure a pixellate filter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol CIPixellate
```

## Topics

### Instance Properties
- [var center: CGPoint](cipixellate/3228674-center.md)
  The x and y position to use as the center of the effect.
- [var inputImage: CIImage?](cipixellate/3228675-inputimage.md)
  The image to use as an input image.
- [var scale: Float](cipixellate/3228676-scale.md)
  A value that determines the size of the squares.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func pixellate() -> any CIFilter & CIPixellate](cifilter/3228393-pixellate.md)
  Enlarges the colors of the pixels to create a blurred effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cipixellate)*