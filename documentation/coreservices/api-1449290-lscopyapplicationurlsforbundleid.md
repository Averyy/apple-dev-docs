# LSCopyApplicationURLsForBundleIdentifier(_:_:)

**Framework**: Core Services  
**Kind**: func

Locates all URLs for apps that correspond to the specified bundle identifier.

**Availability**:
- macOS 10.10+ - Deprecated in 12.0

## Declaration

```swift
func LSCopyApplicationURLsForBundleIdentifier(_ inBundleIdentifier: CFString, _ outError: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Unmanaged<CFArray>?
```

#### Return_value

The URLs for any applications with the specified bundle identifier returned in a `CFArray`. If no application is found, `NULL` is returned and `outError` (if not `NULL`) is populated with [`kLSApplicationNotFoundErr`](klsapplicationnotfounderr.md).

In macOS 10.15 and later, the returned array is sorted with the first element containing the best available application with the specified bundle identifier. Prior to macOS 10.15, the order of elements in the array was undefined.

The caller is responsible for releasing this array.

## Parameters

- `inBundleIdentifier`: The bundle identifier of interest, such as "com.apple.finder". Must not be  .
- `outError`: On failure, set to a   describing the problem. If you aren't interested in this information, pass  . The caller is responsible for releasing this object.

## See Also

- [func LSCopyDefaultApplicationURLForURL(CFURL, LSRolesMask, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Unmanaged<CFURL>?](1448824-lscopydefaultapplicationurlforur.md)
  Returns the app that opens an item.
- [func LSCopyDefaultApplicationURLForContentType(CFString, LSRolesMask, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Unmanaged<CFURL>?](1447734-lscopydefaultapplicationurlforco.md)
  Returns the app that opens a content type.
- [func LSCopyApplicationURLsForURL(CFURL, LSRolesMask) -> Unmanaged<CFArray>?](1445148-lscopyapplicationurlsforurl.md)
  Locates all known apps suitable for opening an item for the specified URL.
- [func LSCanURLAcceptURL(CFURL, CFURL, LSRolesMask, LSAcceptanceFlags, UnsafeMutablePointer<DarwinBoolean>) -> OSStatus](1441854-lscanurlaccepturl.md)
  Tests whether an app can accept (open) an item for a URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1449290-lscopyapplicationurlsforbundleid)*