# LSCopyApplicationURLsForURL(_:_:)

**Framework**: Core Services  
**Kind**: func

Locates all known apps suitable for opening an item for the specified URL.

**Availability**:
- macOS 10.3+ - Deprecated in 12.0

## Declaration

```swift
func LSCopyApplicationURLsForURL(_ inURL: CFURL, _ inRoleMask: LSRolesMask) -> Unmanaged<CFArray>?
```

#### Return_value

An array of Core Foundation URL references, one for each app that can open the designated item with at least one of the specified roles. You are responsible for releasing the array object. If no suitable apps are found in the Launch Services database, the function will return `NULL.`

In macOS 10.15 and later, the returned array is sorted with the first element containing the best available apps for opening the specified URL. Prior to macOS 10.15, the order of elements in the array was undefined.

#### Discussion

If the item URL’s scheme is `file` (designating either a file or a directory), the selection of suitable applications is based on the designated item’s filename extension, file type, and creator signature, along with the role specified by the `inRolesMask` parameter. Otherwise, the selection is based on the URL scheme (such as `http`, `ftp`, or `mailto`).

##### 1675582

Thread-safe since macOS 10.3.

## Parameters

- `inURL`: A Core Foundation URL reference designating the item for which all suitable apps are requested. See   for a description of the   data type.
- `inRolesMask`: A bit mask specifying the apps’ role or roles with respect to the designated item. See   for a description of this mask. This parameter applies only to URLs with a scheme component of  , and is ignored for all other schemes. If the role is unimportant, pass  .

## See Also

- [func LSCopyDefaultApplicationURLForURL(CFURL, LSRolesMask, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Unmanaged<CFURL>?](1448824-lscopydefaultapplicationurlforur.md)
  Returns the app that opens an item.
- [func LSCopyDefaultApplicationURLForContentType(CFString, LSRolesMask, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Unmanaged<CFURL>?](1447734-lscopydefaultapplicationurlforco.md)
  Returns the app that opens a content type.
- [func LSCanURLAcceptURL(CFURL, CFURL, LSRolesMask, LSAcceptanceFlags, UnsafeMutablePointer<DarwinBoolean>) -> OSStatus](1441854-lscanurlaccepturl.md)
  Tests whether an app can accept (open) an item for a URL.
- [func LSCopyApplicationURLsForBundleIdentifier(CFString, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Unmanaged<CFArray>?](1449290-lscopyapplicationurlsforbundleid.md)
  Locates all URLs for apps that correspond to the specified bundle identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1445148-lscopyapplicationurlsforurl)*