# kLSNoExecutableErr

**Framework**: Core Services  
**Kind**: data

The executable file is missing or has an unusable format.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.3+

## Declaration

```swift
var kLSNoExecutableErr: OSStatus { get }
```

## See Also

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
- [var kLSMultipleSessionsNotSupportedErr: OSStatus](klsmultiplesessionsnotsupportederr.md)
  The requested app can’t run simultaneously in two different user sessions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/klsnoexecutableerr)*