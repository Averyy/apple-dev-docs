# PMSessionSetCurrentPMPrinter(_:_:)

**Framework**: Application Services  
**Kind**: func

Changes the current printer for a printing session.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func PMSessionSetCurrentPMPrinter(_ session: PMPrintSession, _ printer: PMPrinter) -> OSStatus
```

#### Return_value

A result code. See [`Result Codes`](core_printing#1670007.md).

#### Discussion

You must call this function between the creation and release of a printing session. See the function [`PMCreateSession(_:)`](1463247-pmcreatesession.md).

## Parameters

- `session`: The printing session whose printer you want to change.
- `printer`: The new printer for the printing session.

## See Also

- [func PMSessionGetDataFromSession(PMPrintSession, CFString, UnsafeMutablePointer<Unmanaged<CFTypeRef>?>) -> OSStatus](1462964-pmsessiongetdatafromsession.md)
  Obtains application-specific data previously stored in a printing session object.
- [func PMSessionSetDataInSession(PMPrintSession, CFString, CFTypeRef) -> OSStatus](1461902-pmsessionsetdatainsession.md)
  Stores your application-specific data in a printing session object.
- [func PMSessionGetCurrentPrinter(PMPrintSession, UnsafeMutablePointer<PMPrinter?>) -> OSStatus](1458998-pmsessiongetcurrentprinter.md)
  Obtains the current printer associated with a printing session.
- [func PMSessionGetCGGraphicsContext(PMPrintSession, UnsafeMutablePointer<Unmanaged<CGContext>?>) -> OSStatus](1461952-pmsessiongetcggraphicscontext.md)
  Obtains the Quartz graphics context for the current page in a printing session.
- [func PMSessionError(PMPrintSession) -> OSStatus](1460003-pmsessionerror.md)
  Obtains the result code for any error returned by the printing session. 
- [func PMSessionSetError(PMPrintSession, OSStatus) -> OSStatus](1460216-pmsessionseterror.md)
  Sets the value of the current result code for the specified printing session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1461096-pmsessionsetcurrentpmprinter)*