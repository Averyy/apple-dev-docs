# LSCopyDefaultRoleHandlerForContentType(_:_:)

**Framework**: Core Services  
**Kind**: func

Returns the bundle identifier of the user’s preferred default handler for the specified content type with the specified role.

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 15.0
- macOS 10.4+ - Deprecated in 12.0

## Declaration

```swift
func LSCopyDefaultRoleHandlerForContentType(_ inContentType: CFString, _ inRole: LSRolesMask) -> Unmanaged<CFString>?
```

#### Return_value

The bundle identifier of the default handler for the specified content type in the specified roles, or `NULL` if no handler is available.

#### Discussion

This function returns the user’s currently preferred default handler for the specified content type. Say, for example, that [`LSSetDefaultRoleHandlerForContentType(_:_:_:)`](1444955-lssetdefaultrolehandlerforconten.md) has been used to set “com.Apple.TextEdit” for the “public.xml” content type. When a file whose content type is “public.xml” is double-clicked, TextEdit will be launched to open the file. If you call `LSCopyDefaultRoleHandlerForContentType(CFSTR(“public.xml”), kLSRolesAll)`, the string `com.apple.TextEdit` is returned.

The [`CFBundleDocumentTypes`](https://developer.apple.com/documentation/bundleresources/information-property-list/cfbundledocumenttypes) key in an app’s `Info.plist` can be used to set an app’s content handling capabilities. The `LSItemContentTypes` key is particularly useful because it supports the use of UTIs in document claims.

##### 1818366

Thread-safe since OS X v10.4.

## Parameters

- `inContentType`: The content type. The content type is a uniform type identifier.
- `inRole`: The role. Pass   if any role is acceptable. For additional possible values, see  .

## See Also

- [func LSCopyAllRoleHandlersForContentType(CFString, LSRolesMask) -> Unmanaged<CFArray>?](1448020-lscopyallrolehandlersforcontentt.md)
  Locates an array of bundle identifiers for apps capable of handling a specified content type with the specified roles.
- [func LSSetDefaultRoleHandlerForContentType(CFString, LSRolesMask, CFString) -> OSStatus](1444955-lssetdefaultrolehandlerforconten.md)
  Sets the user’s preferred default handler for the specified content type in the specified roles.
- [func LSSetDefaultHandlerForURLScheme(CFString, CFString) -> OSStatus](1447760-lssetdefaulthandlerforurlscheme.md)
  Sets the user’s preferred default handler for the specified URL scheme.
- [struct LSRolesMask](lsrolesmask.md)
  The specification that sets the desired role or roles for an app to claim for an item or a family of items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1449868-lscopydefaultrolehandlerforconte)*