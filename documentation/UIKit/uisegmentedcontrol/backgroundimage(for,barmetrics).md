# backgroundImage(for:barMetrics:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns the background image for a given state and bar metrics.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func backgroundImage(for state: UIControl.State, barMetrics: UIBarMetrics) -> UIImage?
```

```objc
- (UIImage *) backgroundImageForState:(UIControlState) state barMetrics:(UIBarMetrics) barMetrics;
```

## Return Value

The background image for `state` and `barMetrics`.

## Discussion

For more details, see [`setBackgroundImage(_:for:barMetrics:)`](./setbackgroundimage%28_,for,barmetrics%29.md).

## Parameters

- `state`: A control state.
- `barMetrics`: Bar metrics.

## See Also

### Customizing appearance
- [var selectedSegmentTintColor: UIColor?](./selectedsegmenttintcolor.md)
  The color to use for highlighting the currently selected segment.
- [func setBackgroundImage(UIImage?, for: UIControl.State, barMetrics: UIBarMetrics)](./setbackgroundimage%28_,for,barmetrics%29.md)
  Sets the background image for given state and bar metrics.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisegmentedcontrol/backgroundimage(for:barmetrics:))*