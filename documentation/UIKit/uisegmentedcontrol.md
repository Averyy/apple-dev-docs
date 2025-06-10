# UISegmentedControl

**Framework**: UIKit  
**Kind**: class

A horizontal control that consists of multiple segments, each segment functioning as a discrete button.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UISegmentedControl
```

## Mentions

- [Attaching gesture recognizers to UIKit controls](attaching-gesture-recognizers-to-uikit-controls.md)

#### Overview

A segmented control can display a title (an [`NSString`](https://developer.apple.com/documentation/Foundation/NSString) object) or an image ([`UIImage`](uiimage.md) object). The [`UISegmentedControl`](uisegmentedcontrol.md) object automatically resizes segments to fit proportionally within their superview unless they have a specific width set. When you add and remove segments, you can request that the action be animated with sliding and fading effects.

You register the target-action methods for a segmented control using the [`valueChanged`](uicontrol/event/valuechanged.md) constant as shown below.

How you configure a segmented control can affect its display behavior:

- If you set a segmented control to have a momentary style, a segment doesn’t show itself as selected (blue background) when the user touches it. The disclosure button is always momentary and doesn’t affect the actual selection.
- In versions of iOS prior to 3.0, if a segmented control has only two segments, then it behaves like a switch — tapping the currently-selected segment causes the other segment to be selected. In iOS 3.0 and later, tapping the currently-selected segment doesn’t cause the other segment to be selected.

##### Customize Appearance

You can customize the appearance of segmented controls using the methods listed in [`Customizing appearance`](uisegmentedcontrol#Customizing-appearance.md). You can customize the appearance of all segmented controls using the appearance proxy (for example, `[UISegmentedControl appearance]`), or just of a single control.

When customizing appearance, in general, you should specify a value for the normal state of a property to be used by other states which don’t have a custom value set. Similarly, when a property is dependent on the bar metrics (on the iPhone in landscape orientation, bars have a different height from standard), you should make sure you specify a value for [`UIBarMetrics.default`](uibarmetrics/default.md).

In the case of the segmented control, appearance properties for [`landscapePhone`](uibarmetrics/landscapephone.md) are only respected for segmented controls in the smaller navigation and toolbars that are used in landscape orientation on the iPhone.

To provide complete customization, you need to provide divider images for different state combinations, using [`setDividerImage(_:forLeftSegmentState:rightSegmentState:barMetrics:)`](uisegmentedcontrol/setdividerimage(_:forleftsegmentstate:rightsegmentstate:barmetrics:).md):

## Topics

### Creating a segmented control
- [init(items: [Any]?)](uisegmentedcontrol/init(items:).md)
  Creates a segmented control with segments having the given titles or images.
- [convenience init(frame: CGRect, actions: [UIAction])](uisegmentedcontrol/init(frame:actions:).md)
  Creates a segmented control with the given frame and adds segments for the actions you specify.
- [init(frame: CGRect)](uisegmentedcontrol/init(frame:).md)
  Creates an empty segmented control with the frame you specify.
- [init?(coder: NSCoder)](uisegmentedcontrol/init(coder:).md)
  Creates a segmented control with data from an unarchiver.
### Managing segment content
- [func setImage(UIImage?, forSegmentAt: Int)](uisegmentedcontrol/setimage(_:forsegmentat:).md)
  Sets the content of a segment to a given image.
- [func imageForSegment(at: Int) -> UIImage?](uisegmentedcontrol/imageforsegment(at:).md)
  Returns the image for a specific segment.
- [func setTitle(String?, forSegmentAt: Int)](uisegmentedcontrol/settitle(_:forsegmentat:).md)
  Sets the title of a segment.
- [func titleForSegment(at: Int) -> String?](uisegmentedcontrol/titleforsegment(at:).md)
  Returns the title of the specified segment.
### Managing segment actions
- [func actionForSegment(at: Int) -> UIAction?](uisegmentedcontrol/actionforsegment(at:).md)
  Fetches the action of the segment at the index you specify, if one exists.
- [func setAction(UIAction, forSegmentAt: Int)](uisegmentedcontrol/setaction(_:forsegmentat:).md)
  Sets the action for the segment at the index you specify.
### Managing segments
- [var numberOfSegments: Int](uisegmentedcontrol/numberofsegments.md)
  Returns the number of segments the segmented control has.
- [func segmentIndex(identifiedBy: UIAction.Identifier) -> Int](uisegmentedcontrol/segmentindex(identifiedby:).md)
  The index of a segment with an action that has an identifier matching the identifier you specify.
- [func insertSegment(action: UIAction, at: Int, animated: Bool)](uisegmentedcontrol/insertsegment(action:at:animated:).md)
  Insert a segment with the action you specify at the given index.
- [func insertSegment(with: UIImage?, at: Int, animated: Bool)](uisegmentedcontrol/insertsegment(with:at:animated:).md)
  Inserts a segment at the position you specify and gives it an image as content.
- [func insertSegment(withTitle: String?, at: Int, animated: Bool)](uisegmentedcontrol/insertsegment(withtitle:at:animated:).md)
  Inserts a segment at the position you specify and gives it a title as content.
- [func removeAllSegments()](uisegmentedcontrol/removeallsegments.md)
  Removes all segments of the segmented control.
- [func removeSegment(at: Int, animated: Bool)](uisegmentedcontrol/removesegment(at:animated:).md)
  Removes the segment you specify from the segmented control, optionally animating the transition.
- [var selectedSegmentIndex: Int](uisegmentedcontrol/selectedsegmentindex.md)
  The index number that identifies the selected segment that the user last touched.
- [class var noSegment: Int](uisegmentedcontrol/nosegment.md)
  A segment index value indicating that there’s no selected segment.
### Managing segment behavior and appearance
- [var isMomentary: Bool](uisegmentedcontrol/ismomentary.md)
  A Boolean value that determines whether segments in the segmented control show selected state.
- [func setEnabled(Bool, forSegmentAt: Int)](uisegmentedcontrol/setenabled(_:forsegmentat:).md)
  Enables the segment you specify.
- [func isEnabledForSegment(at: Int) -> Bool](uisegmentedcontrol/isenabledforsegment(at:).md)
  Returns whether the indicated segment is enabled.
- [func setContentOffset(CGSize, forSegmentAt: Int)](uisegmentedcontrol/setcontentoffset(_:forsegmentat:).md)
  Adjusts the offset for drawing the content (image or text) of the specified segment.
- [func contentOffsetForSegment(at: Int) -> CGSize](uisegmentedcontrol/contentoffsetforsegment(at:).md)
  Returns the offset for drawing the content (image or text) of the segment you specify.
- [func setWidth(CGFloat, forSegmentAt: Int)](uisegmentedcontrol/setwidth(_:forsegmentat:).md)
  Sets the width of the segment at the index you specify.
- [func widthForSegment(at: Int) -> CGFloat](uisegmentedcontrol/widthforsegment(at:).md)
  Returns the width of the segment at the index you specify.
- [var apportionsSegmentWidthsByContent: Bool](uisegmentedcontrol/apportionssegmentwidthsbycontent.md)
  Indicates whether the control attempts to adjust segment widths based on their content widths.
### Customizing appearance
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
- [func setDividerImage(UIImage?, forLeftSegmentState: UIControl.State, rightSegmentState: UIControl.State, barMetrics: UIBarMetrics)](uisegmentedcontrol/setdividerimage(_:forleftsegmentstate:rightsegmentstate:barmetrics:).md)
  Sets the divider image to use for a given combination of left and right segment states and bar metrics.
- [func titleTextAttributes(for: UIControl.State) -> [NSAttributedString.Key : Any]?](uisegmentedcontrol/titletextattributes(for:).md)
  Returns the text attributes of the title for a given control state.
- [func setTitleTextAttributes([NSAttributedString.Key : Any]?, for: UIControl.State)](uisegmentedcontrol/settitletextattributes(_:for:).md)
  Sets the text attributes of the title for a given control state.

## Relationships

### Inherits From
- [UIControl](uicontrol.md)
### Conforms To
- [CALayerDelegate](../QuartzCore/CALayerDelegate.md)
- [CVarArg](../Swift/CVarArg.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [UIAccessibilityIdentification](uiaccessibilityidentification.md)
- [UIActivityItemsConfigurationProviding](uiactivityitemsconfigurationproviding.md)
- [UIAppearance](uiappearance.md)
- [UIAppearanceContainer](uiappearancecontainer.md)
- [UIContextMenuInteractionDelegate](uicontextmenuinteractiondelegate.md)
- [UICoordinateSpace](uicoordinatespace.md)
- [UIDynamicItem](uidynamicitem.md)
- [UIFocusEnvironment](uifocusenvironment.md)
- [UIFocusItem](uifocusitem.md)
- [UIFocusItemContainer](uifocusitemcontainer.md)
- [UILargeContentViewerItem](uilargecontentvieweritem.md)
- [UIPasteConfigurationSupporting](uipasteconfigurationsupporting.md)
- [UIPopoverPresentationControllerSourceItem](uipopoverpresentationcontrollersourceitem.md)
- [UIResponderStandardEditActions](uiresponderstandardeditactions.md)
- [UISpringLoadedInteractionSupporting](uispringloadedinteractionsupporting.md)
- [UITraitChangeObservable](uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](uitraitenvironment.md)
- [UIUserActivityRestoring](uiuseractivityrestoring.md)

## See Also

- [Responding to control-based events using target-action](responding-to-control-based-events-using-target-action.md)
  Handle user input by connecting buttons, sliders, and other controls to your app’s code using the target-action design pattern.
- [class UIControl](uicontrol.md)
  The base class for controls, which are visual elements that convey a specific action or intention in response to user interactions.
- [class UIButton](uibutton.md)
  A control that executes your custom code in response to user interactions.
- [class UIColorWell](uicolorwell.md)
  A control that displays a color picker.
- [class UIDatePicker](uidatepicker.md)
  A control for inputting date and time values.
- [class UIPageControl](uipagecontrol.md)
  A control that displays a horizontal series of dots, each of which corresponds to a page in the app’s document or other data-model entity.
- [class UISlider](uislider.md)
  A control for selecting a single value from a continuous range of values.
- [class UIStepper](uistepper.md)
  A control for incrementing or decrementing a value.
- [class UISwitch](uiswitch.md)
  A control that offers a binary choice, such as on/off.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisegmentedcontrol)*