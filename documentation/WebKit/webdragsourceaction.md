# WebDragSourceAction

**Framework**: WebKit  
**Kind**: struct  
**Role**: Structure

Actions that the source object of a drag operation can perform.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
struct WebDragSourceAction
```

```c
enum WebDragSourceAction : NSUInteger;
```

## Topics

### Constants
- [static var DHTML: WebDragSourceAction](./webdragsourceaction/dhtml.md)
  Allows DHTML (such as JavaScript) in the source object to initiate a drag operation.
- [static var image: WebDragSourceAction](./webdragsourceaction/image.md)
  Allows the user to drag an image in the source object.
- [static var link: WebDragSourceAction](./webdragsourceaction/link.md)
  Allows the user to drag a link in the source object.
- [static var selection: WebDragSourceAction](./webdragsourceaction/selection.md)
  Allows the user to drag a selection in the source object.
- [static var any: WebDragSourceAction](./webdragsourceaction/any.md)
  Allows any defined action to occur.
### Initializers
- [init(rawValue: UInt)](./webdragsourceaction/init%28rawvalue%29.md)

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
- [struct WebDragDestinationAction](./webdragdestinationaction.md)
  Actions that the destination object of a drag operation can perform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webdragsourceaction)*