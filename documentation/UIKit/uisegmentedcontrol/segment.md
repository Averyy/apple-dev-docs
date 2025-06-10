# UISegmentedControl.Segment

**Framework**: UIKit  
**Kind**: enum

Constants for specifying a segment in a control.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
enum Segment
```

## Topics

### Constants
- [UISegmentedControl.Segment.any](uisegmentedcontrol/segment/any.md)
  Specifies any segment.
- [UISegmentedControl.Segment.left](uisegmentedcontrol/segment/left.md)
  The capped, leftmost segment.
- [UISegmentedControl.Segment.center](uisegmentedcontrol/segment/center.md)
  Any segment between the left and rightmost segments.
- [UISegmentedControl.Segment.right](uisegmentedcontrol/segment/right.md)
  The capped, rightmost segment.
- [UISegmentedControl.Segment.alone](uisegmentedcontrol/segment/alone.md)
  The standalone segment, capped on both ends.
### Initializers
- [init?(rawValue: Int)](uisegmentedcontrol/segment/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

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
- [func dividerImage(forLeftSegmentState: UIControl.State, rightSegmentState: UIControl.State, barMetrics: UIBarMetrics) -> UIImage?](uisegmentedcontrol/dividerimage(forleftsegmentstate:rightsegmentstate:barmetrics:).md)
  Returns the divider image used for a given combination of left and right segment states and bar metrics.
- [func setDividerImage(UIImage?, forLeftSegmentState: UIControl.State, rightSegmentState: UIControl.State, barMetrics: UIBarMetrics)](uisegmentedcontrol/setdividerimage(_:forleftsegmentstate:rightsegmentstate:barmetrics:).md)
  Sets the divider image to use for a given combination of left and right segment states and bar metrics.
- [func titleTextAttributes(for: UIControl.State) -> [NSAttributedString.Key : Any]?](uisegmentedcontrol/titletextattributes(for:).md)
  Returns the text attributes of the title for a given control state.
- [func setTitleTextAttributes([NSAttributedString.Key : Any]?, for: UIControl.State)](uisegmentedcontrol/settitletextattributes(_:for:).md)
  Sets the text attributes of the title for a given control state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisegmentedcontrol/segment)*