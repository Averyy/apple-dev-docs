# WKInterfaceSlider

**Framework**: Watchkit  
**Kind**: class

An interface element that lets users select a single floating-point value from a range of values.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
class WKInterfaceSlider
```

## Overview

You configure the appearance of sliders in your storyboard file, including the images to display for the minimum and maximum value. At runtime, you use a slider object to enable the slider or set its value.

Do not subclass or create instances of this class yourself. Instead, define outlets in your interface controller class and connect them to the corresponding objects in your storyboard file. For example, to refer to a slider object in your interface, define a property with the following syntax in your interface controller class:

During the initialization of your interface controller, WatchKit creates a new instance of this class and assigns it to your outlet. At that point, you can use the object in your outlet to make changes to the onscreen slider.

When the user changes the value of a slider, WatchKit delivers the new value to the slider’s action method. The format of a slider’s action method is as follows:

Declare a method of this form in the interface controller class used to receive the slider’s new value. You can change the method name to anything you like. When configuring the slider in Xcode, connect its selector to your custom action method.

Xcode lets you configure information about your slider in your storyboard file. The following table lists the attributes you can configure in your storyboard and their meaning.

| r | o | w |
| --- | --- | --- |
| [{'type': 'paragraph', 'inlineContent': [{'text': 'Attribute', 'type': 'text'}]}] | [{'type': 'paragraph', 'inlineContent': [{'text': 'Description', 'type': 'text'}]}] |
| [{'type': 'paragraph', 'inlineContent': [{'text': 'Value', 'type': 'text'}]}] | [{'type': 'paragraph', 'inlineContent': [{'type': 'text', 'text': 'The initial numerical value of the slider. This value must be between the specified minimum and maximum values. Clicking the slider buttons decreases or increases the current value until it reaches the minimum or maximum value.'}]}] |
| [{'inlineContent': [{'type': 'text', 'text': 'Minimum'}], 'type': 'paragraph'}] | [{'inlineContent': [{'text': 'The smallest numerical value allowed by the slider.', 'type': 'text'}], 'type': 'paragraph'}] |
| [{'inlineContent': [{'text': 'Maximum', 'type': 'text'}], 'type': 'paragraph'}] | [{'inlineContent': [{'type': 'text', 'text': 'The largest numerical value allowed by the slider.'}], 'type': 'paragraph'}] |
| [{'inlineContent': [{'type': 'text', 'text': 'Steps'}], 'type': 'paragraph'}] | [{'inlineContent': [{'text': 'The number of steps between the minimum and maximum values. The slider uses the number of steps to determine how much to increment or decrement the value when the user interacts with the slider controls.', 'type': 'text'}], 'type': 'paragraph'}] |
| [{'inlineContent': [{'text': 'Continuous', 'type': 'text'}], 'type': 'paragraph'}] | [{'inlineContent': [{'text': 'The display style for the slider. When enabled, the slider value displays its value using a solid bar. When disabled, the slider displays its value using discrete steps.', 'type': 'text'}], 'type': 'paragraph'}] |
| [{'inlineContent': [{'type': 'text', 'text': 'Color'}], 'type': 'paragraph'}] | [{'inlineContent': [{'type': 'text', 'text': 'The color of the slider bar. You can also set the color programmatically using the '}, {'type': 'reference', 'isActive': True, 'identifier': 'doc://com.apple.watchkit/documentation/WatchKit/WKInterfaceSlider/setColor(_:)'}, {'type': 'text', 'text': ' method.'}], 'type': 'paragraph'}] |
| [{'inlineContent': [{'type': 'text', 'text': 'Min Image'}], 'type': 'paragraph'}] | [{'inlineContent': [{'type': 'text', 'text': 'The name of the image to display next to the minimum value of the slider. This image must be bundled in the WatchKit app.'}], 'type': 'paragraph'}] |
| [{'inlineContent': [{'type': 'text', 'text': 'Max Image'}], 'type': 'paragraph'}] | [{'inlineContent': [{'text': 'The name of the image to display next to the maximum value of the slider. This image must be bundled with your WatchKit app.', 'type': 'text'}], 'type': 'paragraph'}] |
| [{'inlineContent': [{'type': 'text', 'text': 'Enabled'}], 'type': 'paragraph'}] | [{'inlineContent': [{'type': 'text', 'text': 'A checkbox indicating whether the slider is enabled and whether it sends events when its value changes.'}], 'type': 'paragraph'}] |

## Topics

### Setting the Slider Value
- [func setValue(Float)](setvalue(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceslider/setvalue(_:)))
  Changes the value of the slider.
- [func setColor(UIColor?)](setcolor(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceslider/setcolor(_:)))
  Sets the color of the slider bar.
- [func setNumberOfSteps(Int)](setnumberofsteps(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceslider/setnumberofsteps(_:)))
  Sets the number of steps for the slider.
### Enabling the Slider
- [func setEnabled(Bool)](setenabled(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceslider/setenabled(_:)))
  Enables or disables the slider.

## Relationships

### Inherits From
- [WKInterfaceObject](wkinterfaceobject.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobject))
### Conforms To
- CVarArg ([Apple Docs](https://developer.apple.com/documentation/Swift/CVarArg))
- CustomDebugStringConvertible ([Apple Docs](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible))
- CustomStringConvertible ([Apple Docs](https://developer.apple.com/documentation/Swift/CustomStringConvertible))
- Equatable ([Apple Docs](https://developer.apple.com/documentation/Swift/Equatable))
- Hashable ([Apple Docs](https://developer.apple.com/documentation/Swift/Hashable))
- NSObjectProtocol ([Apple Docs](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol))

## See Also

- [class WKInterfaceLabel](wkinterfacelabel.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacelabel))
- [class WKInterfaceDate](wkinterfacedate.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacedate))
- [class WKInterfaceTimer](wkinterfacetimer.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacetimer))
- [class WKInterfaceButton](wkinterfacebutton.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacebutton))
- [class WKInterfaceAuthorizationAppleIDButton](wkinterfaceauthorizationappleidbutton.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceauthorizationappleidbutton))
- [class WKInterfacePaymentButton](wkinterfacepaymentbutton.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacepaymentbutton))
- [class WKInterfaceTextField](wkinterfacetextfield.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacetextfield))
- [class WKInterfaceSwitch](wkinterfaceswitch.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceswitch))
- [class WKInterfaceActivityRing](wkinterfaceactivityring.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceactivityring))
- [class WKInterfaceMap](wkinterfacemap.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacemap))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfaceslider)*