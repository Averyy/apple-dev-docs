# boundingBox(for:)

**Framework**: Vision  
**Kind**: method

Calculates the bounding box around the characters in the range of a string.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
func boundingBox(for range: Range<String.Index>) -> RectangleObservation?
```

#### Return Value

The bounding box surrounding the characters recognized in the image.

#### Discussion

Bounding boxes aren’t always an exact fit around the characters. Use them to display in user interfaces to provide general guidance, but avoid using their contents for image processing.

The coordinates of the bounding box are normalized to the dimensions of the processed image, with the origin at the lower-left corner of the image.

## Parameters

- `range`: The range of the characters in the text string to draw a bounding box around.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/recognizedtext/boundingbox(for:))*