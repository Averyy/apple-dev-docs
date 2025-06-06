# LSOpenCFURLRef(_:_:)

**Framework**: Core Services  
**Kind**: func

Opens an item for a URL in the default manner in its preferred app.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func LSOpenCFURLRef(_ inURL: CFURL, _ outLaunchedURL: UnsafeMutablePointer<Unmanaged<CFURL>?>?) -> OSStatus
```

#### Return_value

A result code; see [`Result Codes`](launch_services#1661359.md).

#### Discussion

The designated item is opened in the default manner, as if it had been opened with the `LSOpenFromURLSpec` function with a launch specification specifying the launch flag `kLSLaunchDefaults`: that is, asynchronously, and with the remaining launch parameters taken from the application’s information property list. For greater control, call `LSOpenFromURLSpec` directly. See [`LSLaunchFlags`](lslaunchflags.md) for more information about launch flags.

If the item URL’s scheme is `file` (designating either a file or a directory), the selection of the preferred application is based on the designated item’s filename extension, file type, and creator signature; otherwise, it is based on the URL scheme (such as `http`, `ftp`, or `mailto`). The application is launched or activated, as required, and sent an appropriate Apple event depending on the circumstances:

- If the URL’s scheme is `file` and it designates a document, the document’s preferred application is launched (or activated if it is already running). - If the application claims to accept `file` URLs, it is sent a `'GURL'` (“get URL”) Apple event containing the item’s URL.
- If the application does not claim to accept `file` URLs, it is sent an `'odoc'` (“open document”) Apple event identifying the document to open.
- If the URL’s scheme is `file` and it designates an application:  - If the application is not already running, it is launched and sent an `'oapp'` (“open application”) Apple event.
- If the application is already running, it is activated and sent an `'rapp'` (“reopen application”) Apple event.
- If the URL has a scheme other than `file`, the scheme’s preferred application is launched (or activated if it is already running) and sent a `'GURL'` (“get URL”) Apple event containing the item’s URL.

As of macOS 10.4 and later, [`launchApplication(at:options:configuration:)`](https://developer.apple.com/documentation/appkit/nsworkspace/launchapplication(at:options:configuration:)) is the preferred way of opening a URL.

##### 1675829

Thread-safe since Mac OS version 10.2.

## Parameters

- `inURL`: A Core Foundation URL reference designating the item to open; see the   in the Core Foundation Reference Documentation for a description of the   data type.
- `outLaunchedURL`: Despite the absence of the word   in its name, this function retains the URL reference object on your behalf; you are responsible for releasing this object.

## See Also

- [func LSOpenFromURLSpec(UnsafePointer<LSLaunchURLSpec>, UnsafeMutablePointer<Unmanaged<CFURL>?>?) -> OSStatus](1441986-lsopenfromurlspec.md)
  Opens one or more items for a URL in the preferred apps or a designated app.
- [struct LSLaunchURLSpec](lslaunchurlspec.md)
  The specification for launching an app, opening items, or both, along with related information.
- [class LSSharedFileList](lssharedfilelist.md)
  A persistent list of file-system objects.
- [class LSSharedFileListItem](lssharedfilelistitem.md)
  A file-system object in the shared file list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1442850-lsopencfurlref)*