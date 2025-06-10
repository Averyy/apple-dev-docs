# UIStepper

**Framework**: UIKit  
**Kind**: class

A control for incrementing or decrementing a value.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIStepper
```

## Mentions

- [Choosing a user interface idiom for your Mac app](choosing-a-user-interface-idiom-for-your-mac-app.md)
- [Attaching gesture recognizers to UIKit controls](attaching-gesture-recognizers-to-uikit-controls.md)

#### Overview

By default, pressing and holding a stepper’s button increments or decrements the stepper’s value repeatedly. The rate of change depends on how long the user continues pressing the control. To turn off this behavior, set the [`autorepeat`](uistepper/autorepeat.md) property to [`false`](https://developer.apple.com/documentation/swift/false).

The maximum value must be greater than or equal to the minimum value. If you set a maximum or minimum value that would break this invariant, both values are set to the new value. For example, if the minimum value is 200 and you set a maximum value of 100, then both the minimum and maximum become 200.

> ❗ **Important**:  [`UIStepper`](uistepper.md) isn’t available when the user interface idiom is [`UIUserInterfaceIdiom.mac`](uiuserinterfaceidiom/mac.md).

## Topics

### Configuring the stepper
- [var isContinuous: Bool](uistepper/iscontinuous.md)
  A Boolean value that determines whether to send value changes during user interaction or after user interaction ends.
- [var autorepeat: Bool](uistepper/autorepeat.md)
  A Boolean value that determines whether to repeatedly change the stepper’s value as the user presses and holds a stepper button.
- [var wraps: Bool](uistepper/wraps.md)
  A Boolean value that determines whether the stepper can wrap its value to the minimum or maximum value when incrementing and decrementing the value.
- [var minimumValue: Double](uistepper/minimumvalue.md)
  The lowest possible numeric value for the stepper.
- [var maximumValue: Double](uistepper/maximumvalue.md)
  The highest possible numeric value for the stepper.
- [var stepValue: Double](uistepper/stepvalue.md)
  The step, or increment, value for the stepper.
### Accessing the stepper’s value
- [var value: Double](uistepper/value.md)
  The numeric value of the stepper.
### Customizing appearance
- [func backgroundImage(for: UIControl.State) -> UIImage?](uistepper/backgroundimage(for:).md)
  Returns the background image associated with the specified control state.
- [func setBackgroundImage(UIImage?, for: UIControl.State)](uistepper/setbackgroundimage(_:for:).md)
  Sets the background image for the control when it’s in the specified state.
- [func decrementImage(for: UIControl.State) -> UIImage?](uistepper/decrementimage(for:).md)
  Returns the image used for the decrement glyph of the control.
- [func setDecrementImage(UIImage?, for: UIControl.State)](uistepper/setdecrementimage(_:for:).md)
  Sets the image to use for the decrement glyph of the control.
- [func dividerImage(forLeftSegmentState: UIControl.State, rightSegmentState: UIControl.State) -> UIImage?](uistepper/dividerimage(forleftsegmentstate:rightsegmentstate:).md)
  Returns the divider image for the given combination of left and right states.
- [func setDividerImage(UIImage?, forLeftSegmentState: UIControl.State, rightSegmentState: UIControl.State)](uistepper/setdividerimage(_:forleftsegmentstate:rightsegmentstate:).md)
  Sets the image to use for the given combination of left and right states.
- [func incrementImage(for: UIControl.State) -> UIImage?](uistepper/incrementimage(for:).md)
  Returns the image used for the increment glyph of the control.
- [func setIncrementImage(UIImage?, for: UIControl.State)](uistepper/setincrementimage(_:for:).md)
  Sets the image to use for the increment glyph of the control.

## Relationships

### Inherits From
- [UIControl](uicontrol.md)
### Conforms To
- [CALayerDelegate](../QuartzCore/CALayerDelegate.md)
- [CVarArg](../Swift/CVarArg.md)
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
- [class UISegmentedControl](uisegmentedcontrol.md)
  A horizontal control that consists of multiple segments, each segment functioning as a discrete button.
- [class UISlider](uislider.md)
  A control for selecting a single value from a continuous range of values.
- [class UISwitch](uiswitch.md)
  A control that offers a binary choice, such as on/off.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uistepper)*