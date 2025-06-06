# LSCanURLAcceptURL(_:_:_:_:_:)

**Framework**: Core Services  
**Kind**: func

Tests whether an app can accept (open) an item for a URL.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func LSCanURLAcceptURL(_ inItemURL: CFURL, _ inTargetURL: CFURL, _ inRoleMask: LSRolesMask, _ inFlags: LSAcceptanceFlags, _ outAcceptsItem: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus
```

#### Return_value

A result code; see [`Result Codes`](launch_services#1661359.md).

#### Discussion

If the item URL’s scheme is `file` (designating either a file or a directory), the acceptance test is based on the designated item’s filename extension, file type, and creator signature, along with the role specified by the `inRolesMask` parameter; otherwise, it is based on the URL scheme (such as `http`, `ftp`, or `mailto`).

##### 1675609

Thread-safe since Mac OS version 10.2.

## Parameters

- `inItemURL`: A Core Foundation URL reference designating the source item (the item to test for acceptance by the target application); see the   in the Core Foundation Reference Documentation for a description of the   data type.
- `inTargetURL`: A Core Foundation URL reference designating the target application; see the   in the Core Foundation Reference Documentation for a description of the   data type. The URL must have scheme   and contain a valid path to an application file or application bundle.
- `inRolesMask`: A bit mask specifying the target app’s desired role or roles with respect to the source item; see   for a description of this mask. This parameter applies only to URLs with a scheme component of  , and is ignored for all other schemes. If the role is unimportant, pass  .
- `inFlags`: Flags specifying behavior to observe during the acceptance test; see   for a description of these flags.
- `outAcceptsItem`: A pointer to a Boolean value that, on return, will indicate whether the target application can accept the source item with at least one of the specified roles.

## See Also

- [func LSCopyDefaultApplicationURLForURL(CFURL, LSRolesMask, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Unmanaged<CFURL>?](1448824-lscopydefaultapplicationurlforur.md)
  Returns the app that opens an item.
- [func LSCopyDefaultApplicationURLForContentType(CFString, LSRolesMask, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Unmanaged<CFURL>?](1447734-lscopydefaultapplicationurlforco.md)
  Returns the app that opens a content type.
- [func LSCopyApplicationURLsForURL(CFURL, LSRolesMask) -> Unmanaged<CFArray>?](1445148-lscopyapplicationurlsforurl.md)
  Locates all known apps suitable for opening an item for the specified URL.
- [func LSCopyApplicationURLsForBundleIdentifier(CFString, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Unmanaged<CFArray>?](1449290-lscopyapplicationurlsforbundleid.md)
  Locates all URLs for apps that correspond to the specified bundle identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1441854-lscanurlaccepturl)*