# LSRolesMask

**Framework**: Core Services  
**Kind**: struct

The specification that sets the desired role or roles for an app to claim for an item or a family of items.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
struct LSRolesMask
```

#### Overview

This bit mask is passed to functions that find the preferred app for an item or family of items (`LSGetApplicationForItem`, `LSGetApplicationForURL`, `LSGetApplicationForInfo`), or that determine whether an app can open a designated item (`LSCanRefAcceptItem`, `LSCanURLAcceptURL`), to specify the app’s desired role or roles for the item. For example, to request only an editor app, specify `kLSRolesEditor`. If either an editor or a viewer app is acceptable, specify `kLSRolesEditor | kLSRolesViewer`.

## Topics

### Constants
- [static var none: LSRolesMask](lsrolesmask/1442696-none.md)
  Requests the role `None` (theapplication cannot open the item, but provides an icon and a kindstring for it).
- [static var viewer: LSRolesMask](lsrolesmask/1441708-viewer.md)
  Requests the role `Viewer` (theapplication can read and present the item, but cannot manipulateor save it).
- [static var editor: LSRolesMask](lsrolesmask/1448087-editor.md)
  Requests the role `Editor` (theapplication can read, present, manipulate, and save the item).
- [static var shell: LSRolesMask](lsrolesmask/1442557-shell.md)
  Requests the role `Shell` (theapplication can execute the item).
- [static var all: LSRolesMask](lsrolesmask/1450616-all.md)
  Accepts any role with respect to the item.
### Creating a Roles Mask
- [init(rawValue: OptionBits)](lsrolesmask/1445983-init.md)

## Relationships

### Conforms To
- [OptionSet](../swift/optionset.md)
- [Sendable](../swift/sendable.md)

## See Also

- [func LSCopyAllRoleHandlersForContentType(CFString, LSRolesMask) -> Unmanaged<CFArray>?](1448020-lscopyallrolehandlersforcontentt.md)
  Locates an array of bundle identifiers for apps capable of handling a specified content type with the specified roles.
- [func LSCopyDefaultRoleHandlerForContentType(CFString, LSRolesMask) -> Unmanaged<CFString>?](1449868-lscopydefaultrolehandlerforconte.md)
  Returns the bundle identifier of the user’s preferred default handler for the specified content type with the specified role.
- [func LSSetDefaultRoleHandlerForContentType(CFString, LSRolesMask, CFString) -> OSStatus](1444955-lssetdefaultrolehandlerforconten.md)
  Sets the user’s preferred default handler for the specified content type in the specified roles.
- [func LSSetDefaultHandlerForURLScheme(CFString, CFString) -> OSStatus](1447760-lssetdefaulthandlerforurlscheme.md)
  Sets the user’s preferred default handler for the specified URL scheme.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/lsrolesmask)*