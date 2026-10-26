# isMomentary

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether segments in the segmented control show selected state.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var isMomentary: Bool { get set }
```

```objc
@property (nonatomic, getter=isMomentary) BOOL momentary;
```

#### Discussion

The default value of this property is [`false`](../../Swift/false.md). If it’s set to [`true`](../../Swift/true.md), segments in the control don’t show selected state and don’t update the value of [`selectedSegmentIndex`](./selectedsegmentindex.md) after tracking ends.

## See Also

### Managing segment behavior and appearance
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
- [segmentedControlStyle](./segmentedcontrolstyle.md)
  The style of the segmented control.
- [UISegmentedControlStyle](../uisegmentedcontrolstyle.md)
  The styles of the segmented control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisegmentedcontrol/ismomentary)*