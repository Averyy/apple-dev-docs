# LSOpenFromRefSpec(_:_:)

**Framework**: Core Services  
**Kind**: func

Opens one or more items with a file-system reference in either their preferred apps or a designated app.

**Availability**:
- macOS 10.0+ - Deprecated in 10.10

## Declaration

```swift
func LSOpenFromRefSpec(_ inLaunchSpec: UnsafePointer<LSLaunchFSRefSpec>!, _ outLaunchedRef: UnsafeMutablePointer<FSRef>!) -> OSStatus
```

#### Return_value

A result code; see [`Result Codes`](launch_services#1661359.md).

#### Discussion

This function affords greater control of how items are opened or applications launched than is possible with the `LSOpenFSRef` function. For instance, you can use it to open multiple items in a single call, in either the same or different applications; open documents for printing rather than for simple viewing or editing; or force a document to open in an application other than its own preferred application.

The launch specification supplied for the `inLaunchSpec` parameter may designate an application to launch, items to open, or both. The relevant application or applications are launched or activated, as required, and sent an appropriate Apple event depending on the circumstances:

- If the launch specification designates both items to open and an application with which to open them, the designated application is used to open all of the items. The application is launched (or activated if it is already running) and sent an `'odoc'` (“open document”) Apple event containing the list of items to open; if the items are to be printed, the Apple event is `'pdoc'` (“print document”) instead. > **Note**: When both an application and a list of items are supplied, the designated application is asked to open all of the items, whether or not it claims the ability to do so. Launch Services does not report an error if the application is unable to open one or more of the items; any error processing is the application’s responsibility. When both an application and a list of items are supplied, the designated application is asked to open all of the items, whether or not it claims the ability to do so. Launch Services does not report an error if the application is unable to open one or more of the items; any error processing is the application’s responsibility.
- If the launch specification designates items to open but not an application with which to open them, each item is opened in its own preferred application. Each application is launched or activated and sent an `'odoc'` or `'pdoc'` Apple event, as described for the preceding case. (If two or more of the items have the same preferred application, the application receives a single `'odoc'` or `'pdoc'` event listing all of the relevant items.)
- If the launch specification designates only an application to launch (or if one or more of the items to open are applications): - If the application is not already running, it is launched and sent an `'oapp'` (“open application”) Apple event.
- If the application is already running, it is activated and sent an `'rapp'` (“reopen application”) Apple event.

As of macOS 10.4 and later, [`LSOpenItemsWithRole(_:_:_:_:_:_:_:)`](1449783-lsopenitemswithrole.md) is the preferred way of opening items.

##### 1675802

Thread-safe since Mac OS version 10.2.

## Parameters

- `inLaunchSpec`: A pointer to a file-based launch specification indicating what to open and how to launch the relevant application or applications; see   for a description of this structure.
- `outLaunchedRef`: A pointer to a file-system reference that, on return, will identify the application launched; see the   in the Carbon File Management Documentation for a description of the   data type. Pass   if this information is unimportant. If more than one application is launched, the one identified will be the one corresponding to the first item designated in the launch specification.

## See Also

- [func LSGetHandlerOptionsForContentType(CFString!) -> LSHandlerOptions](1445296-lsgethandleroptionsforcontenttyp.md)
  Gets the handler options for the specified content type.
- [func LSSetHandlerOptionsForContentType(CFString!, LSHandlerOptions) -> OSStatus](1447588-lssethandleroptionsforcontenttyp.md)
  Sets the handler option for the specified content type.
- [func LSCopyAllHandlersForURLScheme(CFString) -> Unmanaged<CFArray>?](1443240-lscopyallhandlersforurlscheme.md)
  Locates app bundle identifiers for apps capable of handling the specified URL scheme.
- [func LSCopyDefaultHandlerForURLScheme(CFString) -> Unmanaged<CFString>?](1441725-lscopydefaulthandlerforurlscheme.md)
  Returns the bundle identifier of the user’s preferred default handler for the specified URL scheme.
- [func LSGetApplicationForItem(UnsafePointer<FSRef>!, LSRolesMask, UnsafeMutablePointer<FSRef>!, UnsafeMutablePointer<Unmanaged<CFURL>?>!) -> OSStatus](1446185-lsgetapplicationforitem.md)
  Locates the preferred app for opening an item with a file-system reference.
- [func LSGetApplicationForURL(CFURL!, LSRolesMask, UnsafeMutablePointer<FSRef>!, UnsafeMutablePointer<Unmanaged<CFURL>?>!) -> OSStatus](1445210-lsgetapplicationforurl.md)
  Locates the preferred app for opening an item with a URL.
- [func LSGetApplicationForInfo(OSType, OSType, CFString!, LSRolesMask, UnsafeMutablePointer<FSRef>!, UnsafeMutablePointer<Unmanaged<CFURL>?>!) -> OSStatus](1449928-lsgetapplicationforinfo.md)
  Locates the preferred app for opening items with a specified file type, creator signature, filename extension, or any combination of these characteristics.
- [func LSCopyApplicationForMIMEType(CFString!, LSRolesMask, UnsafeMutablePointer<Unmanaged<CFURL>?>!) -> OSStatus](1448586-lscopyapplicationformimetype.md)
  Locates the preferred app for opening items with a specified MIME type.
- [func LSCanRefAcceptItem(UnsafePointer<FSRef>!, UnsafePointer<FSRef>!, LSRolesMask, LSAcceptanceFlags, UnsafeMutablePointer<DarwinBoolean>!) -> OSStatus](1442183-lscanrefacceptitem.md)
  Tests whether an app can accept (open) an item with a file-system reference.
- [func LSFindApplicationForInfo(OSType, CFString!, CFString!, UnsafeMutablePointer<FSRef>!, UnsafeMutablePointer<Unmanaged<CFURL>?>!) -> OSStatus](1449588-lsfindapplicationforinfo.md)
  Locates an app with a specified creator signature, bundle ID, filename, or any combination of these characteristics.
- [func LSOpenApplication(UnsafePointer<LSApplicationParameters>!, UnsafeMutablePointer<ProcessSerialNumber>!) -> OSStatus](1447930-lsopenapplication.md)
  Launches the specified app.
- [func LSOpenItemsWithRole(UnsafePointer<FSRef>!, CFIndex, LSRolesMask, UnsafePointer<AEKeyDesc>!, UnsafePointer<LSApplicationParameters>!, UnsafeMutablePointer<ProcessSerialNumber>!, CFIndex) -> OSStatus](1449783-lsopenitemswithrole.md)
  Opens items with an array of file-system references with a specified role.
- [func LSOpenURLsWithRole(CFArray!, LSRolesMask, UnsafePointer<AEKeyDesc>!, UnsafePointer<LSApplicationParameters>!, UnsafeMutablePointer<ProcessSerialNumber>!, CFIndex) -> OSStatus](1448184-lsopenurlswithrole.md)
  Opens one or more URLs with the specified roles.
- [func LSOpenFSRef(UnsafePointer<FSRef>!, UnsafeMutablePointer<FSRef>!) -> OSStatus](1445663-lsopenfsref.md)
  Opens an item with a file-system reference in the default manner in its preferred app.
- [func LSCopyItemInfoForRef(UnsafePointer<FSRef>!, LSRequestedInfo, UnsafeMutablePointer<LSItemInfoRecord>!) -> OSStatus](1445227-lscopyiteminfoforref.md)
  Obtains requested information about an item with a file-system reference.
- [func LSCopyItemInfoForURL(CFURL!, LSRequestedInfo, UnsafeMutablePointer<LSItemInfoRecord>!) -> OSStatus](1445685-lscopyiteminfoforurl.md)
  Obtains requested information about an item with a URL.
- [func LSCopyDisplayNameForRef(UnsafePointer<FSRef>!, UnsafeMutablePointer<Unmanaged<CFString>?>!) -> OSStatus](1442576-lscopydisplaynameforref.md)
  Obtains the display name for an item with a file-system reference.
- [func LSCopyDisplayNameForURL(CFURL!, UnsafeMutablePointer<Unmanaged<CFString>?>!) -> OSStatus](1446850-lscopydisplaynameforurl.md)
  Obtains the display name for an item with a URL.
- [func LSCopyKindStringForRef(UnsafePointer<FSRef>!, UnsafeMutablePointer<Unmanaged<CFString>?>!) -> OSStatus](1448593-lscopykindstringforref.md)
  Obtains the kind string for an item with a file-system reference.
- [func LSCopyKindStringForURL(CFURL!, UnsafeMutablePointer<Unmanaged<CFString>?>!) -> OSStatus](1447481-lscopykindstringforurl.md)
  Obtains the kind string for an item with a URL.
- [func LSCopyKindStringForTypeInfo(OSType, OSType, CFString!, UnsafeMutablePointer<Unmanaged<CFString>?>!) -> OSStatus](1446207-lscopykindstringfortypeinfo.md)
  Obtains a kind string for items with a specified file type, creator signature, filename extension, or any combination of these characteristics.
- [func LSCopyKindStringForMIMEType(CFString!, UnsafeMutablePointer<Unmanaged<CFString>?>!) -> OSStatus](1442446-lscopykindstringformimetype.md)
  Obtains the kind string for a specified MIME type.
- [func LSCopyItemAttribute(UnsafePointer<FSRef>!, LSRolesMask, CFString!, UnsafeMutablePointer<Unmanaged<CFTypeRef>?>!) -> OSStatus](1445023-lscopyitemattribute.md)
  Obtains the value of an item’s attribute.
- [func LSCopyItemAttributes(UnsafePointer<FSRef>!, LSRolesMask, CFArray!, UnsafeMutablePointer<Unmanaged<CFDictionary>?>!) -> OSStatus](1446078-lscopyitemattributes.md)
  Obtains multiple item attribute values as a dictionary.
- [func LSGetExtensionInfo(Int, UnsafePointer<UniChar>!, UnsafeMutablePointer<Int>!) -> OSStatus](1446043-lsgetextensioninfo.md)
  Obtains the starting index of the extension within a filename.
- [func LSSetExtensionHiddenForRef(UnsafePointer<FSRef>!, Bool) -> OSStatus](1442766-lssetextensionhiddenforref.md)
  Specifies whether to show or hide the filename extension for an item with a file-system reference.
- [func LSSetExtensionHiddenForURL(CFURL!, Bool) -> OSStatus](1443948-lssetextensionhiddenforurl.md)
  Specifies whether to show or hide the filename extension for an item with a URL.
- [func LSRegisterFSRef(UnsafePointer<FSRef>!, Bool) -> OSStatus](1444582-lsregisterfsref.md)
  Registers an app with a file-system reference in the Launch Services database.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1444466-lsopenfromrefspec)*