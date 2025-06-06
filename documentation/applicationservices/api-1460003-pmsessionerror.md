# PMSessionError(_:)

**Framework**: Application Services  
**Kind**: func

Obtains the result code for any error returned by the printing session. 

**Availability**:
- macOS 10.0+

## Declaration

```swift
func PMSessionError(_ printSession: PMPrintSession) -> OSStatus
```

#### Return_value

A result code. See [`Result Codes`](core_printing#1670007.md). The constant `kPMCancel` indicates the user canceled the current print job.

#### Discussion

You must call this function between the creation and release of a printing session. See the function [`PMCreateSession(_:)`](1463247-pmcreatesession.md).

The `PMSessionError` function returns the last printing session error, not the last error from a printing function (`PMxxx`). Because most printing functions return a result code, the `PMSessionError` function is not required for general error checking. However, you can use `PMSessionError` in your print loop to determine if the user cancels the current print job or if any other errors occur during printing that are not explicitly returned by one of the other calls. For example, if the user clicks the Cancel button in the status dialog or presses Command-period on the keyboard, this function returns the constant `kPMCancel`. If this or any other error is encountered during the print loop, your application should call the appropriate functions (for example, `PMSessionEndPage` and `PMSessionEndDocument`) to exit the print loop before your application reports the error.

## Parameters

- `printSession`: The printing session whose last error you want to obtain.

## See Also

- [func PMSessionGetDataFromSession(PMPrintSession, CFString, UnsafeMutablePointer<Unmanaged<CFTypeRef>?>) -> OSStatus](1462964-pmsessiongetdatafromsession.md)
  Obtains application-specific data previously stored in a printing session object.
- [func PMSessionSetDataInSession(PMPrintSession, CFString, CFTypeRef) -> OSStatus](1461902-pmsessionsetdatainsession.md)
  Stores your application-specific data in a printing session object.
- [func PMSessionGetCurrentPrinter(PMPrintSession, UnsafeMutablePointer<PMPrinter?>) -> OSStatus](1458998-pmsessiongetcurrentprinter.md)
  Obtains the current printer associated with a printing session.
- [func PMSessionSetCurrentPMPrinter(PMPrintSession, PMPrinter) -> OSStatus](1461096-pmsessionsetcurrentpmprinter.md)
  Changes the current printer for a printing session.
- [func PMSessionGetCGGraphicsContext(PMPrintSession, UnsafeMutablePointer<Unmanaged<CGContext>?>) -> OSStatus](1461952-pmsessiongetcggraphicscontext.md)
  Obtains the Quartz graphics context for the current page in a printing session.
- [func PMSessionSetError(PMPrintSession, OSStatus) -> OSStatus](1460216-pmsessionseterror.md)
  Sets the value of the current result code for the specified printing session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1460003-pmsessionerror)*