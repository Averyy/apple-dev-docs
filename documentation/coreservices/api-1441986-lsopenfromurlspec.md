# LSOpenFromURLSpec(_:_:)

**Framework**: Core Services  
**Kind**: func

Opens one or more items for a URL in the preferred apps or a designated app.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func LSOpenFromURLSpec(_ inLaunchSpec: UnsafePointer<LSLaunchURLSpec>, _ outLaunchedURL: UnsafeMutablePointer<Unmanaged<CFURL>?>?) -> OSStatus
```

#### Return_value

A result code; see [`Result Codes`](launch_services#1661359.md).

#### Discussion

This function affords greater control of how items are opened or applications launched than is possible with the `LSOpenCFURLRef` function. For instance, you can use it to open multiple items in a single call, in either the same or different applications; open documents for printing rather than for simple viewing or editing; or force a document to open in an application other than its own preferred application.

The launch specification supplied for the `inLaunchSpec` parameter may designate an application to launch, items to open, or both. The relevant application or applications are launched or activated, as required, and sent an appropriate Apple event depending on the circumstances:

- If the launch specification designates both items to open and an application with which to open them, the designated application is used to open all of the items. The application is launched (or activated if it is already running) and sent one or more Apple events:  - If one or more of the item URLs have scheme `file` and designate documents to open, and if the application claims to accept `file` URLs, it is sent a `'GURL'` (“get URL”) Apple event for each such URL.
- If one or more of the item URLs have scheme `file` and designate documents to open, and if the application does not claim to accept `file` URLs, it is sent a single `'odoc'` (“open document”) Apple event containing the list of items to open; if the items are to be printed, the Apple event is `'pdoc'` (“print document”) instead.
- For each item URL with a scheme other than `file`, the application is sent a `'GURL'` (“get URL”) Apple event containing the item’s URL. > **Note**: When both an application and a list of items are supplied, the designated application is asked to open all of the items, whether or not it claims the ability to do so. Launch Services does not report an error if the application is unable to open one or more of the items; any error processing is the application’s responsibility. When both an application and a list of items are supplied, the designated application is asked to open all of the items, whether or not it claims the ability to do so. Launch Services does not report an error if the application is unable to open one or more of the items; any error processing is the application’s responsibility.
- If the launch specification designates items to open but not an application with which to open them, each item is opened in its own preferred application. Each application is launched or activated and sent one or more Apple events, as described for the preceding case. (If two or more of the items have the same preferred application, the application receives a single `'odoc'` or `'pdoc'` event listing all of the relevant items.)
- If the launch specification designates only an application to launch (or if one or more of the items to open are `file` URLs designating applications): - If the application is not already running, it is launched and sent an `'oapp'` (“open application”) Apple event.
- If the application is already running, it is activated and sent an `'rapp'` (“reopen application”) Apple event.

As of macOS 10.4 and later, [`LSOpenURLsWithRole(_:_:_:_:_:_:)`](1448184-lsopenurlswithrole.md) is the preferred way of opening URLs.

##### 1675842

Thread-safe since Mac OS version 10.2.

## Parameters

- `inLaunchSpec`: A pointer to a URL-based launch specification indicating what to open and how to launch the relevant application or applications; see   for a description of this structure.
- `outLaunchedURL`: Despite the absence of the word   in its name, this function retains the URL reference object on your behalf; you are responsible for releasing this object.

## See Also

- [func LSOpenCFURLRef(CFURL, UnsafeMutablePointer<Unmanaged<CFURL>?>?) -> OSStatus](1442850-lsopencfurlref.md)
  Opens an item for a URL in the default manner in its preferred app.
- [struct LSLaunchURLSpec](lslaunchurlspec.md)
  The specification for launching an app, opening items, or both, along with related information.
- [class LSSharedFileList](lssharedfilelist.md)
  A persistent list of file-system objects.
- [class LSSharedFileListItem](lssharedfilelistitem.md)
  A file-system object in the shared file list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1441986-lsopenfromurlspec)*