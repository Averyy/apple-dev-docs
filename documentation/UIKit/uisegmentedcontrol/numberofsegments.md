# numberOfSegments

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

Returns the number of segments the segmented control has.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var numberOfSegments: Int { get }
```

```objc
@property (nonatomic, readonly) NSUInteger numberOfSegments;
```

## See Also

### Managing segments
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
- [class var noSegment: Int](./nosegment.md)
  A segment index value indicating that there’s no selected segment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisegmentedcontrol/numberofsegments)*