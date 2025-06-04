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

## Overview

You create picker items yourself and assign them to a [`WKInterfacePicker`](https://developer.apple.com/documentation/watchkit/wkinterfacepicker) object in your interface. For each item, you can specify a title string, an image, or both based on the style of the picker.

The style of the picker determines how you configure the items of that picker:

- List. Items may be configured in one of two ways:
- Specify an image in the [`contentImage`](https://developer.apple.com/documentation/watchkit/wkpickeritem/contentimage) property.
- Specify text in the [`title`](https://developer.apple.com/documentation/watchkit/wkpickeritem/title) property and an optional image in the [`accessoryImage`](https://developer.apple.com/documentation/watchkit/wkpickeritem/accessoryimage) property.
- Stacked. Configure each item with an image in the [`contentImage`](https://developer.apple.com/documentation/watchkit/wkpickeritem/contentimage) property.
- Image Sequence. Configure each item with an image in the [`contentImage`](https://developer.apple.com/documentation/watchkit/wkpickeritem/contentimage) property.

## Topics

### Setting the Picker Item’s Content
- [var contentImage: WKImage?](contentimage.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkpickeritem/contentimage))
  The image to display for the item.
- [var title: String?](title.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkpickeritem/title))
  The text to display for the item.
- [var accessoryImage: WKImage?](accessoryimage.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkpickeritem/accessoryimage))
  A small image to display next to the title string.
- [var caption: String?](caption.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkpickeritem/caption))
  A caption for the item’s content.

## Relationships

### Inherits From
- NSObject ([Apple Docs](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class))
### Conforms To
- CVarArg ([Apple Docs](https://developer.apple.com/documentation/Swift/CVarArg))
- CustomDebugStringConvertible ([Apple Docs](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible))
- CustomStringConvertible ([Apple Docs](https://developer.apple.com/documentation/Swift/CustomStringConvertible))
- Equatable ([Apple Docs](https://developer.apple.com/documentation/Swift/Equatable))
- Hashable ([Apple Docs](https://developer.apple.com/documentation/Swift/Hashable))
- NSCoding ([Apple Docs](https://developer.apple.com/documentation/Foundation/NSCoding))
- NSObjectProtocol ([Apple Docs](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol))
- NSSecureCoding ([Apple Docs](https://developer.apple.com/documentation/Foundation/NSSecureCoding))

## See Also

- [func setItems([WKPickerItem]?)](setitems(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacepicker/setitems(_:)))
- [func setSelectedItemIndex(Int)](setselecteditemindex(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacepicker/setselecteditemindex(_:)))
- [func setCoordinatedAnimations([any WKInterfaceObject & WKImageAnimatable]?)](setcoordinatedanimations(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacepicker/setcoordinatedanimations(_:)))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkpickeritem)*