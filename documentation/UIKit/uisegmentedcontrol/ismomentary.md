# isMomentary

**Framework**: UIKit  
**Kind**: property

A Boolean value that determines whether segments in the segmented control show selected state.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var isMomentary: Bool { get set }
```

#### Discussion

The default value of this property is [`false`](https://developer.apple.com/documentation/swift/false). If it’s set to [`true`](https://developer.apple.com/documentation/swift/true), segments in the control don’t show selected state and don’t update the value of [`selectedSegmentIndex`](uisegmentedcontrol/selectedsegmentindex.md) after tracking ends.

## See Also

- [func setEnabled(Bool, forSegmentAt: Int)](uisegmentedcontrol/setenabled(_:forsegmentat:).md)
  Enables the segment you specify.
- [func isEnabledForSegment(at: Int) -> Bool](uisegmentedcontrol/isenabledforsegment(at:).md)
  Returns whether the indicated segment is enabled.
- [func setContentOffset(CGSize, forSegmentAt: Int)](uisegmentedcontrol/setcontentoffset(_:forsegmentat:).md)
  Adjusts the offset for drawing the content (image or text) of the specified segment.
- [func contentOffsetForSegment(at: Int) -> CGSize](uisegmentedcontrol/contentoffsetforsegment(at:).md)
  Returns the offset for drawing the content (image or text) of the segment you specify.
- [func setWidth(CGFloat, forSegmentAt: Int)](uisegmentedcontrol/setwidth(_:forsegmentat:).md)
  Sets the width of the segment at the index you specify.
- [func widthForSegment(at: Int) -> CGFloat](uisegmentedcontrol/widthforsegment(at:).md)
  Returns the width of the segment at the index you specify.
- [var apportionsSegmentWidthsByContent: Bool](uisegmentedcontrol/apportionssegmentwidthsbycontent.md)
  Indicates whether the control attempts to adjust segment widths based on their content widths.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisegmentedcontrol/ismomentary)*