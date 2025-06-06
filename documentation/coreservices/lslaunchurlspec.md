# LSLaunchURLSpec

**Framework**: Core Services  
**Kind**: struct

The specification for launching an app, opening items, or both, along with related information.

**Availability**:
- macOS 10.0+

## Declaration

```swift
struct LSLaunchURLSpec
```

#### Overview

This data type defines a URL-based launch specification designating, by URL, an app to launch, items to open, or both. To request that items be opened in a particular app, set `appURL` and `itemURLs` accordingly. To request that each designated item be opened in its own preferred app, set `appURL` to `NULL`.If the item URL’s scheme is `file` (designating either a file or a directory), the selection of the preferred app is based on the designated item’s filename extension, file type, and creator signature; otherwise, it is based on the URL scheme (such as `http`, `ftp`, or `mailto`). To request that a particular app be launched without opening any document, set `appURL` accordingly and set `itemURLs` to `NULL`.

## Topics

### Creating a Launch URL
- [init()](lslaunchurlspec/1444528-init.md)
  Create a launch URL.
- [init(appURL: Unmanaged<CFURL>?, itemURLs: Unmanaged<CFArray>?, passThruParams: UnsafePointer<AEDesc>?, launchFlags: LSLaunchFlags, asyncRefCon: UnsafeMutableRawPointer?)](lslaunchurlspec/1446360-init.md)
  Create a launch URL with the provided parameters.
### Configuring a Launch URL
- [var appURL: Unmanaged<CFURL>?](lslaunchurlspec/1443566-appurl.md)
  A Core Foundation URL reference designating the application to launch; see the  in the Core Foundation Reference Documentation for a description of the `CFURLRef` data type.The URL must have scheme `file` and contain a valid path to an application file or application bundle. Set this field to `NULL` to request that each item in the `itemURLs` array be opened in its own preferred application.
- [var asyncRefCon: UnsafeMutableRawPointer?](lslaunchurlspec/1448168-asyncrefcon.md)
  A pointer to an arbitrary application-defined value, passed in the Carbon event notifying you of an application’s launch or termination (if you have registered for such notification). The value of this field can be `NULL`.
- [var itemURLs: Unmanaged<CFArray>?](lslaunchurlspec/1443759-itemurls.md)
  A reference to an array of Core Foundation URL references designating the item or items to open; see the  in the Core Foundation Reference Documentation for a description of the `CFArrayRef` data type. The value of this field can be `NULL`, in which case the application designated by `appURL` will be launched without opening any items.
- [var launchFlags: LSLaunchFlags](lslaunchurlspec/1443957-launchflags.md)
  Launch flags specifying how to launch each application (including whether to print or merely open documents); see [`LSLaunchFlags`](lslaunchflags.md) for a description of these flags.
- [var passThruParams: UnsafePointer<AEDesc>?](lslaunchurlspec/1445136-passthruparams.md)
  A pointer to an Apple event descriptor that is passed untouched as an optional parameter, with keyword `keyAEPropData` (`'prdt'`), in the Apple event sent to each application launched or activated (whether individual preferred applications or the application designated by `appURL`). See the  in the Carbon Interapplication Communication Documentation for a description of the `AEDesc` data type. The value of this field can be `NULL`.

## See Also

- [func LSOpenCFURLRef(CFURL, UnsafeMutablePointer<Unmanaged<CFURL>?>?) -> OSStatus](1442850-lsopencfurlref.md)
  Opens an item for a URL in the default manner in its preferred app.
- [func LSOpenFromURLSpec(UnsafePointer<LSLaunchURLSpec>, UnsafeMutablePointer<Unmanaged<CFURL>?>?) -> OSStatus](1441986-lsopenfromurlspec.md)
  Opens one or more items for a URL in the preferred apps or a designated app.
- [class LSSharedFileList](lssharedfilelist.md)
  A persistent list of file-system objects.
- [class LSSharedFileListItem](lssharedfilelistitem.md)
  A file-system object in the shared file list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/lslaunchurlspec)*