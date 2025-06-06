# inputImage

**Framework**: Core Image  
**Kind**: intfp  
**Required**: Yes

The image to use as an input image.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var inputImage: CIImage? { get set }
```

#### Discussion

The white values of the input image define those pixels that are inside the height field while the black values define those pixels that are outside. The field varies smoothly and continuously inside the mask, reaching the value 0 at the edge of the mask.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciheightfieldfrommask/3228487-inputimage)*