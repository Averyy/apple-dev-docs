# contentOffsetForSegment(at:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns the offset for drawing the content (image or text) of the segment you specify.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func contentOffsetForSegment(at segment: Int) -> CGSize
```

```objc
- (CGSize) contentOffsetForSegmentAtIndex:(NSUInteger) segment;
```

#### Return Value

The offset (as a [`CGSize`](../../CoreFoundation/cgsize.md) structure) from the origin of the segment at which to draw the segment’s content.

## Parameters

- `segment`: An index number that identifies a segment in the control. It must be a number between 0 and the number of segments ([`numberOfSegments`](./numberofsegments.md)) minus 1; the segmented control pins values exceeding this upper range to the last segment.

## See Also

### Managing segment behavior and appearance
- [var isMomentary: Bool](./ismomentary.md)
  A Boolean value that determines whether segments in the segmented control show selected state.
- [func setEnabled(Bool, forSegmentAt: Int)](./setenabled%28_,forsegmentat%29.md)
  Enables the segment you specify.
- [func isEnabledForSegment(at: Int) -> Bool](./isenabledforsegment%28at%29.md)
  Returns whether the indicated segment is enabled.
- [func setContentOffset(CGSize, forSegmentAt: Int)](./setcontentoffset%28_,forsegmentat%29.md)
  Adjusts the offset for drawing the content (image or text) of the specified segment.
- [func setWidth(CGFloat, forSegmentAt: Int)](./setwidth%28_,forsegmentat%29.md)
  Sets the width of the segment at the index you specify.
- [func widthForSegment(at: Int) -> CGFloat](./widthforsegment%28at%29.md)
  Returns the width of the segment at the index you specify.
- [var apportionsSegmentWidthsByContent: Bool](./apportionssegmentwidthsbycontent.md)
  Indicates whether the control attempts to adjust segment widths based on their content widths.
- [segmentedControlStyle](./segmentedcontrolstyle.md)
  The style of the segmented control.
- [UISegmentedControlStyle](../uisegmentedcontrolstyle.md)
  The styles of the segmented control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisegmentedcontrol/contentoffsetforsegment(at:))*