# imageForSegment(at:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns the image for a specific segment.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func imageForSegment(at segment: Int) -> UIImage?
```

```objc
- (UIImage *) imageForSegmentAtIndex:(NSUInteger) segment;
```

## Return Value

Returns the image assigned to the receiver as content. If there is no image, it returns `nil`.

## Parameters

- `segment`: An index number identifying a segment in the control. It must be a number between 0 and the number of segments ([`numberOfSegments`](./numberofsegments.md)) minus 1; the segmented control pins values exceeding this upper range to the last segment.

## See Also

### Managing segment content
- [func setImage(UIImage?, forSegmentAt: Int)](./setimage%28_,forsegmentat%29.md)
  Sets the content of a segment to a given image.
- [func setTitle(String?, forSegmentAt: Int)](./settitle%28_,forsegmentat%29.md)
  Sets the title of a segment.
- [func titleForSegment(at: Int) -> String?](./titleforsegment%28at%29.md)
  Returns the title of the specified segment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisegmentedcontrol/imageforsegment(at:))*