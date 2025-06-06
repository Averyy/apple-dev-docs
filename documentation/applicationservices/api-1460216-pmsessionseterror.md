# PMSessionSetError(_:_:)

**Framework**: Application Services  
**Kind**: func

Sets the value of the current result code for the specified printing session.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func PMSessionSetError(_ printSession: PMPrintSession, _ printError: OSStatus) -> OSStatus
```

#### Return_value

A result code. See [`Result Codes`](core_printing#1670007.md).

#### Discussion

You must call this function between the creation and release of a printing session. See the function [`PMCreateSession(_:)`](1463247-pmcreatesession.md).

You can use this function to terminate a printing session if your application encounters any errors inside the print loop. Typically, this function is used by an application’s idle function. The idle function isn’t called in macOS, so this usage is not available.

## Parameters

- `printSession`: The printing session whose result code you want to set.
- `printError`: The result code you want to set. This result code is returned by the   function. 

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
- [func PMSessionError(PMPrintSession) -> OSStatus](1460003-pmsessionerror.md)
  Obtains the result code for any error returned by the printing session. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1460216-pmsessionseterror)*