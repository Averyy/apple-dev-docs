# removeSegment(at:animated:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Removes the segment you specify from the segmented control, optionally animating the transition.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func removeSegment(at segment: Int, animated: Bool)
```

```objc
- (void) removeSegmentAtIndex:(NSUInteger) segment animated:(BOOL) animated;
```

## Parameters

- `segment`: An index number identifying a segment in the control. It must be a number between 0 and the number of segments ([`numberOfSegments`](./numberofsegments.md)) minus 1; the segmented control pins values exceeding this upper range to the last segment.
- `animated`: [`true`](../../Swift/true.md) if the removal of the new segment must animate; otherwise, [`false`](../../Swift/false.md).

## See Also

### Managing segments
- [var numberOfSegments: Int](./numberofsegments.md)
  Returns the number of segments the segmented control has.
- [func segmentIndex(identifiedBy: UIAction.Identifier) -> Int](./segmentindex%28identifiedby%29.md)
  The index of a segment with an action that has an identifier matching the identifier you specify.
- [func insertSegment(action: UIAction, at: Int, animated: Bool)](./insertsegment%28action,at,animated%29.md)
  Insert a segment with the action you specify at the given index.
- [func insertSegment(with: UIImage?, at: Int, animated: Bool)](./insertsegment%28with,at,animated%29.md)
  Inserts a segment at the position you specify and gives it an image as content.
- [func insertSegment(withTitle: String?, at: Int, animated: Bool)](./insertsegment%28withtitle,at,animated%29.md)
  Inserts a segment at the position you specify and gives it a title as content.
- [func removeAllSegments()](./removeallsegments%28%29.md)
  Removes all segments of the segmented control.
- [var selectedSegmentIndex: Int](./selectedsegmentindex.md)
  The index number that identifies the selected segment that the user last touched.
- [class var noSegment: Int](./nosegment.md)
  A segment index value indicating that there’s no selected segment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisegmentedcontrol/removesegment(at:animated:))*