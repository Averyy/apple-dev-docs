# apportionsSegmentWidthsByContent

**Framework**: UIKit  
**Kind**: property

Indicates whether the control attempts to adjust segment widths based on their content widths.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var apportionsSegmentWidthsByContent: Bool { get set }
```

#### Discussion

If the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true), for segments whose width value is `0`, the control attempts to adjust segment widths based on their content widths.

The default is [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [var isMomentary: Bool](uisegmentedcontrol/ismomentary.md)
  A Boolean value that determines whether segments in the segmented control show selected state.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisegmentedcontrol/apportionssegmentwidthsbycontent)*