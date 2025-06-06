# CISpotLight

**Framework**: Core Image  
**Kind**: intf

The properties you use to configure a spotlight filter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol CISpotLight
```

## Topics

### Instance Properties
- [var brightness: Float](cispotlight/3228742-brightness.md)
  The brightness of the spotlight.
- [var color: CIColor](cispotlight/3228743-color.md)
  The color of the spotlight.
- [var concentration: Float](cispotlight/3228744-concentration.md)
  The size of the spotlight.
- [var inputImage: CIImage?](cispotlight/3228745-inputimage.md)
  The image to use as an input image.
- [var lightPointsAt: CIVector](cispotlight/3228746-lightpointsat.md)
  The x and y position that the spotlight points at.
- [var lightPosition: CIVector](cispotlight/3228747-lightposition.md)
  The x and y position of the spotlight.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func spotLight() -> any CIFilter & CISpotLight](cifilter/3228414-spotlight.md)
  Highlights a definined area of the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cispotlight)*