# titleForSegment(at:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns the title of the specified segment.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func titleForSegment(at segment: Int) -> String?
```

```objc
- (NSString *) titleForSegmentAtIndex:(NSUInteger) segment;
```

## Return Value

Returns the string (title) assigned to the receiver as content. If there is no title, it returns `nil`.

## Parameters

- `segment`: An index number identifying a segment in the control. It must be a number between 0 and the number of segments ([`numberOfSegments`](./numberofsegments.md)) minus 1; the segmented control pins values exceeding this upper range to the last segment.

## See Also

### Managing segment content
- [func setImage(UIImage?, forSegmentAt: Int)](./setimage%28_,forsegmentat%29.md)
  Sets the content of a segment to a given image.
- [func imageForSegment(at: Int) -> UIImage?](./imageforsegment%28at%29.md)
  Returns the image for a specific segment.
- [func setTitle(String?, forSegmentAt: Int)](./settitle%28_,forsegmentat%29.md)
  Sets the title of a segment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisegmentedcontrol/titleforsegment(at:))*