# Launch Services

**Framework**: Core Services

Launch and open documents in other apps from your current app process.

#### Overview

macOS Launch Services is an API that enables a running app to open other apps or their document files, similar to the Finder or the Dock. Using Launch Services, an app can perform such tasks as:

- Open (launch or activate) another app
- Open a document or a URL in another app
- Identify the preferred app for opening a document or URL
- Register information about the kinds of document files and URLs an app can open
- Obtain information for displaying a file or URL on the screen, such as its icon, display name, and kind string
- Maintain and update the contents of the Recent Items menu

Launch Services eliminates apps having to query the Finder to open an app, document, or URL for them. The macOS Finder itself uses Launch Services to perform such tasks. Because the Finder performs no additional processing beyond calling Launch Services, any client using Launch Services for these purposes behaves identically to the Finder.

## Topics

### Locating an App
- [func LSCopyDefaultApplicationURLForURL(CFURL, LSRolesMask, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Unmanaged<CFURL>?](1448824-lscopydefaultapplicationurlforur.md)
  Returns the app that opens an item.
- [func LSCopyDefaultApplicationURLForContentType(CFString, LSRolesMask, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Unmanaged<CFURL>?](1447734-lscopydefaultapplicationurlforco.md)
  Returns the app that opens a content type.
- [func LSCopyApplicationURLsForURL(CFURL, LSRolesMask) -> Unmanaged<CFArray>?](1445148-lscopyapplicationurlsforurl.md)
  Locates all known apps suitable for opening an item for the specified URL.
- [func LSCanURLAcceptURL(CFURL, CFURL, LSRolesMask, LSAcceptanceFlags, UnsafeMutablePointer<DarwinBoolean>) -> OSStatus](1441854-lscanurlaccepturl.md)
  Tests whether an app can accept (open) an item for a URL.
- [func LSCopyApplicationURLsForBundleIdentifier(CFString, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Unmanaged<CFArray>?](1449290-lscopyapplicationurlsforbundleid.md)
  Locates all URLs for apps that correspond to the specified bundle identifier.
### Opening Items
- [func LSOpenCFURLRef(CFURL, UnsafeMutablePointer<Unmanaged<CFURL>?>?) -> OSStatus](1442850-lsopencfurlref.md)
  Opens an item for a URL in the default manner in its preferred app.
- [func LSOpenFromURLSpec(UnsafePointer<LSLaunchURLSpec>, UnsafeMutablePointer<Unmanaged<CFURL>?>?) -> OSStatus](1441986-lsopenfromurlspec.md)
  Opens one or more items for a URL in the preferred apps or a designated app.
- [struct LSLaunchURLSpec](lslaunchurlspec.md)
  The specification for launching an app, opening items, or both, along with related information.
- [class LSSharedFileList](lssharedfilelist.md)
  A persistent list of file-system objects.
- [class LSSharedFileListItem](lssharedfilelistitem.md)
  A file-system object in the shared file list.
### Registering an App
- [func LSRegisterURL(CFURL, Bool) -> OSStatus](1446350-lsregisterurl.md)
  Registers an app, using a URL, in the Launch Services database.
### Working with Role Handlers
- [func LSCopyAllRoleHandlersForContentType(CFString, LSRolesMask) -> Unmanaged<CFArray>?](1448020-lscopyallrolehandlersforcontentt.md)
  Locates an array of bundle identifiers for apps capable of handling a specified content type with the specified roles.
- [func LSCopyDefaultRoleHandlerForContentType(CFString, LSRolesMask) -> Unmanaged<CFString>?](1449868-lscopydefaultrolehandlerforconte.md)
  Returns the bundle identifier of the user’s preferred default handler for the specified content type with the specified role.
- [func LSSetDefaultRoleHandlerForContentType(CFString, LSRolesMask, CFString) -> OSStatus](1444955-lssetdefaultrolehandlerforconten.md)
  Sets the user’s preferred default handler for the specified content type in the specified roles.
- [func LSSetDefaultHandlerForURLScheme(CFString, CFString) -> OSStatus](1447760-lssetdefaulthandlerforurlscheme.md)
  Sets the user’s preferred default handler for the specified URL scheme.
- [struct LSRolesMask](lsrolesmask.md)
  The specification that sets the desired role or roles for an app to claim for an item or a family of items.
### Understanding the Quarantine Properties Dictionary
- [let kLSQuarantineAgentBundleIdentifierKey: CFString](klsquarantineagentbundleidentifierkey.md)
  The bundle identifier of the quarantining agent.
- [let kLSQuarantineAgentNameKey: CFString](klsquarantineagentnamekey.md)
  The app name of the quarantining agent.
- [let kLSQuarantineTimeStampKey: CFString](klsquarantinetimestampkey.md)
  The date and time of the item’s quarantine.
- [let kLSQuarantineTypeKey: CFString](klsquarantinetypekey.md)
  A symbolic string identifying the reason for the quarantine.
- [let kLSQuarantineDataURLKey: CFString](klsquarantinedataurlkey.md)
  The actual URL of the quarantined item.
- [let kLSQuarantineOriginURLKey: CFString](klsquarantineoriginurlkey.md)
  The URL of the resource originally hosting the quarantined item.
### Identifying the Quarantine Type
- [let kLSQuarantineTypeCalendarEventAttachment: CFString](klsquarantinetypecalendareventattachment.md)
  The type when the data is an attachment from a calendar event.
- [let kLSQuarantineTypeEmailAttachment: CFString](klsquarantinetypeemailattachment.md)
  The type when the data is an attachment from an email message.
- [let kLSQuarantineTypeInstantMessageAttachment: CFString](klsquarantinetypeinstantmessageattachment.md)
  The type when the data is an attachment from a message.
- [let kLSQuarantineTypeOtherAttachment: CFString](klsquarantinetypeotherattachment.md)
  The type when the data is an attachment from a generic source.
- [let kLSQuarantineTypeOtherDownload: CFString](klsquarantinetypeotherdownload.md)
  The type when the data is from a download.
- [let kLSQuarantineTypeWebDownload: CFString](klsquarantinetypewebdownload.md)
  The type when the data is from a website download.
### Constants
- [struct LSLaunchFlags](lslaunchflags.md)
  The specification for launching an app.
- [struct LSAcceptanceFlags](lsacceptanceflags.md)
  The specification that determines whether an app can accept (open) an item.
- [struct LSItemInfoFlags](lsiteminfoflags.md)
  The specification that provides information about an item.
- [struct LSHandlerOptions](lshandleroptions.md)
  The specification that controls the selection of handlers.
- [struct LSRequestedInfo](lsrequestedinfo.md)
  The specification that controls which information to obtain about an item.
- [Unknown Type or Creator](launch_services/1469201-unknown_type_or_creator.md)
  Represents an unknown file type or creator.
### Result Codes
- [var kLSAppInTrashErr: OSStatus](klsappintrasherr.md)
  The app can’t run because it’s inside a Trash folder.
- [var kLSUnknownErr: OSStatus](klsunknownerr.md)
  An unknown error has occurred.
- [var kLSNotAnApplicationErr: OSStatus](klsnotanapplicationerr.md)
  The item for registration is not an app.
- [var kLSDataUnavailableErr: OSStatus](klsdataunavailableerr.md)
  Data of the desired type is not available (for example, there is no kind string).
- [var kLSApplicationNotFoundErr: OSStatus](klsapplicationnotfounderr.md)
  No app in the Launch Services database matches the input criteria.
- [var kLSDataErr: OSStatus](klsdataerr.md)
  Improper data structure.
- [var kLSLaunchInProgressErr: OSStatus](klslaunchinprogresserr.md)
  A launch of the app is already in progress.
- [var kLSServerCommunicationErr: OSStatus](klsservercommunicationerr.md)
  There is a problem communicating with the server process that maintains the Launch Services database. 
- [var kLSCannotSetInfoErr: OSStatus](klscannotsetinfoerr.md)
  The system can’t hide the filename extension.
- [var kLSIncompatibleSystemVersionErr: OSStatus](klsincompatiblesystemversionerr.md)
  The requested app can’t run on the current macOS version.
- [var kLSNoLaunchPermissionErr: OSStatus](klsnolaunchpermissionerr.md)
  The user doesn’t have permission to launch the app on a managed network.
- [var kLSNoExecutableErr: OSStatus](klsnoexecutableerr.md)
  The executable file is missing or has an unusable format.
- [var kLSMultipleSessionsNotSupportedErr: OSStatus](klsmultiplesessionsnotsupportederr.md)
  The requested app can’t run simultaneously in two different user sessions.
### Deprecated
- [Deprecated Symbols](launch_services/deprecated_symbols.md)
  Apple has deprecated these symbols and no longer recommends using them.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/launch_services)*