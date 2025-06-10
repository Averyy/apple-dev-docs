# WKInterfaceSlider

**Framework**: WatchKit  
**Kind**: class

An interface element that lets users select a single floating-point value from a range of values.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
class WKInterfaceSlider
```

#### Overview

You configure the appearance of sliders in your storyboard file, including the images to display for the minimum and maximum value. At runtime, you use a slider object to enable the slider or set its value.

Do not subclass or create instances of this class yourself. Instead, define outlets in your interface controller class and connect them to the corresponding objects in your storyboard file. For example, to refer to a slider object in your interface, define a property with the following syntax in your interface controller class:

During the initialization of your interface controller, WatchKit creates a new instance of this class and assigns it to your outlet. At that point, you can use the object in your outlet to make changes to the onscreen slider.

When the user changes the value of a slider, WatchKit delivers the new value to the slider’s action method. The format of a slider’s action method is as follows:

Declare a method of this form in the interface controller class used to receive the slider’s new value. You can change the method name to anything you like. When configuring the slider in Xcode, connect its selector to your custom action method.

##### Interface Builder Configuration Options

Xcode lets you configure information about your slider in your storyboard file. The following table lists the attributes you can configure in your storyboard and their meaning.

| Attribute | Description |
| --- | --- |
| Value | The initial numerical value of the slider. This value must be between the specified minimum and maximum values. Clicking the slider buttons decreases or increases the current value until it reaches the minimum or maximum value. |
| Minimum | The smallest numerical value allowed by the slider. |
| Maximum | The largest numerical value allowed by the slider. |
| Steps | The number of steps between the minimum and maximum values. The slider uses the number of steps to determine how much to increment or decrement the value when the user interacts with the slider controls. |
| Continuous | The display style for the slider. When enabled, the slider value displays its value using a solid bar. When disabled, the slider displays its value using discrete steps. |
| Color | The color of the slider bar. You can also set the color programmatically using the [`setColor(_:)`](wkinterfaceslider/setcolor(_:).md) method. |
| Min Image | The name of the image to display next to the minimum value of the slider. This image must be bundled in the WatchKit app. |
| Max Image | The name of the image to display next to the maximum value of the slider. This image must be bundled with your WatchKit app. |
| Enabled | A checkbox indicating whether the slider is enabled and whether it sends events when its value changes. |

## Topics

### Setting the Slider Value
- [func setValue(Float)](wkinterfaceslider/setvalue(_:).md)
  Changes the value of the slider.
- [func setColor(UIColor?)](wkinterfaceslider/setcolor(_:).md)
  Sets the color of the slider bar.
- [func setNumberOfSteps(Int)](wkinterfaceslider/setnumberofsteps(_:).md)
  Sets the number of steps for the slider.
### Enabling the Slider
- [func setEnabled(Bool)](wkinterfaceslider/setenabled(_:).md)
  Enables or disables the slider.

## Relationships

### Inherits From
- [WKInterfaceObject](wkinterfaceobject.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class WKInterfaceLabel](wkinterfacelabel.md)
  An interface element that displays static text.
- [class WKInterfaceDate](wkinterfacedate.md)
  A label that displays the current date or time.
- [class WKInterfaceTimer](wkinterfacetimer.md)
  A label that displays a countdown or count-up timer.
- [class WKInterfaceButton](wkinterfacebutton.md)
  A button in the user interface of your watchOS app.
- [class WKInterfaceAuthorizationAppleIDButton](wkinterfaceauthorizationappleidbutton.md)
  A button that you can use to trigger a Sign in with Apple request.
- [class WKInterfacePaymentButton](wkinterfacepaymentbutton.md)
  A button that you can use to trigger payments through Apple Pay.
- [class WKInterfaceTextField](wkinterfacetextfield.md)
  An interface element that displays an editable text area.
- [class WKInterfaceSwitch](wkinterfaceswitch.md)
  An interface element that toggles between an On and Off state.
- [class WKInterfaceActivityRing](wkinterfaceactivityring.md)
  A view that displays data from a HealthKit activity summary object.
- [class WKInterfaceMap](wkinterfacemap.md)
  An interface element that displays a noninteractive map for the location you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfaceslider)*