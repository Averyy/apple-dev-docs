# setDividerImage(_:forLeftSegmentState:rightSegmentState:barMetrics:)

**Framework**: UIKit  
**Kind**: method

Sets the divider image to use for a given combination of left and right segment states and bar metrics.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func setDividerImage(_ dividerImage: UIImage?, forLeftSegmentState leftState: UIControl.State, rightSegmentState rightState: UIControl.State, barMetrics: UIBarMetrics)
```

#### Discussion

To customize the segmented control appearance, provide divider images for the following cases:

- Between two unselected segments, where `leftState` and `rightState` are both [`normal`](uicontrol/state-swift.struct/normal.md)
- Between a selected segment on the left and an unselected on the right, where `leftState` is [`selected`](uicontrol/state-swift.struct/selected.md) and `rightState` is [`normal`](uicontrol/state-swift.struct/normal.md)
- Between an unselected segment on the left and a selected on the right, where `leftState` is [`normal`](uicontrol/state-swift.struct/normal.md) and `rightState` is [`selected`](uicontrol/state-swift.struct/selected.md)

## Parameters

- `dividerImage`: The divider image to use.
- `leftState`: The state of the left segment.
- `rightState`: The state of the right segment.
- `barMetrics`: Bar metrics.

## See Also

- [var selectedSegmentTintColor: UIColor?](uisegmentedcontrol/selectedsegmenttintcolor.md)
  The color to use for highlighting the currently selected segment.
- [func backgroundImage(for: UIControl.State, barMetrics: UIBarMetrics) -> UIImage?](uisegmentedcontrol/backgroundimage(for:barmetrics:).md)
  Returns the background image for a given state and bar metrics.
- [func setBackgroundImage(UIImage?, for: UIControl.State, barMetrics: UIBarMetrics)](uisegmentedcontrol/setbackgroundimage(_:for:barmetrics:).md)
  Sets the background image for given state and bar metrics.
- [func contentPositionAdjustment(forSegmentType: UISegmentedControl.Segment, barMetrics: UIBarMetrics) -> UIOffset](uisegmentedcontrol/contentpositionadjustment(forsegmenttype:barmetrics:).md)
  Returns the positioning offset for a given segment and bar metrics.
- [func setContentPositionAdjustment(UIOffset, forSegmentType: UISegmentedControl.Segment, barMetrics: UIBarMetrics)](uisegmentedcontrol/setcontentpositionadjustment(_:forsegmenttype:barmetrics:).md)
  Sets the content positioning offset for a given segment and bar metrics.
- [UISegmentedControl.Segment](uisegmentedcontrol/segment.md)
  Constants for specifying a segment in a control.
- [func dividerImage(forLeftSegmentState: UIControl.State, rightSegmentState: UIControl.State, barMetrics: UIBarMetrics) -> UIImage?](uisegmentedcontrol/dividerimage(forleftsegmentstate:rightsegmentstate:barmetrics:).md)
  Returns the divider image used for a given combination of left and right segment states and bar metrics.
- [func titleTextAttributes(for: UIControl.State) -> [NSAttributedString.Key : Any]?](uisegmentedcontrol/titletextattributes(for:).md)
  Returns the text attributes of the title for a given control state.
- [func setTitleTextAttributes([NSAttributedString.Key : Any]?, for: UIControl.State)](uisegmentedcontrol/settitletextattributes(_:for:).md)
  Sets the text attributes of the title for a given control state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisegmentedcontrol/setdividerimage(_:forleftsegmentstate:rightsegmentstate:barmetrics:))*