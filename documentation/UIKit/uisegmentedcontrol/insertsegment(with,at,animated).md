# insertSegment(with:at:animated:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Inserts a segment at the position you specify and gives it an image as content.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func insertSegment(with image: UIImage?, at segment: Int, animated: Bool)
```

```objc
- (void) insertSegmentWithImage:(UIImage *) image atIndex:(NSUInteger) segment animated:(BOOL) animated;
```

## Parameters

- `image`: An image object to use as the content of the segment.
- `segment`: An index number identifying a segment in the control.

  `segment` must be a number in the range 0 to the number of segments ([`numberOfSegments`](./numberofsegments.md)) inclusive; the segmented control pins values exceeding this upper range to the last segment.

  The segmented control inserts the new segment immediately before the designated one.
- `animated`: [`true`](../../Swift/true.md) if the insertion of the new segment must animate; otherwise, [`false`](../../Swift/false.md).

## See Also

### Managing segments
- [var numberOfSegments: Int](./numberofsegments.md)
  Returns the number of segments the segmented control has.
- [func segmentIndex(identifiedBy: UIAction.Identifier) -> Int](./segmentindex%28identifiedby%29.md)
  The index of a segment with an action that has an identifier matching the identifier you specify.
- [func insertSegment(action: UIAction, at: Int, animated: Bool)](./insertsegment%28action,at,animated%29.md)
  Insert a segment with the action you specify at the given index.
- [func insertSegment(withTitle: String?, at: Int, animated: Bool)](./insertsegment%28withtitle,at,animated%29.md)
  Inserts a segment at the position you specify and gives it a title as content.
- [func removeAllSegments()](./removeallsegments%28%29.md)
  Removes all segments of the segmented control.
- [func removeSegment(at: Int, animated: Bool)](./removesegment%28at,animated%29.md)
  Removes the segment you specify from the segmented control, optionally animating the transition.
- [var selectedSegmentIndex: Int](./selectedsegmentindex.md)
  The index number that identifies the selected segment that the user last touched.
- [class var noSegment: Int](./nosegment.md)
  A segment index value indicating that there’s no selected segment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisegmentedcontrol/insertsegment(with:at:animated:))*