# insertSegment(action:at:animated:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Insert a segment with the action you specify at the given index.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func insertSegment(action: UIAction, at segment: Int, animated: Bool)
```

```objc
- (void) insertSegmentWithAction:(UIAction *) action atIndex:(NSUInteger) segment animated:(BOOL) animated;
```

## Discussion

Segments prefer images over titles when the action contains both. Selecting a segment invokes the action’s [`UIActionHandler`](../uiactionhandler.md), as well as handlers for the [`valueChanged`](../uicontrol/event/valuechanged.md) and [`primaryActionTriggered`](../uicontrol/event/primaryactiontriggered.md) control events.

If a segment exists with the action’s identifier, this method updates the existing segment is if the index is the same or removes the segment if the index is different.

## Parameters

- `action`: A [`UIAction`](../uiaction.md) object to set on the segment at the index you specify.
- `segment`: An unsigned integer index of a segment.
- `animated`: [`true`](../../Swift/true.md) if the insertion of the new segment animates; otherwise, [`false`](../../Swift/false.md).

## See Also

### Managing segments
- [var numberOfSegments: Int](./numberofsegments.md)
  Returns the number of segments the segmented control has.
- [func segmentIndex(identifiedBy: UIAction.Identifier) -> Int](./segmentindex%28identifiedby%29.md)
  The index of a segment with an action that has an identifier matching the identifier you specify.
- [func insertSegment(with: UIImage?, at: Int, animated: Bool)](./insertsegment%28with,at,animated%29.md)
  Inserts a segment at the position you specify and gives it an image as content.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisegmentedcontrol/insertsegment(action:at:animated:))*