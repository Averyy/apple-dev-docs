# WKInterfaceObject

**Framework**: WatchKit  
**Kind**: class

An object that provides information that is common to all interface objects in your watchOS app.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
class WKInterfaceObject
```

## Mentions

- [Connecting Your User Interface to Your Code](connecting-your-user-interface-to-your-code.md)

#### Overview

Your WatchKit extension uses interface objects to manipulate the visual elements displayed on Apple Watch. Specifically, you use the methods of this class to change the size, alignment, and visibility of those elements. You can also configure the accessibility information displayed through assistive technologies like VoiceOver.

Do not subclass or create instances of this class, or any of its subclasses, yourself. Instead, define outlets in your interface controller class and connect them to the corresponding objects in your storyboard file. For example, to refer to a button in your interface, define a property with the following syntax in your interface controller class:

At runtime, WatchKit creates the appropriate interface objects and assigns them to the outlets in your interface controller.

WatchKit provides one-way communication between the interface objects in your extension and the corresponding interface elements in your watchOS app. You can set the values of an interface object, but you cannot get the current values. If you want to know the current value of an attribute, you must save the value yourself.

##### Interface Builder Configuration Options

Xcode lets you configure information about your group interface object in your storyboard file. The following table lists the attributes you can configure in your storyboard and their meaning.

| Attribute | Description |
| --- | --- |
| Alpha | The opacity of the object. A value of `1.0` represents fully opaque and a value of `0.0` represents fully transparent. |
| Hidden | A checkbox indicating whether the item is hidden initially. You can change the visibility of the item programmatically by calling the [`setHidden(_:)`](wkinterfaceobject/sethidden(_:).md) method. |
| Installed | A checkbox indicating whether the item is installed for the current device. |
| Horizontal | The horizontal alignment of the item. Use this attribute to configure the horizontal position of the item relative to its immediate parent. |
| Vertical | The vertical alignment of the item. Use this attribute to configure the vertical position of the item relative to its immediate parent. |
| Width | The width of the object. Specify a fixed width or set the value of the object to be a percentage of its container’s width. |
| Height | The height of the object. Specify a fixed height or set the value of the object to be a percentage of its container’s height. |

## Topics

### Hiding and Showing an Object
- [func setHidden(Bool)](wkinterfaceobject/sethidden(_:).md)
  Hides or shows the interface object in your user interface.
- [func setAlpha(CGFloat)](wkinterfaceobject/setalpha(_:).md)
  Sets the opacity of the interface object.
### Getting the Property Name
- [var interfaceProperty: String](wkinterfaceobject/interfaceproperty.md)
  The name of the outlet in your interface controller to which the object is bound.
### Changing an Object’s Size
- [func setWidth(CGFloat)](wkinterfaceobject/setwidth(_:).md)
  Sets the absolute width (in points) of the object.
- [func setHeight(CGFloat)](wkinterfaceobject/setheight(_:).md)
  Sets the absolute height (in points) of the object.
- [func setRelativeWidth(CGFloat, withAdjustment: CGFloat)](wkinterfaceobject/setrelativewidth(_:withadjustment:).md)
  Sets the width of the object relative to its container.
- [func setRelativeHeight(CGFloat, withAdjustment: CGFloat)](wkinterfaceobject/setrelativeheight(_:withadjustment:).md)
  Sets the height of the object relative to its container.
- [func sizeToFitWidth()](wkinterfaceobject/sizetofitwidth.md)
  Sets the width of the object to fit its current content.
- [func sizeToFitHeight()](wkinterfaceobject/sizetofitheight.md)
  Sets the height of the object so that it fills the available vertical space.
### Setting an Object’s Alignment
- [func setHorizontalAlignment(WKInterfaceObjectHorizontalAlignment)](wkinterfaceobject/sethorizontalalignment(_:).md)
  Sets the horizontal alignment of an object relative to its container’s bounds.
- [func setVerticalAlignment(WKInterfaceObjectVerticalAlignment)](wkinterfaceobject/setverticalalignment(_:).md)
  Sets the vertical alignment of an object relative to its container’s bounds.
### Configuring the Accessibility Attributes
- [func setAccessibilityIdentifier(String?)](wkinterfaceobject/setaccessibilityidentifier(_:).md)
  Sets the unique identifier string for the interface object.
- [func setAccessibilityLabel(String?)](wkinterfaceobject/setaccessibilitylabel(_:).md)
  Sets a succinct label on the object that identifies the accessibility element.
- [func setAccessibilityHint(String?)](wkinterfaceobject/setaccessibilityhint(_:).md)
  Sets the description of what happens when performing an action on the accessibility element.
- [func setAccessibilityValue(String?)](wkinterfaceobject/setaccessibilityvalue(_:).md)
  Sets the value of the accessibility element.
- [func setIsAccessibilityElement(Bool)](wkinterfaceobject/setisaccessibilityelement(_:).md)
  Sets whether the object is an accessibility element that an assistive app can access.
- [func setAccessibilityTraits(UIAccessibilityTraits)](wkinterfaceobject/setaccessibilitytraits(_:).md)
  Sets the combination of accessibility traits that best characterize the accessibility element.
- [func setAccessibilityImageRegions([WKAccessibilityImageRegion])](wkinterfaceobject/setaccessibilityimageregions(_:).md)
  Marks portions of an image as separate accessible elements.
### Setting the Layout Direction
- [func setSemanticContentAttribute(WKInterfaceSemanticContentAttribute)](wkinterfaceobject/setsemanticcontentattribute(_:).md)
  Sets the semantic description of the object’s contents, used to determine whether its content should be flipped when switching between left-to-right and right-to-left layouts.
### Constants
- [enum WKInterfaceObjectHorizontalAlignment](wkinterfaceobjecthorizontalalignment.md)
  Constants for horizontally aligning objects in their container.
- [enum WKInterfaceObjectVerticalAlignment](wkinterfaceobjectverticalalignment.md)
  Constants for vertically aligning objects in their container.

## Relationships

### Inherits From
- [NSObject](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class)
### Inherited By
- [WKInterfaceActivityRing](wkinterfaceactivityring.md)
- [WKInterfaceAuthorizationAppleIDButton](wkinterfaceauthorizationappleidbutton.md)
- [WKInterfaceButton](wkinterfacebutton.md)
- [WKInterfaceDate](wkinterfacedate.md)
- [WKInterfaceGroup](wkinterfacegroup.md)
- [WKInterfaceHMCamera](wkinterfacehmcamera.md)
- [WKInterfaceImage](wkinterfaceimage.md)
- [WKInterfaceInlineMovie](wkinterfaceinlinemovie.md)
- [WKInterfaceLabel](wkinterfacelabel.md)
- [WKInterfaceMap](wkinterfacemap.md)
- [WKInterfaceMovie](wkinterfacemovie.md)
- [WKInterfacePaymentButton](wkinterfacepaymentbutton.md)
- [WKInterfacePicker](wkinterfacepicker.md)
- [WKInterfaceSCNScene](wkinterfacescnscene.md)
- [WKInterfaceSKScene](wkinterfaceskscene.md)
- [WKInterfaceSeparator](wkinterfaceseparator.md)
- [WKInterfaceSlider](wkinterfaceslider.md)
- [WKInterfaceSwitch](wkinterfaceswitch.md)
- [WKInterfaceTable](wkinterfacetable.md)
- [WKInterfaceTextField](wkinterfacetextfield.md)
- [WKInterfaceTimer](wkinterfacetimer.md)
- [WKInterfaceVolumeControl](wkinterfacevolumecontrol.md)
### Conforms To
- [CVarArg](https://developer.apple.com/documentation/Swift/CVarArg)
- [CustomDebugStringConvertible](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible)
- [CustomStringConvertible](https://developer.apple.com/documentation/Swift/CustomStringConvertible)
- [Equatable](https://developer.apple.com/documentation/Swift/Equatable)
- [Hashable](https://developer.apple.com/documentation/Swift/Hashable)
- [NSObjectProtocol](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol)

## See Also

- [Building watchOS app Interfaces Using the Storyboard](building-watchos-app-interfaces-using-the-storyboard.md)
  Create the user interface for your watchOS app by nesting stacks.
- [class WKInterfaceController](wkinterfacecontroller.md)
  A class that provides the infrastructure for managing the interface in a watchOS app.
- [class WKAlertAction](wkalertaction.md)
  An object that encapsulates information about a button displayed in an alert or action sheet.
- [class WKAccessibilityImageRegion](wkaccessibilityimageregion.md)
  An object that defines a portion of an image that you want to call out separately to an assistive app.
- [func WKAccessibilityIsVoiceOverRunning() -> Bool](wkaccessibilityisvoiceoverrunning().md)
  Returns a Boolean value indicating whether VoiceOver is running.
- [func WKAccessibilityIsReduceMotionEnabled() -> Bool](wkaccessibilityisreducemotionenabled().md)
  Returns a Boolean value indicating whether reduced motion is enabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfaceobject)*