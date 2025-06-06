# maskImage

**Framework**: Core Image  
**Kind**: intfp  
**Required**: Yes

A grayscale mask that defines the blend.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var maskImage: CIImage? { get set }
```

#### Discussion

When a mask value is 0.0, the result is the background. When the mask value is 1.0, the result is the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciblendwithmask/3228082-maskimage)*