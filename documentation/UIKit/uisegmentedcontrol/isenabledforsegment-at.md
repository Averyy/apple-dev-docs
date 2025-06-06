# isEnabledForSegment(at:)

**Framework**: UIKit  
**Kind**: method

Returns whether the indicated segment is enabled.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func isEnabledForSegment(at segment: Int) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the given segment is enabled and [`false`](https://developer.apple.com/documentation/swift/false) if the segment is disabled. By default, segments are enabled.

## Parameters

- `segment`: An index number identifying a segment in the control. It must be a number between 0 and the number of segments ( ) minus 1; the segmented control pins values exceeding this upper range to the last segment.

## See Also

- [var isMomentary: Bool](uisegmentedcontrol/ismomentary.md)
  A Boolean value that determines whether segments in the segmented control show selected state.
- [func setEnabled(Bool, forSegmentAt: Int)](uisegmentedcontrol/setenabled(_:forsegmentat:).md)
  Enables the segment you specify.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisegmentedcontrol/isenabledforsegment(at:))*