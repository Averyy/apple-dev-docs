# LSCopyAllRoleHandlersForContentType(_:_:)

**Framework**: Core Services  
**Kind**: func

Locates an array of bundle identifiers for apps capable of handling a specified content type with the specified roles.

**Availability**:
- macOS 10.4+ - Deprecated in 12.0

## Declaration

```swift
func LSCopyAllRoleHandlersForContentType(_ inContentType: CFString, _ inRole: LSRolesMask) -> Unmanaged<CFArray>?
```

#### Return_value

The bundle identifiers for apps capable of handling the specified content type in the specified roles, or `NULL` if no handlers are available.

In macOS 10.15 and later, the returned array is sorted so that the first element contains the bundle identifier of the best available app for opening the content type. Prior to macOS 10.15, the order of elements in the array was undefined.

#### Discussion

This function returns all of the bundle identifiers that are capable of handling the specified content type in the specified roles.

The [`CFBundleDocumentTypes`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Articles/CoreFoundationKeys.html#//apple_ref/doc/uid/20001431-101685) key in an app’s `Info.plist` can be used to set an app’s content handling capabilities. The [`LSItemContentTypes`](https://developer.apple.com/documentation/bundleresources/information-property-list/cfbundledocumenttypes/lsitemcontenttypes) key is particularly useful because it supports the use of UTIs in document claims.

##### 1818345

Thread-safe since macOS 10.4.

## Parameters

- `inContentType`: The content type. The content type is a uniform type identifier.
- `inRole`: The role. Pass   if any role is acceptable. For additional possible values, see  .

## See Also

- [func LSCopyDefaultRoleHandlerForContentType(CFString, LSRolesMask) -> Unmanaged<CFString>?](1449868-lscopydefaultrolehandlerforconte.md)
  Returns the bundle identifier of the user’s preferred default handler for the specified content type with the specified role.
- [func LSSetDefaultRoleHandlerForContentType(CFString, LSRolesMask, CFString) -> OSStatus](1444955-lssetdefaultrolehandlerforconten.md)
  Sets the user’s preferred default handler for the specified content type in the specified roles.
- [func LSSetDefaultHandlerForURLScheme(CFString, CFString) -> OSStatus](1447760-lssetdefaulthandlerforurlscheme.md)
  Sets the user’s preferred default handler for the specified URL scheme.
- [struct LSRolesMask](lsrolesmask.md)
  The specification that sets the desired role or roles for an app to claim for an item or a family of items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1448020-lscopyallrolehandlersforcontentt)*