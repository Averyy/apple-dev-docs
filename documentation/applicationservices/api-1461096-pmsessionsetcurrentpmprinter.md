# PMSessionSetCurrentPMPrinter(_:_:)

**Framework**: Application Services  
**Kind**: func  
**Role**: Function

Changes the current printer for a printing session.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func PMSessionSetCurrentPMPrinter(_ session: PMPrintSession, _ printer: PMPrinter) -> OSStatus
```

```c
OSStatus PMSessionSetCurrentPMPrinter(PMPrintSession session, PMPrinter printer);
```

## Return Value

A result code. See [Result Codes](./core_printing.md#1670007).

## Discussion

You must call this function between the creation and release of a printing session. See the function [`PMCreateSession(_:)`](./api-1463247-pmcreatesession.md).

## Parameters

- `session`: The printing session whose printer you want to change.
- `printer`: The new printer for the printing session.

## See Also

### Accessing Data in Printing Session Objects
- [func PMSessionGetDataFromSession(PMPrintSession, CFString, UnsafeMutablePointer<Unmanaged<CFTypeRef>?>) -> OSStatus](./api-1462964-pmsessiongetdatafromsession.md)
  Obtains application-specific data previously stored in a printing session object.
- [func PMSessionSetDataInSession(PMPrintSession, CFString, CFTypeRef) -> OSStatus](./api-1461902-pmsessionsetdatainsession.md)
  Stores your application-specific data in a printing session object.
- [func PMSessionGetCurrentPrinter(PMPrintSession, UnsafeMutablePointer<PMPrinter?>) -> OSStatus](./api-1458998-pmsessiongetcurrentprinter.md)
  Obtains the current printer associated with a printing session.
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

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1461096-pmsessionsetcurrentpmprinter)*