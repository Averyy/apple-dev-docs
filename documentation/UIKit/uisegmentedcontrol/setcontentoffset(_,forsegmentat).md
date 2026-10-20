# setContentOffset(_:forSegmentAt:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Adjusts the offset for drawing the content (image or text) of the specified segment.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func setContentOffset(_ offset: CGSize, forSegmentAt segment: Int)
```

```objc
- (void) setContentOffset:(CGSize) offset forSegmentAtIndex:(NSUInteger) segment;
```

## Parameters

- `offset`: The offset (as a [`CGSize`](../../CoreFoundation/cgsize.md) type) from the origin of the segment at which to draw the segment’s content. The default offset is (0,0).
- `segment`: An index number identifying a segment in the control. It must be a number between 0 and the number of segments ([`numberOfSegments`](./numberofsegments.md)) minus 1; the segmented control pins values exceeding this upper range to the last segment.

## See Also

### Managing segment behavior and appearance
- [var isMomentary: Bool](./ismomentary.md)
  A Boolean value that determines whether segments in the segmented control show selected state.
- [func setEnabled(Bool, forSegmentAt: Int)](./setenabled%28_,forsegmentat%29.md)
  Enables the segment you specify.
- [func isEnabledForSegment(at: Int) -> Bool](./isenabledforsegment%28at%29.md)
  Returns whether the indicated segment is enabled.
- [func contentOffsetForSegment(at: Int) -> CGSize](./contentoffsetforsegment%28at%29.md)
  Returns the offset for drawing the content (image or text) of the segment you specify.
- [func setWidth(CGFloat, forSegmentAt: Int)](./setwidth%28_,forsegmentat%29.md)
  Sets the width of the segment at the index you specify.
- [func widthForSegment(at: Int) -> CGFloat](./widthforsegment%28at%29.md)
  Returns the width of the segment at the index you specify.
- [var apportionsSegmentWidthsByContent: Bool](./apportionssegmentwidthsbycontent.md)
  Indicates whether the control attempts to adjust segment widths based on their content widths.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisegmentedcontrol/setcontentoffset(_:forsegmentat:))*