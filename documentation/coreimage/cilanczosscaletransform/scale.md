# scale

**Framework**: Core Image  
**Kind**: property  
**Required**: Yes

The scaling factor to use on the image.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
var scale: Float { get set }
```

#### Discussion

Values less than 1.0 scale down the images. Values greater than 1.0 scale up the image.

## See Also

- [var aspectRatio: Float](cilanczosscaletransform/aspectratio.md)
  The additional horizontal scaling factor to use on the image.
- [var inputImage: CIImage?](cilanczosscaletransform/inputimage.md)
  The image to use as an input image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cilanczosscaletransform/scale)*