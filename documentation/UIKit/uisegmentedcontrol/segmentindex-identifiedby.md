# segmentIndex(identifiedBy:)

**Framework**: UIKit  
**Kind**: method

The index of a segment with an action that has an identifier matching the identifier you specify.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func segmentIndex(identifiedBy actionIdentifier: UIAction.Identifier) -> Int
```

#### Return Value

The index of the segment with an action that has a matching identifier, or [`NSNotFound`](https://developer.apple.com/documentation/Foundation/NSNotFound-4qp9h) if no matching action is found.

## Parameters

- `actionIdentifier`: The   to match.

## See Also

- [var numberOfSegments: Int](uisegmentedcontrol/numberofsegments.md)
  Returns the number of segments the segmented control has.
- [func insertSegment(action: UIAction, at: Int, animated: Bool)](uisegmentedcontrol/insertsegment(action:at:animated:).md)
  Insert a segment with the action you specify at the given index.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisegmentedcontrol/segmentindex(identifiedby:))*