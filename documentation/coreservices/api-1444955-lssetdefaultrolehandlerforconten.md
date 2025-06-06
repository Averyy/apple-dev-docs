# LSSetDefaultRoleHandlerForContentType(_:_:_:)

**Framework**: Core Services  
**Kind**: func

Sets the user’s preferred default handler for the specified content type in the specified roles.

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 15.0
- macOS 10.4+ - Deprecated in 12.0

## Declaration

```swift
func LSSetDefaultRoleHandlerForContentType(_ inContentType: CFString, _ inRole: LSRolesMask, _ inHandlerBundleID: CFString) -> OSStatus
```

#### Return_value

A result code; see [`Result Codes`](launch_services#1661359.md).

#### Discussion

Call [`LSCopyDefaultRoleHandlerForContentType(_:_:)`](1449868-lscopydefaultrolehandlerforconte.md) to get the current setting of the user’s preferred default handler for a specified content type.

##### 1676309

Thread-safe since OS X v10.4.

## Parameters

- `inContentType`: The content type for which the default role handler is being set. The content type is a uniform type identifier.
- `inRole`: The roles for which the default role handler is being set. Pass   to specify all roles. For additional possible values, see  .
- `inHandlerBundleID`: The bundle identifier that is to be set as the default handler for the specified content type and roles.

## See Also

- [func LSCopyAllRoleHandlersForContentType(CFString, LSRolesMask) -> Unmanaged<CFArray>?](1448020-lscopyallrolehandlersforcontentt.md)
  Locates an array of bundle identifiers for apps capable of handling a specified content type with the specified roles.
- [func LSCopyDefaultRoleHandlerForContentType(CFString, LSRolesMask) -> Unmanaged<CFString>?](1449868-lscopydefaultrolehandlerforconte.md)
  Returns the bundle identifier of the user’s preferred default handler for the specified content type with the specified role.
- [func LSSetDefaultHandlerForURLScheme(CFString, CFString) -> OSStatus](1447760-lssetdefaulthandlerforurlscheme.md)
  Sets the user’s preferred default handler for the specified URL scheme.
- [struct LSRolesMask](lsrolesmask.md)
  The specification that sets the desired role or roles for an app to claim for an item or a family of items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1444955-lssetdefaultrolehandlerforconten)*