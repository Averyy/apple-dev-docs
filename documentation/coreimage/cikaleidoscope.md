# CIKaleidoscope

**Framework**: Core Image  
**Kind**: intf

The properties you use to configure a kaleidoscope filter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol CIKaleidoscope
```

## Topics

### Instance Properties
- [var angle: Float](cikaleidoscope/3228508-angle.md)
  The angle of the reflection.
- [var center: CGPoint](cikaleidoscope/3228509-center.md)
  The x and y position to use as the center of the effect.
- [var count: Int](cikaleidoscope/3228510-count.md)
  The number of reflections in the pattern.
- [var inputImage: CIImage?](cikaleidoscope/3228511-inputimage.md)
  The image to use as an input image.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func kaleidoscope() -> any CIFilter & CIKaleidoscope](cifilter/3228343-kaleidoscope.md)
  Creates a 12-way kaleidoscopic image from an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cikaleidoscope)*