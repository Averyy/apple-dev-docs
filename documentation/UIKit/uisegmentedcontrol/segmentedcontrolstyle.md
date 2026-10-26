# segmentedControlStyle

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The style of the segmented control.

**Availability**:
- iOS 2.0+ - Deprecated in 7.0
- iPadOS 2.0+ - Deprecated in 7.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Segmented controls no longer support multiple styles using this functionality. Use the other appearance modification methods and properties to customize a segmented control.

## Declaration

```objc
@property (nonatomic) UISegmentedControlStyle segmentedControlStyle;
```

#### Discussion

The default style is [`UISegmentedControlStylePlain`](../uisegmentedcontrolstyle/uisegmentedcontrolstyleplain.md). See [`UISegmentedControlStyle`](../uisegmentedcontrolstyle.md) for descriptions of valid constants.

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
- [func contentOffsetForSegment(at: Int) -> CGSize](./contentoffsetforsegment%28at%29.md)
  Returns the offset for drawing the content (image or text) of the segment you specify.
- [func setWidth(CGFloat, forSegmentAt: Int)](./setwidth%28_,forsegmentat%29.md)
  Sets the width of the segment at the index you specify.
- [func widthForSegment(at: Int) -> CGFloat](./widthforsegment%28at%29.md)
  Returns the width of the segment at the index you specify.
- [var apportionsSegmentWidthsByContent: Bool](./apportionssegmentwidthsbycontent.md)
  Indicates whether the control attempts to adjust segment widths based on their content widths.
- [UISegmentedControlStyle](../uisegmentedcontrolstyle.md)
  The styles of the segmented control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisegmentedcontrol/segmentedcontrolstyle)*