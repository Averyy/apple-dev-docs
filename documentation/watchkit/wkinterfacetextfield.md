# WKInterfaceTextField

**Framework**: Watchkit  
**Kind**: class

An interface element that displays an editable text area.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
class WKInterfaceTextField
```

#### Overview

Text fields gather text-based input from the user. The text field defines an area of editable text within your user interface, letting you create forms with multiple input fields.

![A screenshot of a sample sign in screen.](https://docs-assets.developer.apple.com/published/684cea39263d88ab95e57029984c52c7/media-3222854%402x.png)

When the user taps the text field, WatchKit displays the text input controller. Users can enter text by selecting one of the suggestions, or using dictation or Scribble. Users can also launch the Apple Continuity Keyboard, entering text from a nearby iOS device logged into the same iCloud account.

Use text fields to gather short, specific pieces of information such as the user’s name, address, password, or credit card number. Identify the type of data using the text field’s content type, which allows the system to optimize the behavior of the text input controller and the Apple Continuity Keyboard. For more information, see `Authenticating Users on Apple Watch`.

You can also describe the expected content to the user in the text field’s placeholder. Effective placeholders let you build a form that is both compact and easy to use.

For general text input, consider using [`presentTextInputController(withSuggestions:allowedInputMode:completion:)`](wkinterfacecontroller/presenttextinputcontroller(withsuggestions:allowedinputmode:completion:).md) or [`presentTextInputControllerWithSuggestions(forLanguage:allowedInputMode:completion:)`](wkinterfacecontroller/presenttextinputcontrollerwithsuggestions(forlanguage:allowedinputmode:completion:).md) instead. Call these methods to display the text input controller with the suggestions that you provide. Keep in mind that the system doesn’t provide the text input controller with a content type, so the system cannot optimize its behavior.

##### Configure the Text Field

As with other WatchKit interface objects, you should not subclass or create instances of this class. Instead, add a text field to your WatchKit App’s storyboard. The system then creates the text field when it loads the storyboard.

Xcode also lets you configure the text field directly in the storyboard. The following table lists the attributes and their meaning.

| Attribute | Description |
| --- | --- |
| Text | The initial text displayed by the text field. Specify a plain string or an attributed string. You can set this value programmatically using the [`setText(_:)`](wkinterfacetextfield/settext(_:).md) or [`setAttributedText(_:)`](wkinterfacetextfield/setattributedtext(_:).md) methods. |
| Placeholder | The placeholder text displayed by the text field. When the text field’s value is empty, the text field displays the placeholder, formatting it to make it clear that it’s not an actual text entry. Typing any text into the text field hides this string. You can set this value programmatically using the [`setPlaceholder(_:)`](wkinterfacetextfield/setplaceholder(_:).md) or [`setAttributedPlaceholder(_:)`](wkinterfacetextfield/setattributedplaceholder(_:).md) methods. |
| Text Color | The color of the text. The system applies this color to the entire string. You can set this value programmatically using the [`setTextColor(_:)`](wkinterfacetextfield/settextcolor(_:).md) method. |
| Content Type | The text field’s expected content, such as a username, password, or address. You can set this value programmatically using the [`setTextContentType(_:)`](wkinterfacetextfield/settextcontenttype(_:).md) method. |
| Secure Text Entry | A checkbox indicating whether the text field hides the text that the user entered, keeping passwords and other secure data private. You can set this value programmatically using the [`setSecureTextEntry(_:)`](wkinterfacetextfield/setsecuretextentry(_:).md) method. |
| Enabled | A checkbox indicating whether the text field  is enabled and responds when tapped. You can configure this value programmatically using the [`setEnabled(_:)`](wkinterfacetextfield/setenabled(_:).md) method. |

To dynamically modify a text field at runtime, define an outlet in your interface controller and connect it to the corresponding text field in your storyboard. For example, define a property with the following syntax in your interface controller class:

During your interface controller’s initialization, WatchKit creates a new instance of the [`WKInterfaceTextField`](wkinterfacetextfield.md) class and assigns it to your outlet. At that point, you can use the object in your outlet to manage the text field.

##### Receive Text Input

To receive the text entered by the user, connect the text field in the storyboard to an action method defined in your interface controller.

WatchKit calls the action method after the user dismisses the text input controller. The `value` parameter contains the string entered by the user. If the user cancels the text input controller, the value is `nil`.

## Topics

### Specifying the Content Type
- [func setTextContentType(WKTextContentType?)](wkinterfacetextfield/settextcontenttype(_:).md)
  Sets the text field’s semantic meaning.
- [struct WKTextContentType](wktextcontenttype.md)
  Constants that specify a text field’s semantic meaning.
### Setting the Text
- [func setText(String?)](wkinterfacetextfield/settext(_:).md)
  Sets the text displayed by the text field.
- [func setAttributedText(NSAttributedString?)](wkinterfacetextfield/setattributedtext(_:).md)
  Sets the styled text displayed by the text field.
- [func setTextColor(UIColor?)](wkinterfacetextfield/settextcolor(_:).md)
  Sets the text’s color.
### Setting a Placeholder
- [func setPlaceholder(String?)](wkinterfacetextfield/setplaceholder(_:).md)
  Sets the text field’s placeholder.
- [func setAttributedPlaceholder(NSAttributedString?)](wkinterfacetextfield/setattributedplaceholder(_:).md)
  Sets the text field’s placeholder using styled text.
### Configuring the Control
- [func setEnabled(Bool)](wkinterfacetextfield/setenabled(_:).md)
  Enables or disables the text field.
- [func setSecureTextEntry(Bool)](wkinterfacetextfield/setsecuretextentry(_:).md)
  Determines whether the text field hides the text entered by the user.

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

- [func presentTextInputController(withSuggestions: [String]?, allowedInputMode: WKTextInputMode, completion: ([Any]?) -> Void)](wkinterfacecontroller/presenttextinputcontroller(withsuggestions:allowedinputmode:completion:).md)
  Displays a modal interface for gathering text input from the user.
- [func presentTextInputControllerWithSuggestions(forLanguage: ((String) -> [Any]?)?, allowedInputMode: WKTextInputMode, completion: ([Any]?) -> Void)](wkinterfacecontroller/presenttextinputcontrollerwithsuggestions(forlanguage:allowedinputmode:completion:).md)
  Displays a modal interface for gathering language-specific text input from the user.
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
- [class WKInterfaceSwitch](wkinterfaceswitch.md)
  An interface element that toggles between an On and Off state.
- [class WKInterfaceSlider](wkinterfaceslider.md)
  An interface element that lets users select a single floating-point value from a range of values.
- [class WKInterfaceActivityRing](wkinterfaceactivityring.md)
  A view that displays data from a HealthKit activity summary object.
- [class WKInterfaceMap](wkinterfacemap.md)
  An interface element that displays a noninteractive map for the location you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacetextfield)*