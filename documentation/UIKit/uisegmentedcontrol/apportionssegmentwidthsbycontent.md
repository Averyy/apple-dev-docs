# apportionsSegmentWidthsByContent

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

Indicates whether the control attempts to adjust segment widths based on their content widths.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var apportionsSegmentWidthsByContent: Bool { get set }
```

```objc
@property (nonatomic) BOOL apportionsSegmentWidthsByContent;
```

## Discussion

If the value of this property is [`true`](../../Swift/true.md), for segments whose width value is `0`, the control attempts to adjust segment widths based on their content widths.

The default is [`false`](../../Swift/false.md).

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
- [segmentedControlStyle](./segmentedcontrolstyle.md)
  The style of the segmented control.
- [UISegmentedControlStyle](../uisegmentedcontrolstyle.md)
  The styles of the segmented control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisegmentedcontrol/apportionssegmentwidthsbycontent)*