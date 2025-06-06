# CISpotColor

**Framework**: Core Image  
**Kind**: intf

The properties you use to configure a spot color filter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol CISpotColor
```

## Topics

### Instance Properties
- [var centerColor1: CIColor](cispotcolor/3228728-centercolor1.md)
  The center value of the first color range to replace.
- [var centerColor2: CIColor](cispotcolor/3228729-centercolor2.md)
  The center value of the second color range to replace.
- [var centerColor3: CIColor](cispotcolor/3228730-centercolor3.md)
  The center value of the third color range to replace.
- [var closeness1: Float](cispotcolor/3228731-closeness1.md)
  A value that indicates how closely the first color must match before it’s replaced.
- [var closeness2: Float](cispotcolor/3228732-closeness2.md)
  A value that indicates how closely the second color must match before it’s replaced.
- [var closeness3: Float](cispotcolor/3228733-closeness3.md)
  A value that indicates how closely the third color must match before it’s replaced.
- [var contrast1: Float](cispotcolor/3228734-contrast1.md)
  The contrast of the first replacement color.
- [var contrast2: Float](cispotcolor/3228735-contrast2.md)
  The contrast of the second replacement color.
- [var contrast3: Float](cispotcolor/3228736-contrast3.md)
  The contrast of the third replacement color.
- [var inputImage: CIImage?](cispotcolor/3228737-inputimage.md)
  The image to use as an input image.
- [var replacementColor1: CIColor](cispotcolor/3228738-replacementcolor1.md)
  A replacement color for the first color range.
- [var replacementColor2: CIColor](cispotcolor/3228739-replacementcolor2.md)
  A replacement color for the second color range.
- [var replacementColor3: CIColor](cispotcolor/3228740-replacementcolor3.md)
  A replacement color for the third color range.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func spotColor() -> any CIFilter & CISpotColor](cifilter/3228413-spotcolor.md)
  Replaces colors of an image with specifed colors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cispotcolor)*