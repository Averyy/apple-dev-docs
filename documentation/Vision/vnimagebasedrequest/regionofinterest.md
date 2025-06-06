# regionOfInterest

**Framework**: Vision  
**Kind**: property

The region of the image in which Vision will perform the request.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var regionOfInterest: CGRect { get set }
```

## Mentions

- [Detecting Human Body Poses in Images](detecting-human-body-poses-in-images.md)

#### Discussion

The rectangle is normalized to the dimensions of the processed image.  Its origin is specified relative to the image’s lower-left corner.

The default value is `{ { 0, 0 }, { 1, 1 } }`.

> ❗ **Important**:  The request will fail to perform if you set this property to a rectangle outside the normalized coordinate space.

 The request will fail to perform if you set this property to a rectangle outside the normalized coordinate space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnimagebasedrequest/regionofinterest)*