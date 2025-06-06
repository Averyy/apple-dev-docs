# PMSessionGetCGGraphicsContext(_:_:)

**Framework**: Application Services  
**Kind**: func

Obtains the Quartz graphics context for the current page in a printing session.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func PMSessionGetCGGraphicsContext(_ printSession: PMPrintSession, _ context: UnsafeMutablePointer<Unmanaged<CGContext>?>) -> OSStatus
```

#### Return_value

A result code. See [`Result Codes`](core_printing#1670007.md).

#### Discussion

If you’re using Quartz 2D to draw the content for a print job, after each call to `PMSessionBeginPage` you should call `PMSessionGetCGGraphicsContext` to obtain the Quartz graphics context for the current page. Note that before you can use the function `PMSessionGetCGGraphicsContext`, you must have called `PMSessionBeginCGDocument` or [`PMSessionBeginCGDocumentNoDialog(_:_:_:)`](1460101-pmsessionbegincgdocumentnodialog.md) instead of PMSessionBeginDocument or [`PMSessionBeginDocumentNoDialog`](core_printing/1805538-pmsessionbegindocumentnodialog.md).

## Parameters

- `printSession`: The printing session whose Quartz graphics context you want to obtain.
- `context`: A pointer to your   variable. On return, the variable refers to the Quartz graphics context for the current page in the specified printing session. The context’s origin is at the lower-left corner of the sheet of paper, not the imageable area. You should not release the context without first retaining it. The context is valid only for the current page; you should not retain it beyond the end of the page.

## See Also

- [func PMSessionGetDataFromSession(PMPrintSession, CFString, UnsafeMutablePointer<Unmanaged<CFTypeRef>?>) -> OSStatus](1462964-pmsessiongetdatafromsession.md)
  Obtains application-specific data previously stored in a printing session object.
- [func PMSessionSetDataInSession(PMPrintSession, CFString, CFTypeRef) -> OSStatus](1461902-pmsessionsetdatainsession.md)
  Stores your application-specific data in a printing session object.
- [func PMSessionGetCurrentPrinter(PMPrintSession, UnsafeMutablePointer<PMPrinter?>) -> OSStatus](1458998-pmsessiongetcurrentprinter.md)
  Obtains the current printer associated with a printing session.
- [func PMSessionSetCurrentPMPrinter(PMPrintSession, PMPrinter) -> OSStatus](1461096-pmsessionsetcurrentpmprinter.md)
  Changes the current printer for a printing session.
- [func PMSessionError(PMPrintSession) -> OSStatus](1460003-pmsessionerror.md)
  Obtains the result code for any error returned by the printing session. 
- [func PMSessionSetError(PMPrintSession, OSStatus) -> OSStatus](1460216-pmsessionseterror.md)
  Sets the value of the current result code for the specified printing session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1461952-pmsessiongetcggraphicscontext)*