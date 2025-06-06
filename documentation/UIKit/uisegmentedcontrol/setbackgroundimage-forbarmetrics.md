# setBackgroundImage(_:for:barMetrics:)

**Framework**: UIKit  
**Kind**: method

Sets the background image for given state and bar metrics.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func setBackgroundImage(_ backgroundImage: UIImage?, for state: UIControl.State, barMetrics: UIBarMetrics)
```

#### Discussion

If `backgroundImage` is an image that [`resizableImage(withCapInsets:)`](uiimage/resizableimage(withcapinsets:).md) returns, the system calculates the cap widths from that information.

If `backgroundImage` isn’t an image that [`resizableImage(withCapInsets:)`](uiimage/resizableimage(withcapinsets:).md) returns, the system calculates the cap width by subtracting one from the image’s width, then dividing by 2. The system uses the cap widths as the margins for text placement. To adjust the margin, use the margin adjustment methods.

Generally, specify a value for the [`normal`](uicontrol/state-swift.struct/normal.md) state. The segmented control uses this state for other states that don’t have a custom value set.

Similarly, when a property is dependent on the bar metrics, be sure to specify a value for [`UIBarMetrics.default`](uibarmetrics/default.md). The segmented control respects properties for [`UIBarMetrics.compact`](uibarmetrics/compact.md) only when the control is in smaller navigation and toolbars.

## Parameters

- `backgroundImage`: The background image to use for   and  .
- `state`: A control state.
- `barMetrics`: Bar metrics.

## See Also

- [var selectedSegmentTintColor: UIColor?](uisegmentedcontrol/selectedsegmenttintcolor.md)
  The color to use for highlighting the currently selected segment.
- [func backgroundImage(for: UIControl.State, barMetrics: UIBarMetrics) -> UIImage?](uisegmentedcontrol/backgroundimage(for:barmetrics:).md)
  Returns the background image for a given state and bar metrics.
- [func contentPositionAdjustment(forSegmentType: UISegmentedControl.Segment, barMetrics: UIBarMetrics) -> UIOffset](uisegmentedcontrol/contentpositionadjustment(forsegmenttype:barmetrics:).md)
  Returns the positioning offset for a given segment and bar metrics.
- [func setContentPositionAdjustment(UIOffset, forSegmentType: UISegmentedControl.Segment, barMetrics: UIBarMetrics)](uisegmentedcontrol/setcontentpositionadjustment(_:forsegmenttype:barmetrics:).md)
  Sets the content positioning offset for a given segment and bar metrics.
- [UISegmentedControl.Segment](uisegmentedcontrol/segment.md)
  Constants for specifying a segment in a control.
- [func dividerImage(forLeftSegmentState: UIControl.State, rightSegmentState: UIControl.State, barMetrics: UIBarMetrics) -> UIImage?](uisegmentedcontrol/dividerimage(forleftsegmentstate:rightsegmentstate:barmetrics:).md)
  Returns the divider image used for a given combination of left and right segment states and bar metrics.
- [func setDividerImage(UIImage?, forLeftSegmentState: UIControl.State, rightSegmentState: UIControl.State, barMetrics: UIBarMetrics)](uisegmentedcontrol/setdividerimage(_:forleftsegmentstate:rightsegmentstate:barmetrics:).md)
  Sets the divider image to use for a given combination of left and right segment states and bar metrics.
- [func titleTextAttributes(for: UIControl.State) -> [NSAttributedString.Key : Any]?](uisegmentedcontrol/titletextattributes(for:).md)
  Returns the text attributes of the title for a given control state.
- [func setTitleTextAttributes([NSAttributedString.Key : Any]?, for: UIControl.State)](uisegmentedcontrol/settitletextattributes(_:for:).md)
  Sets the text attributes of the title for a given control state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisegmentedcontrol/setbackgroundimage(_:for:barmetrics:))*