# WKInterfacePicker

**Framework**: WatchKit  
**Kind**: class

An interface element that presents a scrolling list of items for the user to choose from.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
class WKInterfacePicker
```

#### Overview

The picker presents one or more [`WKPickerItem`](wkpickeritem.md) objects to the user. These Items may consist of text, images, or a combination of the two. The user interacts with a picker by tapping it, using the crown to scroll through items, and tapping again to select an item. A single interface controller may contain multiple pickers, each with its own set of items.

Pickers can be configured to display items using one of several styles:

- List. Displays a vertically stacked list of items. Each item contains a title and an optional accessory image. If you supply a content image, that image is displayed behind the title and accessory image. Multiple items may be onscreen at once and turning the crown navigates vertically through the list of items.
- Stacked. Displays items as a stack of cards that animate in from the bottom of the picker. Each item in the list displays an image. Turning the crown animates the new card onscreen while animating the old card offscreen.
- Image Sequence. Displays a single image from a sequence of images. Each item in the list represents the previous or next item in the sequence. Turning the crown displays the previous or next image in the sequence without animations.

When the user selects a new value, WatchKit calls the picker’s action method to report that new value. The format of the picker’s action method is as follows:

Declare a method of this form in the interface controller class used to receive the picker’s new value. You can change the method name to anything you like. When configuring the picker in Xcode, connect its selector to your custom action method. The parameter represents the index of the item in the array of items you specified when calling the [`setItems(_:)`](wkinterfacepicker/setitems(_:).md) method.

Do not subclass or create instances of this class yourself. Instead, define outlets in your interface controller class and connect them to the corresponding objects in your storyboard file. For example, to refer to a picker object in your interface, define a property with the following syntax in your interface controller class:

During the initialization of your interface controller, WatchKit creates a new instance of this class and assigns it to your outlet. At that point, you can use the object in your outlet to make changes to the onscreen picker.

##### Interface Builder Configuration Options

Xcode lets you configure information about your picker interface object in your storyboard file. The following table lists the attributes you can configure and their meaning.

| Attribute | Description |
| --- | --- |
| Style | The visual style of the picker. The style determines the type of information displayed by the picker. For example, a picker configured with the List style displays a string and an optional accessory image for each item. Other styles display only the content image of each picker item. |
| Focus | The highlight style when the picker has the focus. The focus style lets the user know when a picker is selected and receiving input from the Digital Crown. If you specify a focus style that includes a caption, the picker displays the caption string for the current item in addition to that item’s text. |
| Indicator | A value indicating whether the picker uses an indicator to convey context about the number of picker items and which item is selected. |
| Enabled | A checkbox indicating whether the picker is enabled and sends events when tapped. You can also configure this value programmatically using the [`setEnabled(_:)`](wkinterfacepicker/setenabled(_:).md) method. |

## Topics

### Managing the Picker Contents
- [func setItems([WKPickerItem]?)](wkinterfacepicker/setitems(_:).md)
  Sets the list of items displayed by the picker.
- [class WKPickerItem](wkpickeritem.md)
  A single item in a picker interface.
- [func setSelectedItemIndex(Int)](wkinterfacepicker/setselecteditemindex(_:).md)
  Selects the specified item in the list.
- [func setCoordinatedAnimations([any WKInterfaceObject & WKImageAnimatable]?)](wkinterfacepicker/setcoordinatedanimations(_:).md)
  Sets the interface objects that should coordinate their own animations with the picker.
### Managing Input from the Digital Crown
- [func focus()](wkinterfacepicker/focus.md)
  Configures the picker to receive input from the Digital Crown.
- [func resignFocus()](wkinterfacepicker/resignfocus.md)
  Removes focus from the picker, causing it to stop receiving input from the Digital Crown.
### Enabling and Disabling the Picker
- [func setEnabled(Bool)](wkinterfacepicker/setenabled(_:).md)
  Enables or disables the picker.

## Relationships

### Inherits From
- [WKInterfaceObject](wkinterfaceobject.md)
### Conforms To
- [CVarArg](https://developer.apple.com/documentation/Swift/CVarArg)
- [CustomDebugStringConvertible](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible)
- [CustomStringConvertible](https://developer.apple.com/documentation/Swift/CustomStringConvertible)
- [Equatable](https://developer.apple.com/documentation/Swift/Equatable)
- [Hashable](https://developer.apple.com/documentation/Swift/Hashable)
- [NSObjectProtocol](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol)

## See Also

- [class WKInterfaceGroup](wkinterfacegroup.md)
  A container for one or more interface objects.
- [class WKInterfaceSeparator](wkinterfaceseparator.md)
  An interface object that displays a visual separator within a group.
- [class WKInterfaceTable](wkinterfacetable.md)
  An object that creates and manages the contents of a single-column table interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacepicker)*