# PMSessionSetCurrentPrinter

**Framework**: Application Services  
**Kind**: func

Changes the current printer for a printing session to a printer specified by name.

> **Deprecated**: Use [`PMSessionSetCurrentPMPrinter`](../api-1461096-pmsessionsetcurrentpmprinter.md) instead.

## Declaration

```c
OSStatus PMSessionSetCurrentPrinter (
   PMPrintSession session,
   CFStringRef printerName
);
```

## Return Value

A result code. See [Result Codes](../core_printing.md#1670007).

## Overview

You must call this function between the creation and release of a printing session. See the function [`PMCreateSession`](../api-1463247-pmcreatesession.md).

## Parameters

- `session`: The printing session whose printer you want to change.
- `printerName`: The name of the printer you want to set as the current printer. 

## See Also

### Accessing Data in Printing Session Objects
- [PMSessionGetDataFromSession](../api-1462964-pmsessiongetdatafromsession.md)
  Obtains application-specific data previously stored in a printing session object.
- [PMSessionSetDataInSession](../api-1461902-pmsessionsetdatainsession.md)
  Stores your application-specific data in a printing session object.
- [PMSessionGetCurrentPrinter](../api-1458998-pmsessiongetcurrentprinter.md)
  Obtains the current printer associated with a printing session.
- [PMSessionSetCurrentPMPrinter](../api-1461096-pmsessionsetcurrentpmprinter.md)
  Changes the current printer for a printing session.
- [PMSessionGetDocumentFormatGeneration](./api-1805525-pmsessiongetdocumentformatgenera.md)
  Obtains the spool file formats that can be generated for the specified printing session.
- [PMSessionSetDocumentFormatGeneration](./api-1805527-pmsessionsetdocumentformatgenera.md)
  Requests a specified spool file format and supplies the graphics context type to use for drawing pages within the print loop.
- [PMSessionGetCGGraphicsContext](../api-1461952-pmsessiongetcggraphicscontext.md)
  Obtains the Quartz graphics context for the current page in a printing session.
- [PMSessionGetGraphicsContext](./api-1805529-pmsessiongetgraphicscontext.md)
  Obtains the graphics context for the current page in a printing session.
- [PMSessionError](../api-1460003-pmsessionerror.md)
  Obtains the result code for any error returned by the printing session. 
- [PMSessionSetError](../api-1460216-pmsessionseterror.md)
  Sets the value of the current result code for the specified printing session.
- [PMSessionGeneral](./api-1805530-pmsessiongeneral.md)
  Maintains compatibility with the `PrGeneral` function in the classic Printing Manager.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/core_printing/1805523-pmsessionsetcurrentprinter)*