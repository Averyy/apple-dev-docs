# noSegment

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

A segment index value indicating that there’s no selected segment.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
class var noSegment: Int { get }
```

```c
UISegmentedControlNoSegment
```

#### Discussion

See [`selectedSegmentIndex`](./selectedsegmentindex.md) for more information.

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
- [func removeSegment(at: Int, animated: Bool)](./removesegment%28at,animated%29.md)
  Removes the segment you specify from the segmented control, optionally animating the transition.
- [var selectedSegmentIndex: Int](./selectedsegmentindex.md)
  The index number that identifies the selected segment that the user last touched.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisegmentedcontrol/nosegment)*