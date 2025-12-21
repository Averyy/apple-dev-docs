# UISwitch

**Framework**: UIKit  
**Kind**: class

A control that offers a binary choice, such as on/off.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UISwitch
```

## Mentions

- [Attaching gesture recognizers to UIKit controls](attaching-gesture-recognizers-to-uikit-controls.md)
- [Choosing a user interface idiom for your Mac app](choosing-a-user-interface-idiom-for-your-mac-app.md)
- [Displaying a checkbox in your Mac app built with Mac Catalyst](displaying-a-checkbox-in-your-mac-app-built-with-mac-catalyst.md)

#### Overview

The [`UISwitch`](uiswitch.md) class declares a property and a method to control its on/off state. When a person manipulates the switch control (“flips” it), it triggers the [`valueChanged`](uicontrol/event/valuechanged.md) event.

You can customize the appearance of the switch by changing the color used to tint the switch when it’s on or off.

For information about basic view behaviors, see [`View Programming Guide for iOS`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/WindowsViews/Conceptual/ViewPG_iPhoneOS/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009503).

## Topics

### Creating a switch
- [init(frame: CGRect)](uiswitch/init(frame:).md)
  Creates a switch control.
- [init?(coder: NSCoder)](uiswitch/init(coder:).md)
  Creates a switch control from data in an unarchiver.
### Setting the on/off state
- [var isOn: Bool](uiswitch/ison.md)
  A Boolean value that determines whether the switch is in the on or off position.
- [func setOn(Bool, animated: Bool)](uiswitch/seton(_:animated:).md)
  Sets the state of the switch to the on or off position, optionally animating the transition.
### Setting the display style
- [Displaying a checkbox in your Mac app built with Mac Catalyst](displaying-a-checkbox-in-your-mac-app-built-with-mac-catalyst.md)
  Present a switch control as a Mac-style checkbox when your app runs in the Mac user interface idiom.
- [var preferredStyle: UISwitch.Style](uiswitch/preferredstyle.md)
  The preferred display style for the switch.
- [var style: UISwitch.Style](uiswitch/style-swift.property.md)
  The display style for the switch.
- [UISwitch.Style](uiswitch/style-swift.enum.md)
  Styles that determine the appearance of the switch.
- [var title: String?](uiswitch/title.md)
  The title displayed next to a checkbox-style switch.
### Customizing the appearance of the switch
- [var onTintColor: UIColor?](uiswitch/ontintcolor.md)
  The color used to tint the appearance of the switch when it’s in the on position.
- [var thumbTintColor: UIColor?](uiswitch/thumbtintcolor.md)
  The color used to tint the appearance of the thumb.
### Deprecated
- [var onImage: UIImage?](uiswitch/onimage.md)
  The image displayed when the switch is in the on position.
- [var offImage: UIImage?](uiswitch/offimage.md)
  The image displayed when the switch is in the off position.

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
- [class UIStepper](uistepper.md)
  A control for incrementing or decrementing a value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiswitch)*