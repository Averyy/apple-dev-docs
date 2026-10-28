# LSRolesMask

**Framework**: Core Services  
**Kind**: struct  
**Role**: Structure

The specification that sets the desired role or roles for an app to claim for an item or a family of items.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
struct LSRolesMask
```

```c
typedef enum LSRolesMask : OptionBits {
    ...
} LSRolesMask;
```

## Overview

This bit mask is passed to functions that find the preferred app for an item or family of items (`LSGetApplicationForItem`, `LSGetApplicationForURL`, `LSGetApplicationForInfo`), or that determine whether an app can open a designated item (`LSCanRefAcceptItem`, `LSCanURLAcceptURL`), to specify the app’s desired role or roles for the item. For example, to request only an editor app, specify `kLSRolesEditor`. If either an editor or a viewer app is acceptable, specify `kLSRolesEditor | kLSRolesViewer`.

## Topics

### Constants
- [static var none: LSRolesMask](./lsrolesmask/api-1442696-none.md)
  Requests the role `None` (theapplication cannot open the item, but provides an icon and a kindstring for it).
- [static var viewer: LSRolesMask](./lsrolesmask/api-1441708-viewer.md)
  Requests the role `Viewer` (theapplication can read and present the item, but cannot manipulateor save it).
- [static var editor: LSRolesMask](./lsrolesmask/api-1448087-editor.md)
  Requests the role `Editor` (theapplication can read, present, manipulate, and save the item).
- [static var shell: LSRolesMask](./lsrolesmask/api-1442557-shell.md)
  Requests the role `Shell` (theapplication can execute the item).
- [static var all: LSRolesMask](./lsrolesmask/api-1450616-all.md)
  Accepts any role with respect to the item.
- [kLSRolesNone](./lsrolesmask/klsrolesnone.md)
  Requests the role `None` (theapplication cannot open the item, but provides an icon and a kindstring for it).
- [kLSRolesViewer](./lsrolesmask/klsrolesviewer.md)
  Requests the role `Viewer` (theapplication can read and present the item, but cannot manipulateor save it).
- [kLSRolesEditor](./lsrolesmask/klsroleseditor.md)
  Requests the role `Editor` (theapplication can read, present, manipulate, and save the item).
- [kLSRolesShell](./lsrolesmask/klsrolesshell.md)
  Requests the role `Shell` (theapplication can execute the item).
- [kLSRolesAll](./lsrolesmask/klsrolesall.md)
  Accepts any role with respect to the item.
### Creating a Roles Mask
- [init(rawValue: OptionBits)](./lsrolesmask/api-1445983-init.md)

## Relationships

### Conforms To
- [OptionSet](../Swift/optionset.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Working with Role Handlers
- [func LSCopyAllRoleHandlersForContentType(CFString, LSRolesMask) -> Unmanaged<CFArray>?](./api-1448020-lscopyallrolehandlersforcontentt.md)
  Locates an array of bundle identifiers for apps capable of handling a specified content type with the specified roles.
- [func LSCopyDefaultRoleHandlerForContentType(CFString, LSRolesMask) -> Unmanaged<CFString>?](./api-1449868-lscopydefaultrolehandlerforconte.md)
  Returns the bundle identifier of the user’s preferred default handler for the specified content type with the specified role.
- [func LSSetDefaultRoleHandlerForContentType(CFString, LSRolesMask, CFString) -> OSStatus](./api-1444955-lssetdefaultrolehandlerforconten.md)
  Sets the user’s preferred default handler for the specified content type in the specified roles.
- [func LSSetDefaultHandlerForURLScheme(CFString, CFString) -> OSStatus](./api-1447760-lssetdefaulthandlerforurlscheme.md)
  Sets the user’s preferred default handler for the specified URL scheme.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/lsrolesmask)*