# WebDragDestinationAction

**Framework**: WebKit  
**Kind**: struct  
**Role**: Structure

Actions that the destination object of a drag operation can perform.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
struct WebDragDestinationAction
```

```c
enum WebDragDestinationAction : NSUInteger;
```

## Topics

### Constants
- [static var DHTML: WebDragDestinationAction](./webdragdestinationaction/dhtml.md)
  Allows DHTML (such as JavaScript) to handle the drag.
- [static var edit: WebDragDestinationAction](./webdragdestinationaction/edit.md)
  Allows editable documents to be changed by the drag operation.
- [static var load: WebDragDestinationAction](./webdragdestinationaction/load.md)
  Allows the drag operation to change the location.
- [static var any: WebDragDestinationAction](./webdragdestinationaction/any.md)
  Allows any defined action to occur.
- [WebDragDestinationActionNone](./webdragdestinationaction/webdragdestinationactionnone.md)
  No action.
### Initializers
- [init(rawValue: UInt)](./webdragdestinationaction/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Constants
- [Menu Item Tags](./menu-item-tags.md)
  Tags that define the types of default menu items passed to the [`webView(_:contextMenuItemsForElement:defaultMenuItems:)`](./webuidelegate/webview%28_,contextmenuitemsforelement,defaultmenuitems%29.md) method.
- [struct WebDragSourceAction](./webdragsourceaction.md)
  Actions that the source object of a drag operation can perform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webdragdestinationaction)*