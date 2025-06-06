# PMSessionGetDataFromSession(_:_:_:)

**Framework**: Application Services  
**Kind**: func

Obtains application-specific data previously stored in a printing session object.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func PMSessionGetDataFromSession(_ printSession: PMPrintSession, _ key: CFString, _ data: UnsafeMutablePointer<Unmanaged<CFTypeRef>?>) -> OSStatus
```

#### Return_value

A result code. See [`Result Codes`](core_printing#1670007.md).

#### Discussion

You must call this function between the creation and release of a printing session. See the function [`PMCreateSession(_:)`](1463247-pmcreatesession.md).

## Parameters

- `printSession`: The printing session whose data you want to obtain.
- `key`: The key that uniquely identifies the data to be retrieved. You specify this key when you store the data using the function  . 
- `data`: A pointer to your   variable. On return, the variable refers to the data retrieved from the printing session.

## See Also

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
- [func PMSessionSetError(PMPrintSession, OSStatus) -> OSStatus](1460216-pmsessionseterror.md)
  Sets the value of the current result code for the specified printing session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1462964-pmsessiongetdatafromsession)*