# PMSessionGetCurrentPrinter(_:_:)

**Framework**: Application Services  
**Kind**: func  
**Role**: Function

Obtains the current printer associated with a printing session.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func PMSessionGetCurrentPrinter(_ printSession: PMPrintSession, _ currentPrinter: UnsafeMutablePointer<PMPrinter?>) -> OSStatus
```

```c
OSStatus PMSessionGetCurrentPrinter(PMPrintSession printSession, PMPrinter  _Nullable *currentPrinter);
```

## Return Value

A result code. See [Result Codes](./core_printing.md#1670007).

## Discussion

You must call this function between the creation and release of a printing session. See the function [`PMCreateSession(_:)`](./api-1463247-pmcreatesession.md).

## Parameters

- `printSession`: The printing session whose printer you want to obtain.
- `currentPrinter`: A pointer to your [`PMPrinter`](./pmprinter.md) variable. On return, the variable refers to the printer associated with the specified printing session. The printer object is valid as long as the printing session is valid or the current printer hasn’t changed. You should not release this object without first retaining it.

## See Also

### Accessing Data in Printing Session Objects
- [func PMSessionGetDataFromSession(PMPrintSession, CFString, UnsafeMutablePointer<Unmanaged<CFTypeRef>?>) -> OSStatus](./api-1462964-pmsessiongetdatafromsession.md)
  Obtains application-specific data previously stored in a printing session object.
- [func PMSessionSetDataInSession(PMPrintSession, CFString, CFTypeRef) -> OSStatus](./api-1461902-pmsessionsetdatainsession.md)
  Stores your application-specific data in a printing session object.
- [func PMSessionSetCurrentPMPrinter(PMPrintSession, PMPrinter) -> OSStatus](./api-1461096-pmsessionsetcurrentpmprinter.md)
  Changes the current printer for a printing session.
- [func PMSessionGetCGGraphicsContext(PMPrintSession, UnsafeMutablePointer<Unmanaged<CGContext>?>) -> OSStatus](./api-1461952-pmsessiongetcggraphicscontext.md)
  Obtains the Quartz graphics context for the current page in a printing session.
- [func PMSessionError(PMPrintSession) -> OSStatus](./api-1460003-pmsessionerror.md)
  Obtains the result code for any error returned by the printing session. 
- [func PMSessionSetError(PMPrintSession, OSStatus) -> OSStatus](./api-1460216-pmsessionseterror.md)
  Sets the value of the current result code for the specified printing session.
- [PMSessionSetCurrentPrinter](./core_printing/api-1805523-pmsessionsetcurrentprinter.md)
  Changes the current printer for a printing session to a printer specified by name.
- [PMSessionGetDocumentFormatGeneration](./core_printing/api-1805525-pmsessiongetdocumentformatgenera.md)
  Obtains the spool file formats that can be generated for the specified printing session.
- [PMSessionSetDocumentFormatGeneration](./core_printing/api-1805527-pmsessionsetdocumentformatgenera.md)
  Requests a specified spool file format and supplies the graphics context type to use for drawing pages within the print loop.
- [PMSessionGetGraphicsContext](./core_printing/api-1805529-pmsessiongetgraphicscontext.md)
  Obtains the graphics context for the current page in a printing session.
- [PMSessionGeneral](./core_printing/api-1805530-pmsessiongeneral.md)
  Maintains compatibility with the `PrGeneral` function in the classic Printing Manager.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1458998-pmsessiongetcurrentprinter)*