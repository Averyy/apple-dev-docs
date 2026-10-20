# LSCopyDisplayNameForURL(_:_:)

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Obtains the display name for an item with a URL.

**Availability**:
- macOS 10.1+ - Deprecated in 10.11

## Declaration

```swift
func LSCopyDisplayNameForURL(_ inURL: CFURL!, _ outDisplayName: UnsafeMutablePointer<Unmanaged<CFString>?>!) -> OSStatus
```

```c
OSStatus LSCopyDisplayNameForURL(CFURLRef inURL, CFStringRef *outDisplayName);
```

#### Return Value

A result code; see [Result Codes](./launch_services.md#1661359).

#### Discussion

The item’s display name is returned in the form in which it will appear on the user’s screen; it may be localized (for applications and folders), and it excludes the filename extension if the extension is set to be hidden and the Finder preference to always show extensions is not enabled.

##### Version-Notes

Thread-safe since Mac OS version 10.2.

## Parameters

- `inFileURL`: A Core Foundation URL reference designating the item whose display name is requested; see the *CFURL Reference* in the Core Foundation Reference Documentation for a description of the `CFURLRef` data type. The URL must have scheme `file` and contain a valid path to either a file or a directory.
- `outDisplayName`: A pointer to a Core Foundation string object that, on return, will contain the item’s display name; see the *CFString Reference* in the Core Foundation Reference Documentation for a description of the `CFStringRef` data type. You are responsible for releasing this object.

## See Also

### Deprecated Functions
- [func LSGetHandlerOptionsForContentType(CFString!) -> LSHandlerOptions](./api-1445296-lsgethandleroptionsforcontenttyp.md)
  Gets the handler options for the specified content type.
- [func LSSetHandlerOptionsForContentType(CFString!, LSHandlerOptions) -> OSStatus](./api-1447588-lssethandleroptionsforcontenttyp.md)
  Sets the handler option for the specified content type.
- [func LSCopyAllHandlersForURLScheme(CFString) -> Unmanaged<CFArray>?](./api-1443240-lscopyallhandlersforurlscheme.md)
  Locates app bundle identifiers for apps capable of handling the specified URL scheme.
- [func LSCopyDefaultHandlerForURLScheme(CFString) -> Unmanaged<CFString>?](./api-1441725-lscopydefaulthandlerforurlscheme.md)
  Returns the bundle identifier of the user’s preferred default handler for the specified URL scheme.
- [func LSGetApplicationForItem(UnsafePointer<FSRef>!, LSRolesMask, UnsafeMutablePointer<FSRef>!, UnsafeMutablePointer<Unmanaged<CFURL>?>!) -> OSStatus](./api-1446185-lsgetapplicationforitem.md)
  Locates the preferred app for opening an item with a file-system reference.
- [func LSGetApplicationForURL(CFURL!, LSRolesMask, UnsafeMutablePointer<FSRef>!, UnsafeMutablePointer<Unmanaged<CFURL>?>!) -> OSStatus](./api-1445210-lsgetapplicationforurl.md)
  Locates the preferred app for opening an item with a URL.
- [func LSGetApplicationForInfo(OSType, OSType, CFString!, LSRolesMask, UnsafeMutablePointer<FSRef>!, UnsafeMutablePointer<Unmanaged<CFURL>?>!) -> OSStatus](./api-1449928-lsgetapplicationforinfo.md)
  Locates the preferred app for opening items with a specified file type, creator signature, filename extension, or any combination of these characteristics.
- [func LSCopyApplicationForMIMEType(CFString!, LSRolesMask, UnsafeMutablePointer<Unmanaged<CFURL>?>!) -> OSStatus](./api-1448586-lscopyapplicationformimetype.md)
  Locates the preferred app for opening items with a specified MIME type.
- [func LSCanRefAcceptItem(UnsafePointer<FSRef>!, UnsafePointer<FSRef>!, LSRolesMask, LSAcceptanceFlags, UnsafeMutablePointer<DarwinBoolean>!) -> OSStatus](./api-1442183-lscanrefacceptitem.md)
  Tests whether an app can accept (open) an item with a file-system reference.
- [func LSFindApplicationForInfo(OSType, CFString!, CFString!, UnsafeMutablePointer<FSRef>!, UnsafeMutablePointer<Unmanaged<CFURL>?>!) -> OSStatus](./api-1449588-lsfindapplicationforinfo.md)
  Locates an app with a specified creator signature, bundle ID, filename, or any combination of these characteristics.
- [func LSOpenApplication(UnsafePointer<LSApplicationParameters>!, UnsafeMutablePointer<ProcessSerialNumber>!) -> OSStatus](./api-1447930-lsopenapplication.md)
  Launches the specified app.
- [func LSOpenItemsWithRole(UnsafePointer<FSRef>!, CFIndex, LSRolesMask, UnsafePointer<AEKeyDesc>!, UnsafePointer<LSApplicationParameters>!, UnsafeMutablePointer<ProcessSerialNumber>!, CFIndex) -> OSStatus](./api-1449783-lsopenitemswithrole.md)
  Opens items with an array of file-system references with a specified role.
- [func LSOpenURLsWithRole(CFArray!, LSRolesMask, UnsafePointer<AEKeyDesc>!, UnsafePointer<LSApplicationParameters>!, UnsafeMutablePointer<ProcessSerialNumber>!, CFIndex) -> OSStatus](./api-1448184-lsopenurlswithrole.md)
  Opens one or more URLs with the specified roles.
- [func LSOpenFSRef(UnsafePointer<FSRef>!, UnsafeMutablePointer<FSRef>!) -> OSStatus](./api-1445663-lsopenfsref.md)
  Opens an item with a file-system reference in the default manner in its preferred app.
- [func LSOpenFromRefSpec(UnsafePointer<LSLaunchFSRefSpec>!, UnsafeMutablePointer<FSRef>!) -> OSStatus](./api-1444466-lsopenfromrefspec.md)
  Opens one or more items with a file-system reference in either their preferred apps or a designated app.
- [func LSCopyItemInfoForRef(UnsafePointer<FSRef>!, LSRequestedInfo, UnsafeMutablePointer<LSItemInfoRecord>!) -> OSStatus](./api-1445227-lscopyiteminfoforref.md)
  Obtains requested information about an item with a file-system reference.
- [func LSCopyItemInfoForURL(CFURL!, LSRequestedInfo, UnsafeMutablePointer<LSItemInfoRecord>!) -> OSStatus](./api-1445685-lscopyiteminfoforurl.md)
  Obtains requested information about an item with a URL.
- [func LSCopyDisplayNameForRef(UnsafePointer<FSRef>!, UnsafeMutablePointer<Unmanaged<CFString>?>!) -> OSStatus](./api-1442576-lscopydisplaynameforref.md)
  Obtains the display name for an item with a file-system reference.
- [func LSCopyKindStringForRef(UnsafePointer<FSRef>!, UnsafeMutablePointer<Unmanaged<CFString>?>!) -> OSStatus](./api-1448593-lscopykindstringforref.md)
  Obtains the kind string for an item with a file-system reference.
- [func LSCopyKindStringForURL(CFURL!, UnsafeMutablePointer<Unmanaged<CFString>?>!) -> OSStatus](./api-1447481-lscopykindstringforurl.md)
  Obtains the kind string for an item with a URL.
- [func LSCopyKindStringForTypeInfo(OSType, OSType, CFString!, UnsafeMutablePointer<Unmanaged<CFString>?>!) -> OSStatus](./api-1446207-lscopykindstringfortypeinfo.md)
  Obtains a kind string for items with a specified file type, creator signature, filename extension, or any combination of these characteristics.
- [func LSCopyKindStringForMIMEType(CFString!, UnsafeMutablePointer<Unmanaged<CFString>?>!) -> OSStatus](./api-1442446-lscopykindstringformimetype.md)
  Obtains the kind string for a specified MIME type.
- [func LSCopyItemAttribute(UnsafePointer<FSRef>!, LSRolesMask, CFString!, UnsafeMutablePointer<Unmanaged<CFTypeRef>?>!) -> OSStatus](./api-1445023-lscopyitemattribute.md)
  Obtains the value of an item’s attribute.
- [func LSCopyItemAttributes(UnsafePointer<FSRef>!, LSRolesMask, CFArray!, UnsafeMutablePointer<Unmanaged<CFDictionary>?>!) -> OSStatus](./api-1446078-lscopyitemattributes.md)
  Obtains multiple item attribute values as a dictionary.
- [func LSGetExtensionInfo(Int, UnsafePointer<UniChar>!, UnsafeMutablePointer<Int>!) -> OSStatus](./api-1446043-lsgetextensioninfo.md)
  Obtains the starting index of the extension within a filename.
- [func LSSetExtensionHiddenForRef(UnsafePointer<FSRef>!, Bool) -> OSStatus](./api-1442766-lssetextensionhiddenforref.md)
  Specifies whether to show or hide the filename extension for an item with a file-system reference.
- [func LSSetExtensionHiddenForURL(CFURL!, Bool) -> OSStatus](./api-1443948-lssetextensionhiddenforurl.md)
  Specifies whether to show or hide the filename extension for an item with a URL.
- [func LSRegisterFSRef(UnsafePointer<FSRef>!, Bool) -> OSStatus](./api-1444582-lsregisterfsref.md)
  Registers an app with a file-system reference in the Launch Services database.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1446850-lscopydisplaynameforurl)*