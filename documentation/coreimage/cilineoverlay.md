# CILineOverlay

**Framework**: Core Image  
**Kind**: intf

The properties you use to configure a line overlay filter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol CILineOverlay
```

## Topics

### Instance Properties
- [var nrNoiseLevel: Float](cilineoverlay/3228529-nrnoiselevel.md)
  The noise level of the image, used with camera data, that's removed before tracing the edges of the image.
- [var nrSharpness: Float](cilineoverlay/3228530-nrsharpness.md)
  The amount of sharpening done when removing noise in the image before tracing the edges of the image.
- [var contrast: Float](cilineoverlay/3228531-contrast.md)
  The amount of antialiasing to use on the edges produced by this filter.
- [var edgeIntensity: Float](cilineoverlay/3228532-edgeintensity.md)
  The accentuation factor of the Sobel gradient information when tracing the edges of the image.
- [var inputImage: CIImage?](cilineoverlay/3228533-inputimage.md)
  The image to use as an input image.
- [var threshold: Float](cilineoverlay/3228534-threshold.md)
  A value that determines edge visibility.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func lineOverlay() -> any CIFilter & CILineOverlay](cifilter/3228347-lineoverlay.md)
  Creates an image that resembles a sketch of the outlines of objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cilineoverlay)*