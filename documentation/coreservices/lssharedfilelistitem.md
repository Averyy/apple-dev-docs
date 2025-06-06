# LSSharedFileListItem

**Framework**: Core Services  
**Kind**: cl

A file-system object in the shared file list.

**Availability**:
- Mac Catalyst 16.0+
- macOS 10.5+

## Declaration

```swift
class LSSharedFileListItem
```

## See Also

- [func LSOpenCFURLRef(CFURL, UnsafeMutablePointer<Unmanaged<CFURL>?>?) -> OSStatus](1442850-lsopencfurlref.md)
  Opens an item for a URL in the default manner in its preferred app.
- [func LSOpenFromURLSpec(UnsafePointer<LSLaunchURLSpec>, UnsafeMutablePointer<Unmanaged<CFURL>?>?) -> OSStatus](1441986-lsopenfromurlspec.md)
  Opens one or more items for a URL in the preferred apps or a designated app.
- [struct LSLaunchURLSpec](lslaunchurlspec.md)
  The specification for launching an app, opening items, or both, along with related information.
- [class LSSharedFileList](lssharedfilelist.md)
  A persistent list of file-system objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/lssharedfilelistitem)*