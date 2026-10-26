# PMSessionSetError(_:_:)

**Framework**: Application Services  
**Kind**: func  
**Role**: Function

Sets the value of the current result code for the specified printing session.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func PMSessionSetError(_ printSession: PMPrintSession, _ printError: OSStatus) -> OSStatus
```

```c
OSStatus PMSessionSetError(PMPrintSession printSession, OSStatus printError);
```

#### Return Value

A result code. See [Result Codes](./core_printing.md#1670007).

#### Discussion

You must call this function between the creation and release of a printing session. See the function [`PMCreateSession(_:)`](./api-1463247-pmcreatesession.md).

You can use this function to terminate a printing session if your application encounters any errors inside the print loop. Typically, this function is used by an application’s idle function. The idle function isn’t called in macOS, so this usage is not available.

## Parameters

- `printSession`: The printing session whose result code you want to set.
- `printError`: The result code you want to set. This result code is returned by the `PMSessionError` function. 

## See Also

### Accessing Data in Printing Session Objects
- [func PMSessionGetDataFromSession(PMPrintSession, CFString, UnsafeMutablePointer<Unmanaged<CFTypeRef>?>) -> OSStatus](./api-1462964-pmsessiongetdatafromsession.md)
  Obtains application-specific data previously stored in a printing session object.
- [func PMSessionSetDataInSession(PMPrintSession, CFString, CFTypeRef) -> OSStatus](./api-1461902-pmsessionsetdatainsession.md)
  Stores your application-specific data in a printing session object.
- [func PMSessionGetCurrentPrinter(PMPrintSession, UnsafeMutablePointer<PMPrinter?>) -> OSStatus](./api-1458998-pmsessiongetcurrentprinter.md)
  Obtains the current printer associated with a printing session.
- [func PMSessionSetCurrentPMPrinter(PMPrintSession, PMPrinter) -> OSStatus](./api-1461096-pmsessionsetcurrentpmprinter.md)
  Changes the current printer for a printing session.
- [func PMSessionGetCGGraphicsContext(PMPrintSession, UnsafeMutablePointer<Unmanaged<CGContext>?>) -> OSStatus](./api-1461952-pmsessiongetcggraphicscontext.md)
  Obtains the Quartz graphics context for the current page in a printing session.
- [func PMSessionError(PMPrintSession) -> OSStatus](./api-1460003-pmsessionerror.md)
  Obtains the result code for any error returned by the printing session. 
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

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1460216-pmsessionseterror)*