# ASAccessory.RenameOptions

**Framework**: AccessorySetupKit  
**Kind**: struct

Options that affect the behavior of an accessory renaming operation.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
struct RenameOptions
```

## Topics

### Creating an options instance
- [init(rawValue: UInt)](asaccessory/renameoptions/init(rawvalue:).md)
### Options
- [static var ssid: ASAccessory.RenameOptions](asaccessory/renameoptions/ssid.md)
  An option to change an accessory’s SSID along with its display name.

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

- [func renameAccessory(ASAccessory, options: ASAccessory.RenameOptions, completionHandler: ((any Error)?) -> Void)](asaccessorysession/renameaccessory(_:options:completionhandler:).md)
  Displays a view to rename an accessory.
- [func removeAccessory(ASAccessory, completionHandler: ((any Error)?) -> Void)](asaccessorysession/removeaccessory(_:completionhandler:).md)
  Removes an accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorysetupkit/asaccessory/renameoptions)*