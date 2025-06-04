# WKInterfaceObject

**Framework**: Watchkit  
**Kind**: class

An object that provides information that is common to all interface objects in your watchOS app.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
class WKInterfaceObject
```

## Mentions

- [Connecting Your User Interface to Your Code](connecting-your-user-interface-to-your-code.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/connecting-your-user-interface-to-your-code))

## Overview

Your WatchKit extension uses interface objects to manipulate the visual elements displayed on Apple Watch. Specifically, you use the methods of this class to change the size, alignment, and visibility of those elements. You can also configure the accessibility information displayed through assistive technologies like VoiceOver.

Do not subclass or create instances of this class, or any of its subclasses, yourself. Instead, define outlets in your interface controller class and connect them to the corresponding objects in your storyboard file. For example, to refer to a button in your interface, define a property with the following syntax in your interface controller class:

At runtime, WatchKit creates the appropriate interface objects and assigns them to the outlets in your interface controller.

WatchKit provides one-way communication between the interface objects in your extension and the corresponding interface elements in your watchOS app. You can set the values of an interface object, but you cannot get the current values. If you want to know the current value of an attribute, you must save the value yourself.

Xcode lets you configure information about your group interface object in your storyboard file. The following table lists the attributes you can configure in your storyboard and their meaning.

| r | o | w |
| --- | --- | --- |
| [{'inlineContent': [{'type': 'text', 'text': 'Attribute'}], 'type': 'paragraph'}] | [{'inlineContent': [{'type': 'text', 'text': 'Description'}], 'type': 'paragraph'}] |
| [{'inlineContent': [{'text': 'Alpha', 'type': 'text'}], 'type': 'paragraph'}] | [{'inlineContent': [{'text': 'The opacity of the object. A value of ', 'type': 'text'}, {'code': '1.0', 'type': 'codeVoice'}, {'text': ' represents fully opaque and a value of ', 'type': 'text'}, {'code': '0.0', 'type': 'codeVoice'}, {'text': ' represents fully transparent.', 'type': 'text'}], 'type': 'paragraph'}] |
| [{'inlineContent': [{'text': 'Hidden', 'type': 'text'}], 'type': 'paragraph'}] | [{'inlineContent': [{'type': 'text', 'text': 'A checkbox indicating whether the item is hidden initially. You can change the visibility of the item programmatically by calling the '}, {'isActive': True, 'type': 'reference', 'identifier': 'doc://com.apple.watchkit/documentation/WatchKit/WKInterfaceObject/setHidden(_:)'}, {'type': 'text', 'text': ' method.'}], 'type': 'paragraph'}] |
| [{'inlineContent': [{'type': 'text', 'text': 'Installed'}], 'type': 'paragraph'}] | [{'inlineContent': [{'text': 'A checkbox indicating whether the item is installed for the current device.', 'type': 'text'}], 'type': 'paragraph'}] |
| [{'inlineContent': [{'type': 'text', 'text': 'Horizontal'}], 'type': 'paragraph'}] | [{'inlineContent': [{'text': 'The horizontal alignment of the item. Use this attribute to configure the horizontal position of the item relative to its immediate parent.', 'type': 'text'}], 'type': 'paragraph'}] |
| [{'inlineContent': [{'text': 'Vertical', 'type': 'text'}], 'type': 'paragraph'}] | [{'inlineContent': [{'type': 'text', 'text': 'The vertical alignment of the item. Use this attribute to configure the vertical position of the item relative to its immediate parent.'}], 'type': 'paragraph'}] |
| [{'inlineContent': [{'text': 'Width', 'type': 'text'}], 'type': 'paragraph'}] | [{'inlineContent': [{'text': 'The width of the object. Specify a fixed width or set the value of the object to be a percentage of its container’s width.', 'type': 'text'}], 'type': 'paragraph'}] |
| [{'inlineContent': [{'type': 'text', 'text': 'Height'}], 'type': 'paragraph'}] | [{'inlineContent': [{'text': 'The height of the object. Specify a fixed height or set the value of the object to be a percentage of its container’s height.', 'type': 'text'}], 'type': 'paragraph'}] |

## Topics

### Hiding and Showing an Object
- [func setHidden(Bool)](sethidden(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/sethidden(_:)))
  Hides or shows the interface object in your user interface.
- [func setAlpha(CGFloat)](setalpha(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/setalpha(_:)))
  Sets the opacity of the interface object.
### Getting the Property Name
- [var interfaceProperty: String](interfaceproperty.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/interfaceproperty))
  The name of the outlet in your interface controller to which the object is bound.
### Changing an Object’s Size
- [func setWidth(CGFloat)](setwidth(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/setwidth(_:)))
  Sets the absolute width (in points) of the object.
- [func setHeight(CGFloat)](setheight(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/setheight(_:)))
  Sets the absolute height (in points) of the object.
- [func setRelativeWidth(CGFloat, withAdjustment: CGFloat)](setrelativewidth(_:withadjustment:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/setrelativewidth(_:withadjustment:)))
  Sets the width of the object relative to its container.
- [func setRelativeHeight(CGFloat, withAdjustment: CGFloat)](setrelativeheight(_:withadjustment:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/setrelativeheight(_:withadjustment:)))
  Sets the height of the object relative to its container.
- [func sizeToFitWidth()](sizetofitwidth().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/sizetofitwidth()))
  Sets the width of the object to fit its current content.
- [func sizeToFitHeight()](sizetofitheight().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/sizetofitheight()))
  Sets the height of the object so that it fills the available vertical space.
### Setting an Object’s Alignment
- [func setHorizontalAlignment(WKInterfaceObjectHorizontalAlignment)](sethorizontalalignment(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/sethorizontalalignment(_:)))
  Sets the horizontal alignment of an object relative to its container’s bounds.
- [func setVerticalAlignment(WKInterfaceObjectVerticalAlignment)](setverticalalignment(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/setverticalalignment(_:)))
  Sets the vertical alignment of an object relative to its container’s bounds.
### Configuring the Accessibility Attributes
- [func setAccessibilityIdentifier(String?)](setaccessibilityidentifier(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/setaccessibilityidentifier(_:)))
  Sets the unique identifier string for the interface object.
- [func setAccessibilityLabel(String?)](setaccessibilitylabel(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/setaccessibilitylabel(_:)))
  Sets a succinct label on the object that identifies the accessibility element.
- [func setAccessibilityHint(String?)](setaccessibilityhint(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/setaccessibilityhint(_:)))
  Sets the description of what happens when performing an action on the accessibility element.
- [func setAccessibilityValue(String?)](setaccessibilityvalue(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/setaccessibilityvalue(_:)))
  Sets the value of the accessibility element.
- [func setIsAccessibilityElement(Bool)](setisaccessibilityelement(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/setisaccessibilityelement(_:)))
  Sets whether the object is an accessibility element that an assistive app can access.
- [func setAccessibilityTraits(UIAccessibilityTraits)](setaccessibilitytraits(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/setaccessibilitytraits(_:)))
  Sets the combination of accessibility traits that best characterize the accessibility element.
- [func setAccessibilityImageRegions([WKAccessibilityImageRegion])](setaccessibilityimageregions(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/setaccessibilityimageregions(_:)))
  Marks portions of an image as separate accessible elements.
### Setting the Layout Direction
- [func setSemanticContentAttribute(WKInterfaceSemanticContentAttribute)](setsemanticcontentattribute(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/setsemanticcontentattribute(_:)))
  Sets the semantic description of the object’s contents, used to determine whether its content should be flipped when switching between left-to-right and right-to-left layouts.
### Constants
- [enum WKInterfaceObjectHorizontalAlignment](wkinterfaceobjecthorizontalalignment.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobjecthorizontalalignment))
  Constants for horizontally aligning objects in their container.
- [enum WKInterfaceObjectVerticalAlignment](wkinterfaceobjectverticalalignment.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobjectverticalalignment))
  Constants for vertically aligning objects in their container.

## Relationships

### Inherits From
- NSObject ([Apple Docs](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class))
### Inherited By
- [WKInterfaceActivityRing](wkinterfaceactivityring.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceactivityring))
- [WKInterfaceAuthorizationAppleIDButton](wkinterfaceauthorizationappleidbutton.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceauthorizationappleidbutton))
- [WKInterfaceButton](wkinterfacebutton.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacebutton))
- [WKInterfaceDate](wkinterfacedate.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacedate))
- [WKInterfaceGroup](wkinterfacegroup.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacegroup))
- [WKInterfaceHMCamera](wkinterfacehmcamera.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacehmcamera))
- [WKInterfaceImage](wkinterfaceimage.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceimage))
- [WKInterfaceInlineMovie](wkinterfaceinlinemovie.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceinlinemovie))
- [WKInterfaceLabel](wkinterfacelabel.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacelabel))
- [WKInterfaceMap](wkinterfacemap.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacemap))
- [WKInterfaceMovie](wkinterfacemovie.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacemovie))
- [WKInterfacePaymentButton](wkinterfacepaymentbutton.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacepaymentbutton))
- [WKInterfacePicker](wkinterfacepicker.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacepicker))
- [WKInterfaceSCNScene](wkinterfacescnscene.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacescnscene))
- [WKInterfaceSKScene](wkinterfaceskscene.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceskscene))
- [WKInterfaceSeparator](wkinterfaceseparator.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceseparator))
- [WKInterfaceSlider](wkinterfaceslider.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceslider))
- [WKInterfaceSwitch](wkinterfaceswitch.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceswitch))
- [WKInterfaceTable](wkinterfacetable.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacetable))
- [WKInterfaceTextField](wkinterfacetextfield.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacetextfield))
- [WKInterfaceTimer](wkinterfacetimer.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacetimer))
- [WKInterfaceVolumeControl](wkinterfacevolumecontrol.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacevolumecontrol))
### Conforms To
- CVarArg ([Apple Docs](https://developer.apple.com/documentation/Swift/CVarArg))
- CustomDebugStringConvertible ([Apple Docs](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible))
- CustomStringConvertible ([Apple Docs](https://developer.apple.com/documentation/Swift/CustomStringConvertible))
- Equatable ([Apple Docs](https://developer.apple.com/documentation/Swift/Equatable))
- Hashable ([Apple Docs](https://developer.apple.com/documentation/Swift/Hashable))
- NSObjectProtocol ([Apple Docs](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol))

## See Also

- [Building watchOS app Interfaces Using the Storyboard](building-watchos-app-interfaces-using-the-storyboard.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/building-watchos-app-interfaces-using-the-storyboard))
- [class WKInterfaceController](wkinterfacecontroller.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller))
- [class WKAlertAction](wkalertaction.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkalertaction))
- [class WKAccessibilityImageRegion](wkaccessibilityimageregion.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaccessibilityimageregion))
- [func WKAccessibilityIsVoiceOverRunning() -> Bool](wkaccessibilityisvoiceoverrunning().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaccessibilityisvoiceoverrunning()))
- [func WKAccessibilityIsReduceMotionEnabled() -> Bool](wkaccessibilityisreducemotionenabled().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaccessibilityisreducemotionenabled()))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfaceobject)*