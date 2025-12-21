# setImage(_:forSegmentAt:)

**Framework**: UIKit  
**Kind**: method

Sets the content of a segment to a given image.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func setImage(_ image: UIImage?, forSegmentAt segment: Int)
```

#### Discussion

A segment can have only an image or a title; it can’t have both. There’s no default image.

## Parameters

- `image`: An image object to display in the segment.
- `segment`: An index number identifying a segment in the control. It must be a number between 0 and the number of segments ( ) minus 1; the segmented control pins values exceeding this upper range to the last segment.

## See Also

- [func imageForSegment(at: Int) -> UIImage?](uisegmentedcontrol/imageforsegment(at:).md)
  Returns the image for a specific segment.
- [func setTitle(String?, forSegmentAt: Int)](uisegmentedcontrol/settitle(_:forsegmentat:).md)
  Sets the title of a segment.
- [func titleForSegment(at: Int) -> String?](uisegmentedcontrol/titleforsegment(at:).md)
  Returns the title of the specified segment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisegmentedcontrol/setimage(_:forsegmentat:))*