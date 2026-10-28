# UISegmentedControlStyle

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

The styles of the segmented control.

**Availability**:
- iOS 2.0+ - Deprecated in 7.0
- iPadOS 2.0+ - Deprecated in 7.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Segmented controls no longer support multiple styles using this functionality. Use the other appearance modification methods and properties to customize a segmented control.

## Declaration

```c
enum UISegmentedControlStyle : NSInteger;
```

## Overview

You use these constants as values for the [`segmentedControlStyle`](./uisegmentedcontrol/segmentedcontrolstyle.md) property.

## Topics

### Constants
- [UISegmentedControlStylePlain](./uisegmentedcontrolstyle/uisegmentedcontrolstyleplain.md)
  The large plain style for segmented controls.
- [UISegmentedControlStyleBordered](./uisegmentedcontrolstyle/uisegmentedcontrolstylebordered.md)
  The large bordered style for segmented controls.
- [UISegmentedControlStyleBar](./uisegmentedcontrolstyle/uisegmentedcontrolstylebar.md)
  The small toolbar style for segmented controls.
- [UISegmentedControlStyleBezeled](./uisegmentedcontrolstyle/uisegmentedcontrolstylebezeled.md)
  The large bezeled style for segmented controls.

## See Also

### Managing segment behavior and appearance
- [var isMomentary: Bool](./uisegmentedcontrol/ismomentary.md)
  A Boolean value that determines whether segments in the segmented control show selected state.
- [func setEnabled(Bool, forSegmentAt: Int)](./uisegmentedcontrol/setenabled%28_,forsegmentat%29.md)
  Enables the segment you specify.
- [func isEnabledForSegment(at: Int) -> Bool](./uisegmentedcontrol/isenabledforsegment%28at%29.md)
  Returns whether the indicated segment is enabled.
- [func setContentOffset(CGSize, forSegmentAt: Int)](./uisegmentedcontrol/setcontentoffset%28_,forsegmentat%29.md)
  Adjusts the offset for drawing the content (image or text) of the specified segment.
- [func contentOffsetForSegment(at: Int) -> CGSize](./uisegmentedcontrol/contentoffsetforsegment%28at%29.md)
  Returns the offset for drawing the content (image or text) of the segment you specify.
- [func setWidth(CGFloat, forSegmentAt: Int)](./uisegmentedcontrol/setwidth%28_,forsegmentat%29.md)
  Sets the width of the segment at the index you specify.
- [func widthForSegment(at: Int) -> CGFloat](./uisegmentedcontrol/widthforsegment%28at%29.md)
  Returns the width of the segment at the index you specify.
- [var apportionsSegmentWidthsByContent: Bool](./uisegmentedcontrol/apportionssegmentwidthsbycontent.md)
  Indicates whether the control attempts to adjust segment widths based on their content widths.
- [segmentedControlStyle](./uisegmentedcontrol/segmentedcontrolstyle.md)
  The style of the segmented control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisegmentedcontrolstyle)*