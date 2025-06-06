# bounds

**Framework**: Core Image  
**Kind**: instp

A rectangle indicating the position and extent of the feature in image coordinates.

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

This property identifies the rectangular region  containing the detected text region, not necessarily the shape of the region. A detected feature is rectangular in space, but may appear in perspective in the image. Use the properties listed in [`Identifying the Corners of a Detected Text Region`](citextfeature#1666221.md) to find the corners of the rectangle as it appears in perspective.

## See Also

- [Core Image Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/CoreImaging/ci_intro/ci_intro.html#//apple_ref/doc/uid/TP30001185)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/citextfeature/1437885-bounds)*