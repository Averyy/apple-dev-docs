# bounds

**Framework**: Core Image  
**Kind**: property

A rectangle that indicates the position and extent of the text feature in image coordinates.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var bounds: CGRect { get }
```

#### Discussion

This property identifies the rectangular region of the image containing the detected text, not necessarily the shape of the text box. A detected feature is rectangular in space, but may appear as a four-sided polygon in the image. Use the properties listed in `CITextFeature` to find the corners of the rectangle as it appears in perspective.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/citextfeature/bounds)*