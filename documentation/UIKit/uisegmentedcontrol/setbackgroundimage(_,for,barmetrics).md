# setBackgroundImage(_:for:barMetrics:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Sets the background image for given state and bar metrics.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func setBackgroundImage(_ backgroundImage: UIImage?, for state: UIControl.State, barMetrics: UIBarMetrics)
```

```objc
- (void) setBackgroundImage:(UIImage *) backgroundImage forState:(UIControlState) state barMetrics:(UIBarMetrics) barMetrics;
```

#### Discussion

If `backgroundImage` is an image that [`resizableImage(withCapInsets:)`](../uiimage/resizableimage%28withcapinsets%29.md) returns, the system calculates the cap widths from that information.

If `backgroundImage` isn’t an image that [`resizableImage(withCapInsets:)`](../uiimage/resizableimage%28withcapinsets%29.md) returns, the system calculates the cap width by subtracting one from the image’s width, then dividing by 2. The system uses the cap widths as the margins for text placement. To adjust the margin, use the margin adjustment methods.

Generally, specify a value for the [`normal`](../uicontrol/state-swift.struct/normal.md) state. The segmented control uses this state for other states that don’t have a custom value set.

Similarly, when a property is dependent on the bar metrics, be sure to specify a value for [`UIBarMetrics.default`](../uibarmetrics/default.md). The segmented control respects properties for [`UIBarMetrics.compact`](../uibarmetrics/compact.md) only when the control is in smaller navigation and toolbars.

## Parameters

- `backgroundImage`: The background image to use for `state` and `barMetrics`.
- `state`: A control state.
- `barMetrics`: Bar metrics.

## See Also

### Customizing appearance
- [var selectedSegmentTintColor: UIColor?](./selectedsegmenttintcolor.md)
  The color to use for highlighting the currently selected segment.
- [func backgroundImage(for: UIControl.State, barMetrics: UIBarMetrics) -> UIImage?](./backgroundimage%28for,barmetrics%29.md)
  Returns the background image for a given state and bar metrics.
- [func contentPositionAdjustment(forSegmentType: UISegmentedControl.Segment, barMetrics: UIBarMetrics) -> UIOffset](./contentpositionadjustment%28forsegmenttype,barmetrics%29.md)
  Returns the positioning offset for a given segment and bar metrics.
- [func setContentPositionAdjustment(UIOffset, forSegmentType: UISegmentedControl.Segment, barMetrics: UIBarMetrics)](./setcontentpositionadjustment%28_,forsegmenttype,barmetrics%29.md)
  Sets the content positioning offset for a given segment and bar metrics.
- [UISegmentedControl.Segment](./segment.md)
  Constants for specifying a segment in a control.
- [func dividerImage(forLeftSegmentState: UIControl.State, rightSegmentState: UIControl.State, barMetrics: UIBarMetrics) -> UIImage?](./dividerimage%28forleftsegmentstate,rightsegmentstate,barmetrics%29.md)
  Returns the divider image used for a given combination of left and right segment states and bar metrics.
- [func setDividerImage(UIImage?, forLeftSegmentState: UIControl.State, rightSegmentState: UIControl.State, barMetrics: UIBarMetrics)](./setdividerimage%28_,forleftsegmentstate,rightsegmentstate,barmetrics%29.md)
  Sets the divider image to use for a given combination of left and right segment states and bar metrics.
- [func titleTextAttributes(for: UIControl.State) -> [NSAttributedString.Key : Any]?](./titletextattributes%28for%29.md)
  Returns the text attributes of the title for a given control state.
- [func setTitleTextAttributes([NSAttributedString.Key : Any]?, for: UIControl.State)](./settitletextattributes%28_,for%29.md)
  Sets the text attributes of the title for a given control state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisegmentedcontrol/setbackgroundimage(_:for:barmetrics:))*