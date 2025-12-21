# edgeIntensity

**Framework**: Core Image  
**Kind**: property  
**Required**: Yes

The accentuation factor of the Sobel gradient information when tracing the edges of the image.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
var edgeIntensity: Float { get set }
```

#### Discussion

Higher values find more edges, although typically, you’d use a low value (such as 1.0).

## See Also

- [var nrNoiseLevel: Float](cilineoverlay/nrnoiselevel.md)
  The noise level of the image, used with camera data, that’s removed before tracing the edges of the image.
- [var nrSharpness: Float](cilineoverlay/nrsharpness.md)
  The amount of sharpening done when removing noise in the image before tracing the edges of the image.
- [var contrast: Float](cilineoverlay/contrast.md)
  The amount of antialiasing to use on the edges produced by this filter.
- [var inputImage: CIImage?](cilineoverlay/inputimage.md)
  The image to use as an input image.
- [var threshold: Float](cilineoverlay/threshold.md)
  A value that determines edge visibility.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cilineoverlay/edgeintensity)*