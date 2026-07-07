# boundingBox(for:)

**Framework**: Vision  
**Kind**: method

Calculates the bounding box around the characters in the range of a string.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+

## Declaration

```swift
@nonobjc
func boundingBox(for range: Range<String.Index>) throws -> VNRectangleObservation?
```

#### Return Value

A bounding box.

#### Discussion

Bounding boxes aren’t always an exact fit around the characters. Use them to display in user interfaces to provide general guidance, but avoid using their contents for image processing.

The bounding box that returns from this method differs based on the value of [`recognitionLevel`](vnrecognizetextrequest/recognitionlevel.md), as follows:

| [`VNRequestTextRecognitionLevel.fast`](vnrequesttextrecognitionlevel/fast.md) | The bounding box has character precision. When you specify a range from `0` to `1`, the value that returns is the first character’s bounding box. |
| --- | --- |
| [`VNRequestTextRecognitionLevel.accurate`](vnrequesttextrecognitionlevel/accurate.md) | The bounding box has word precision. When you specify a range from `0` to `1`, or `1` to `2`, the value that returns is the bounding box of the whole word containing the first character. |

## Parameters

- `range`: The range of the characters in the text string to draw a bounding box around.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnrecognizedtext/boundingbox(for:))*