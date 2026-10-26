# kLSMultipleSessionsNotSupportedErr

**Framework**: Core Services  
**Kind**: econst  
**Role**: Enumeration Case

The requested app can’t run simultaneously in two different user sessions.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.3+

## Declaration

```c
kLSMultipleSessionsNotSupportedErr = -10829
```

## See Also

### Result Codes
- [kLSAppInTrashErr](./klsappintrasherr.md)
  The app can’t run because it’s inside a Trash folder.
- [kLSUnknownErr](./klsunknownerr.md)
  An unknown error has occurred.
- [kLSNotAnApplicationErr](./klsnotanapplicationerr.md)
  The item for registration is not an app.
- [kLSDataUnavailableErr](./klsdataunavailableerr.md)
  Data of the desired type is not available (for example, there is no kind string).
- [kLSApplicationNotFoundErr](./klsapplicationnotfounderr.md)
  No app in the Launch Services database matches the input criteria.
- [kLSDataErr](./klsdataerr.md)
  Improper data structure.
- [kLSLaunchInProgressErr](./klslaunchinprogresserr.md)
  A launch of the app is already in progress.
- [kLSServerCommunicationErr](./klsservercommunicationerr.md)
  There is a problem communicating with the server process that maintains the Launch Services database. 
- [kLSCannotSetInfoErr](./klscannotsetinfoerr.md)
  The system can’t hide the filename extension.
- [kLSIncompatibleSystemVersionErr](./klsincompatiblesystemversionerr.md)
  The requested app can’t run on the current macOS version.
- [kLSNoLaunchPermissionErr](./klsnolaunchpermissionerr.md)
  The user doesn’t have permission to launch the app on a managed network.
- [kLSNoExecutableErr](./klsnoexecutableerr.md)
  The executable file is missing or has an unusable format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/3074489-anonymous/klsmultiplesessionsnotsupportederr)*