# contentPositionAdjustment(forSegmentType:barMetrics:)

**Framework**: UIKit  
**Kind**: method

Returns the positioning offset for a given segment and bar metrics.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func contentPositionAdjustment(forSegmentType leftCenterRightOrAlone: UISegmentedControl.Segment, barMetrics: UIBarMetrics) -> UIOffset
```

#### Return Value

The content positioning offset for the segment identified by `leftCenterRightOrAlone` and `barMetrics`.

#### Discussion

For more details, see [`setContentPositionAdjustment(_:forSegmentType:barMetrics:)`](uisegmentedcontrol/setcontentpositionadjustment(_:forsegmenttype:barmetrics:).md).

## Parameters

- `leftCenterRightOrAlone`: An identifier for a segment.
- `barMetrics`: Bar metrics.

## See Also

- [var selectedSegmentTintColor: UIColor?](uisegmentedcontrol/selectedsegmenttintcolor.md)
  The color to use for highlighting the currently selected segment.
- [func backgroundImage(for: UIControl.State, barMetrics: UIBarMetrics) -> UIImage?](uisegmentedcontrol/backgroundimage(for:barmetrics:).md)
  Returns the background image for a given state and bar metrics.
- [func setBackgroundImage(UIImage?, for: UIControl.State, barMetrics: UIBarMetrics)](uisegmentedcontrol/setbackgroundimage(_:for:barmetrics:).md)
  Sets the background image for given state and bar metrics.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisegmentedcontrol/contentpositionadjustment(forsegmenttype:barmetrics:))*