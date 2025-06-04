# WKInterfaceGroup

**Framework**: Watchkit  
**Kind**: class

A container for one or more interface objects.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
class WKInterfaceGroup
```

## Overview

A [`WKInterfaceGroup`](https://developer.apple.com/documentation/watchkit/wkinterfacegroup) is conceptually similar to a superview in UIKit, in that it handles layout for its contained items. A group arranges items vertically or horizontally within its available space. Groups also have attributes that you can use to configure the precise placement of items within the group. You can also nest groups inside of other groups to manage more complex layouts.

Do not subclass or create instances of this class yourself. Instead, define outlets in your interface controller class and connect them to the corresponding objects in your storyboard file. For example, to refer to a group object in your interface, define a property with the following syntax in your interface controller class:

During the initialization of your interface controller, WatchKit creates a new instance of this class and assigns it to your outlet. At that point, you can use the object in your outlet to make changes to the group’s configuration.

Xcode lets you configure information about your group interface object in your storyboard file. The following table lists the attributes you can configure in your storyboard and their meaning.

| r | o | w |
| --- | --- | --- |
| [{'type': 'paragraph', 'inlineContent': [{'type': 'text', 'text': 'Attribute'}]}] | [{'type': 'paragraph', 'inlineContent': [{'type': 'text', 'text': 'Description'}]}] |
| [{'type': 'paragraph', 'inlineContent': [{'text': 'Layout', 'type': 'text'}]}] | [{'type': 'paragraph', 'inlineContent': [{'text': 'The layout direction for items in the group. You can stack items horizontally or vertically, or have them overlap', 'type': 'text'}]}] |
| [{'type': 'paragraph', 'inlineContent': [{'type': 'text', 'text': 'Insets'}]}] | [{'type': 'paragraph', 'inlineContent': [{'text': 'The amount of space (in points) to insert between the edges of the group and its child elements. Selecting Custom lets you specify different values for the top, bottom, left, and right edges.', 'type': 'text'}]}] |
| [{'type': 'paragraph', 'inlineContent': [{'text': 'Spacing', 'type': 'text'}]}] | [{'type': 'paragraph', 'inlineContent': [{'type': 'text', 'text': 'Additional spacing (in points) to include between child elements in the group. The default spacing is 2 points.'}]}] |
| [{'type': 'paragraph', 'inlineContent': [{'type': 'text', 'text': 'Background'}]}] | [{'type': 'paragraph', 'inlineContent': [{'type': 'text', 'text': 'The background image to display behind the group’s items. You can also set this value programmatically using the '}, {'type': 'reference', 'isActive': True, 'identifier': 'doc://com.apple.watchkit/documentation/WatchKit/WKInterfaceGroup/setBackgroundImage(_:)'}, {'type': 'text', 'text': ', '}, {'type': 'reference', 'isActive': True, 'identifier': 'doc://com.apple.watchkit/documentation/WatchKit/WKInterfaceGroup/setBackgroundImageData(_:)'}, {'type': 'text', 'text': ', or '}, {'type': 'reference', 'isActive': True, 'identifier': 'doc://com.apple.watchkit/documentation/WatchKit/WKInterfaceGroup/setBackgroundImageNamed(_:)'}, {'type': 'text', 'text': ' methods.'}]}] |
| [{'type': 'paragraph', 'inlineContent': [{'text': 'Mode', 'type': 'text'}]}] | [{'type': 'paragraph', 'inlineContent': [{'type': 'text', 'text': 'The content mode for the group’s background image. Use this option to specify whether the image is scaled or pinned to a particular edge of the group.'}]}] |
| [{'type': 'paragraph', 'inlineContent': [{'text': 'Animate', 'type': 'text'}]}] | [{'type': 'paragraph', 'inlineContent': [{'type': 'text', 'text': 'A Boolean value indicating whether the background image is animatable. Set the value to Yes to configure the animation parameters, including its duration (in seconds) and whether it starts immediately when the parent interface controller appears onscreen. Animations started at load time run continuously in a loop.'}]}] |
| [{'type': 'paragraph', 'inlineContent': [{'text': 'Color', 'type': 'text'}]}] | [{'type': 'paragraph', 'inlineContent': [{'text': 'The background color for the group.You can also set this value programmatically using the ', 'type': 'text'}, {'isActive': True, 'identifier': 'doc://com.apple.watchkit/documentation/WatchKit/WKInterfaceGroup/setBackgroundColor(_:)', 'type': 'reference'}, {'text': ' method.', 'type': 'text'}]}] |
| [{'type': 'paragraph', 'inlineContent': [{'text': 'Radius', 'type': 'text'}]}] | [{'type': 'paragraph', 'inlineContent': [{'type': 'text', 'text': 'The corner radius to apply to the group’s rectangle. Content inside the group is clipped to the corner radius. If you do not specify a custom value, WatchKit applies a 6-point radius by default.'}]}] |

In watchOS 4 and later, you can use groups to create overlapping content. Set the group’s Layout attribute in the Attribute inspector to Overlap (see [`Figure 1`](https://developer.apple.com/documentation/watchkit/wkinterfacegroup#2929967) ). The system positions each item in the group based on the item’s alignment attributes.

## Topics

### Setting the Group’s Content
- [func setBackgroundColor(UIColor?)](setbackgroundcolor(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacegroup/setbackgroundcolor(_:)))
  Changes the background color for the group container.
- [func setBackgroundImage(UIImage?)](setbackgroundimage(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacegroup/setbackgroundimage(_:)))
  Changes the background image of the group container to the specified image.
- [func setBackgroundImageData(Data?)](setbackgroundimagedata(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacegroup/setbackgroundimagedata(_:)))
  Changes the background image of the group container to the image in the specified data object.
- [func setBackgroundImageNamed(String?)](setbackgroundimagenamed(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacegroup/setbackgroundimagenamed(_:)))
  Changes the background image of the group container to the image in the specified resource file.
### Setting the Layout Information
- [func setCornerRadius(CGFloat)](setcornerradius(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacegroup/setcornerradius(_:)))
  Changes the radius to use when drawing rounded corners for the group.
- [func setContentInset(UIEdgeInsets)](setcontentinset(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacegroup/setcontentinset(_:)))
  Sets the distance between the edges of the group and any contained objects.

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
- [WKImageAnimatable](wkimageanimatable.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkimageanimatable))

## See Also

- [class WKInterfaceSeparator](wkinterfaceseparator.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceseparator))
- [class WKInterfaceTable](wkinterfacetable.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacetable))
- [class WKInterfacePicker](wkinterfacepicker.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacepicker))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacegroup)*