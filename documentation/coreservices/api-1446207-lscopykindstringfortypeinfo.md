# LSCopyKindStringForTypeInfo(_:_:_:_:)

**Framework**: Core Services  
**Kind**: func

Obtains a kind string for items with a specified file type, creator signature, filename extension, or any combination of these characteristics.

**Availability**:
- macOS 10.2+ - Deprecated in 10.10

## Declaration

```swift
func LSCopyKindStringForTypeInfo(_ inType: OSType, _ inCreator: OSType, _ inExtension: CFString!, _ outKindString: UnsafeMutablePointer<Unmanaged<CFString>?>!) -> OSStatus
```

#### Return_value

A result code; see [`Result Codes`](launch_services#1661359.md).

#### Discussion

This function obtains the kind string that most closely describes items having the specified characteristics. It is useful when you want to display the kind string for a document you do not yet have (such as an email attachment).

You can request any combination of one, two, or all three of the characteristics specified by the `inType`, `inCreator`, and `inExtension` parameters; at least one of these characteristics must be supplied. The kind string (which may be localized) is obtained from the preferred application for opening such items, if one is found in the Launch Services database; otherwise, a more generic kind string is chosen. For example, the kind string might be `FrameMaker Document`, or just `Document` if no suitable application is found. 

Note that since the choice of a preferred application is subject to any document binding preferences the user may have set, the kind string will not necessarily be obtained from the default application that matches the specified creator signature (if any), but may instead be taken from a user-specified application that overrides the default. For example, if the user has specified that files of type `'PDF'` and creator `'ACRO'` should be opened in the Preview application rather than in Acrobat, the kind string for this combination of characteristics will be that defined for `'PDF '` files by Preview and not by Acrobat.

##### 1676004

Thread-safe since Mac OS version 10.2

## Parameters

- `inType`: The file type to consider. Comparison of file types is case-sensitive. Pass   if the items’ file type is unimportant.
- `inCreator`: The creator signature to consider. Comparison of creator signatures is case-sensitive. Pass   if the items’ creator signature is unimportant.
- `inExtension`: A Core Foundation string object specifying the filename extension to consider; see the   in the Core Foundation Reference Documentation for a description of the   data type. Comparison of filename extensions is case-insensitive. Pass   if the items’ filename extension is unimportant.
- `outKindString`: A pointer to a Core Foundation string object that, on return, will contain the requested kind string; see the   in the Core Foundation Reference Documentation for a description of the   data type. You are responsible for releasing this object.

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
- [func LSOpenFromRefSpec(UnsafePointer<LSLaunchFSRefSpec>!, UnsafeMutablePointer<FSRef>!) -> OSStatus](1444466-lsopenfromrefspec.md)
  Opens one or more items with a file-system reference in either their preferred apps or a designated app.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1446207-lscopykindstringfortypeinfo)*