# searchLimitRadius

**Framework**: Metal Performance Shaders  
**Kind**: property

Limits the search in an image from a pixel to the closest nonzero pixel within a specified radius.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var searchLimitRadius: Float { get set }
```

#### Discussion

When the nonzero pixels in an input image are far apart, the search algorithm works harder to find the closest nonzero pixel. If you don’t need results outside a certain radius, use this property to limit the search and improve kernel performance. If the nonzero pixels are outside the specified radius, the search result is some number larger that the radius.

The default value for this property is [`greatestFiniteMagnitude`](https://developer.apple.com/documentation/Swift/Float/greatestFiniteMagnitude), which results in an exact Euclidean distance transform. Typical values for this property are `32`, `64`, `96`, and `128`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimageeuclideandistancetransform/searchlimitradius)*