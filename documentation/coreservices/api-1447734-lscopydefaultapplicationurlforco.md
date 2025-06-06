# LSCopyDefaultApplicationURLForContentType(_:_:_:)

**Framework**: Core Services  
**Kind**: func

Returns the app that opens a content type.

**Availability**:
- macOS 10.10+ - Deprecated in 12.0

## Declaration

```swift
func LSCopyDefaultApplicationURLForContentType(_ inContentType: CFString, _ inRoleMask: LSRolesMask, _ outError: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Unmanaged<CFURL>?
```

#### Return_value

If an acceptable app is found, its URL is returned. If no app could be found, `NULL` is returned and `outError` (if not `NULL`) is populated with [`kLSApplicationNotFoundErr`](klsapplicationnotfounderr.md). The caller is responsible for releasing this URL.

#### Discussion

Consults the binding tables to return the application that would be used to open a file of type `inContentType` if it were double-clicked in the Finder. This app will be the user-specified override if appropriate or the default otherwise.

## Parameters

- `inContentType`: The Uniform Type Identifier (UTI) of the item for which the app is requested.
- `inRoleMask`: Whether to return the editor or viewer for  . If you don't care which, use  .
- `outError`: On failure, set to a   describing the problem. If you are not interested in this information, pass  . The caller is responsible for releasing this object.

## See Also

- [func LSCopyDefaultApplicationURLForURL(CFURL, LSRolesMask, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Unmanaged<CFURL>?](1448824-lscopydefaultapplicationurlforur.md)
  Returns the app that opens an item.
- [func LSCopyApplicationURLsForURL(CFURL, LSRolesMask) -> Unmanaged<CFArray>?](1445148-lscopyapplicationurlsforurl.md)
  Locates all known apps suitable for opening an item for the specified URL.
- [func LSCanURLAcceptURL(CFURL, CFURL, LSRolesMask, LSAcceptanceFlags, UnsafeMutablePointer<DarwinBoolean>) -> OSStatus](1441854-lscanurlaccepturl.md)
  Tests whether an app can accept (open) an item for a URL.
- [func LSCopyApplicationURLsForBundleIdentifier(CFString, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Unmanaged<CFArray>?](1449290-lscopyapplicationurlsforbundleid.md)
  Locates all URLs for apps that correspond to the specified bundle identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1447734-lscopydefaultapplicationurlforco)*