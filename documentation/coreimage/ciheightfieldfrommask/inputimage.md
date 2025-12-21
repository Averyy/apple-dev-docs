# inputImage

**Framework**: Core Image  
**Kind**: property  
**Required**: Yes

The image to use as an input image.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
var inputImage: CIImage? { get set }
```

#### Discussion

The white values of the input image define those pixels that are inside the height field while the black values define those pixels that are outside. The field varies smoothly and continuously inside the mask, reaching the value 0 at the edge of the mask.

## See Also

- [var radius: Float](ciheightfieldfrommask/radius.md)
  The length of the height-field transition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciheightfieldfrommask/inputimage)*