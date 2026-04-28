# regionOfInterest

**Framework**: Vision  
**Kind**: property  
**Required**: Yes

The region of the image where the framework performs the request.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
var regionOfInterest: NormalizedRect { get set }
```

#### Discussion

The system normalizes the rectangle to the dimensions of the processed image. Its origin is the image’s lower-left corner.

The default value is `{ { 0, 0 }, { 1, 1 } }`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/imageprocessingrequest/regionofinterest)*