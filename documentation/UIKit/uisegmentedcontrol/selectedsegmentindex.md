# selectedSegmentIndex

**Framework**: UIKit  
**Kind**: property

The index number that identifies the selected segment that the user last touched.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var selectedSegmentIndex: Int { get set }
```

#### Discussion

The default value is [`noSegment`](uisegmentedcontrol/nosegment.md) (no segment selected) until the user touches a segment. Set this property to `-1` to turn off the current selection. [`UISegmentedControl`](uisegmentedcontrol.md) ignores this property when [`isMomentary`](uisegmentedcontrol/ismomentary.md) is [`true`](https://developer.apple.com/documentation/Swift/true). When the user touches a segment to change the selection, the system generates the control event [`valueChanged`](uicontrol/event/valuechanged.md). If you set up the segmented control to respond to this control event, it sends an action message to its target.

## See Also

- [var numberOfSegments: Int](uisegmentedcontrol/numberofsegments.md)
  Returns the number of segments the segmented control has.
- [func segmentIndex(identifiedBy: UIAction.Identifier) -> Int](uisegmentedcontrol/segmentindex(identifiedby:).md)
  The index of a segment with an action that has an identifier matching the identifier you specify.
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
- [class var noSegment: Int](uisegmentedcontrol/nosegment.md)
  A segment index value indicating that there’s no selected segment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisegmentedcontrol/selectedsegmentindex)*