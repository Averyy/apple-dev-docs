# insertSegment(action:at:animated:)

**Framework**: UIKit  
**Kind**: method

Insert a segment with the action you specify at the given index.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func insertSegment(action: UIAction, at segment: Int, animated: Bool)
```

#### Discussion

Segments prefer images over titles when the action contains both. Selecting a segment invokes the action’s [`UIActionHandler`](uiactionhandler.md), as well as handlers for the [`valueChanged`](uicontrol/event/valuechanged.md) and [`primaryActionTriggered`](uicontrol/event/primaryactiontriggered.md) control events.

If a segment exists with the action’s identifier, this method updates the existing segment is if the index is the same or removes the segment if the index is different.

## Parameters

- `action`: A   object to set on the segment at the index you specify.
- `segment`: An unsigned integer index of a segment.
- `animated`:   if the insertion of the new segment animates; otherwise,  .

## See Also

- [var numberOfSegments: Int](uisegmentedcontrol/numberofsegments.md)
  Returns the number of segments the segmented control has.
- [func segmentIndex(identifiedBy: UIAction.Identifier) -> Int](uisegmentedcontrol/segmentindex(identifiedby:).md)
  The index of a segment with an action that has an identifier matching the identifier you specify.
- [func insertSegment(with: UIImage?, at: Int, animated: Bool)](uisegmentedcontrol/insertsegment(with:at:animated:).md)
  Inserts a segment at the position you specify and gives it an image as content.
- [func insertSegment(withTitle: String?, at: Int, animated: Bool)](uisegmentedcontrol/insertsegment(withtitle:at:animated:).md)
  Inserts a segment at the position you specify and gives it a title as content.
- [func removeAllSegments()](uisegmentedcontrol/removeallsegments.md)
  Removes all segments of the segmented control.
- [func removeSegment(at: Int, animated: Bool)](uisegmentedcontrol/removesegment(at:animated:).md)
  Removes the segment you specify from the segmented control, optionally animating the transition.
- [var selectedSegmentIndex: Int](uisegmentedcontrol/selectedsegmentindex.md)
  The index number that identifies the selected segment that the user last touched.
- [class var noSegment: Int](uisegmentedcontrol/nosegment.md)
  A segment index value indicating that there’s no selected segment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisegmentedcontrol/insertsegment(action:at:animated:))*