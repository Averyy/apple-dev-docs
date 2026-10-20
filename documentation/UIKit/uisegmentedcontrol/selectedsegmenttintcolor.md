# selectedSegmentTintColor

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The color to use for highlighting the currently selected segment.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var selectedSegmentTintColor: UIColor? { get set }
```

```objc
@property (nonatomic, strong, nullable) UIColor * selectedSegmentTintColor;
```

## See Also

### Customizing appearance
- [func backgroundImage(for: UIControl.State, barMetrics: UIBarMetrics) -> UIImage?](./backgroundimage%28for,barmetrics%29.md)
  Returns the background image for a given state and bar metrics.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisegmentedcontrol/selectedsegmenttintcolor)*