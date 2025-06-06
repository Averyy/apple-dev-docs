# LSSetDefaultHandlerForURLScheme(_:_:)

**Framework**: Core Services  
**Kind**: func

Sets the user’s preferred default handler for the specified URL scheme.

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 15.0
- macOS 10.4+ - Deprecated in 12.0

## Declaration

```swift
func LSSetDefaultHandlerForURLScheme(_ inURLScheme: CFString, _ inHandlerBundleID: CFString) -> OSStatus
```

#### Return_value

A result code; see [`Result Codes`](launch_services#1661359.md).

#### Discussion

Call [`LSCopyDefaultHandlerForURLScheme(_:)`](1441725-lscopydefaulthandlerforurlscheme.md) to get the current setting of the user’s preferred default handler for a specified content type.

URL handling capability is determined according to the value of the `CFBundleURLTypes` key in an app’s `Info.plist`. For information on the `CFBundleURLTypes` key, see the section “CFBundleURLTypes” in .

##### 1818418

Thread-safe since OS X v10.4.

## Parameters

- `inURLScheme`: The URL scheme for which the handler is to be set.
- `inHandlerBundleID`: The bundle identifier that is to be set as the handler for the URL scheme specified by  .

## See Also

- [func LSCopyAllRoleHandlersForContentType(CFString, LSRolesMask) -> Unmanaged<CFArray>?](1448020-lscopyallrolehandlersforcontentt.md)
  Locates an array of bundle identifiers for apps capable of handling a specified content type with the specified roles.
- [func LSCopyDefaultRoleHandlerForContentType(CFString, LSRolesMask) -> Unmanaged<CFString>?](1449868-lscopydefaultrolehandlerforconte.md)
  Returns the bundle identifier of the user’s preferred default handler for the specified content type with the specified role.
- [func LSSetDefaultRoleHandlerForContentType(CFString, LSRolesMask, CFString) -> OSStatus](1444955-lssetdefaultrolehandlerforconten.md)
  Sets the user’s preferred default handler for the specified content type in the specified roles.
- [struct LSRolesMask](lsrolesmask.md)
  The specification that sets the desired role or roles for an app to claim for an item or a family of items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1447760-lssetdefaulthandlerforurlscheme)*