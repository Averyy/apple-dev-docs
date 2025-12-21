# maskImage

**Framework**: Core Image  
**Kind**: property  
**Required**: Yes

A grayscale mask that defines the blend.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
var maskImage: CIImage? { get set }
```

#### Discussion

When a mask value is 0.0, the result is the background. When the mask value is 1.0, the result is the image.

## See Also

- [var backgroundImage: CIImage?](ciblendwithmask/backgroundimage.md)
  The image to use as a background image.
- [var inputImage: CIImage?](ciblendwithmask/inputimage.md)
  The image to use as a foreground image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciblendwithmask/maskimage)*