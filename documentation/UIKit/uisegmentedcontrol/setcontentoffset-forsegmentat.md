# setContentOffset(_:forSegmentAt:)

**Framework**: UIKit  
**Kind**: method

Adjusts the offset for drawing the content (image or text) of the specified segment.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func setContentOffset(_ offset: CGSize, forSegmentAt segment: Int)
```

## Parameters

- `offset`: The offset (as a   type) from the origin of the segment at which to draw the segment’s content. The default offset is (0,0).
- `segment`: An index number identifying a segment in the control. It must be a number between 0 and the number of segments ( ) minus 1; the segmented control pins values exceeding this upper range to the last segment.

## See Also

- [var isMomentary: Bool](uisegmentedcontrol/ismomentary.md)
  A Boolean value that determines whether segments in the segmented control show selected state.
- [func setEnabled(Bool, forSegmentAt: Int)](uisegmentedcontrol/setenabled(_:forsegmentat:).md)
  Enables the segment you specify.
- [func isEnabledForSegment(at: Int) -> Bool](uisegmentedcontrol/isenabledforsegment(at:).md)
  Returns whether the indicated segment is enabled.
- [func contentOffsetForSegment(at: Int) -> CGSize](uisegmentedcontrol/contentoffsetforsegment(at:).md)
  Returns the offset for drawing the content (image or text) of the segment you specify.
- [func setWidth(CGFloat, forSegmentAt: Int)](uisegmentedcontrol/setwidth(_:forsegmentat:).md)
  Sets the width of the segment at the index you specify.
- [func widthForSegment(at: Int) -> CGFloat](uisegmentedcontrol/widthforsegment(at:).md)
  Returns the width of the segment at the index you specify.
- [var apportionsSegmentWidthsByContent: Bool](uisegmentedcontrol/apportionssegmentwidthsbycontent.md)
  Indicates whether the control attempts to adjust segment widths based on their content widths.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisegmentedcontrol/setcontentoffset(_:forsegmentat:))*