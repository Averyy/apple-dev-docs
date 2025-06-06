# WKPickerItem

**Framework**: Watchkit  
**Kind**: class

A single item in a picker interface.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
class WKPickerItem
```

#### Overview

You create picker items yourself and assign them to a [`WKInterfacePicker`](wkinterfacepicker.md) object in your interface. For each item, you can specify a title string, an image, or both based on the style of the picker.

The style of the picker determines how you configure the items of that picker:

- List. Items may be configured in one of two ways:
- Specify an image in the [`contentImage`](wkpickeritem/contentimage.md) property.
- Specify text in the [`title`](wkpickeritem/title.md) property and an optional image in the [`accessoryImage`](wkpickeritem/accessoryimage.md) property.
- Stacked. Configure each item with an image in the [`contentImage`](wkpickeritem/contentimage.md) property.
- Image Sequence. Configure each item with an image in the [`contentImage`](wkpickeritem/contentimage.md) property.

## Topics

### Setting the Picker Item’s Content
- [var contentImage: WKImage?](wkpickeritem/contentimage.md)
  The image to display for the item.
- [var title: String?](wkpickeritem/title.md)
  The text to display for the item.
- [var accessoryImage: WKImage?](wkpickeritem/accessoryimage.md)
  A small image to display next to the title string.
- [var caption: String?](wkpickeritem/caption.md)
  A caption for the item’s content.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [func setItems([WKPickerItem]?)](wkinterfacepicker/setitems(_:).md)
  Sets the list of items displayed by the picker.
- [func setSelectedItemIndex(Int)](wkinterfacepicker/setselecteditemindex(_:).md)
  Selects the specified item in the list.
- [func setCoordinatedAnimations([any WKInterfaceObject & WKImageAnimatable]?)](wkinterfacepicker/setcoordinatedanimations(_:).md)
  Sets the interface objects that should coordinate their own animations with the picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkpickeritem)*