# WebDragDestinationAction

**Framework**: WebKit  
**Kind**: struct

Actions that the destination object of a drag operation can perform.

**Availability**:
- macOS 10.3+

## Declaration

```swift
struct WebDragDestinationAction
```

## Topics

### Constants
- [static var DHTML: WebDragDestinationAction](webdragdestinationaction/dhtml.md)
  Allows DHTML (such as JavaScript) to handle the drag.
- [static var edit: WebDragDestinationAction](webdragdestinationaction/edit.md)
  Allows editable documents to be changed by the drag operation.
- [static var load: WebDragDestinationAction](webdragdestinationaction/load.md)
  Allows the drag operation to change the location.
- [static var any: WebDragDestinationAction](webdragdestinationaction/any.md)
  Allows any defined action to occur.
### Initializers
- [init(rawValue: UInt)](webdragdestinationaction/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [Menu Item Tags](menu-item-tags.md)
  Tags that define the types of default menu items passed to the [`webView(_:contextMenuItemsForElement:defaultMenuItems:)`](webuidelegate/webview(_:contextmenuitemsforelement:defaultmenuitems:).md) method.
- [struct WebDragSourceAction](webdragsourceaction.md)
  Actions that the source object of a drag operation can perform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webdragdestinationaction)*