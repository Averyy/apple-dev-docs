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

- [var aspectRatio: Float](cibicubicscaletransform/aspectratio.md)
  The additional horizontal scaling factor to use on the image.
- [var inputImage: CIImage?](cibicubicscaletransform/inputimage.md)
  The image to use as an input image.
- [var parameterB: Float](cibicubicscaletransform/parameterb.md)
  The value of B to use for the cubic resampling function.
- [var parameterC: Float](cibicubicscaletransform/parameterc.md)
  The value of C to use for the cubic resampling function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cibicubicscaletransform/scale)*