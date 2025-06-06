# WebDragSourceAction

**Framework**: Webkit  
**Kind**: struct

Actions that the source object of a drag operation can perform.

**Availability**:
- macOS 10.3+

## Declaration

```swift
struct WebDragSourceAction
```

## Topics

### Constants
- [static var DHTML: WebDragSourceAction](webdragsourceaction/dhtml.md)
  Allows DHTML (such as JavaScript) in the source object to initiate a drag operation.
- [static var image: WebDragSourceAction](webdragsourceaction/image.md)
  Allows the user to drag an image in the source object.
- [static var link: WebDragSourceAction](webdragsourceaction/link.md)
  Allows the user to drag a link in the source object.
- [static var selection: WebDragSourceAction](webdragsourceaction/selection.md)
  Allows the user to drag a selection in the source object.
- [static var any: WebDragSourceAction](webdragsourceaction/any.md)
  Allows any defined action to occur.
### Initializers
- [init(rawValue: UInt)](webdragsourceaction/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [Menu Item Tags](menu-item-tags.md)
  Tags that define the types of default menu items passed to the [`webView(_:contextMenuItemsForElement:defaultMenuItems:)`](webuidelegate/webview(_:contextmenuitemsforelement:defaultmenuitems:).md) method.
- [struct WebDragDestinationAction](webdragdestinationaction.md)
  Actions that the destination object of a drag operation can perform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webdragsourceaction)*