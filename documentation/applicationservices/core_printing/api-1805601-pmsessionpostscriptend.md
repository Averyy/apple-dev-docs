# PMSessionPostScriptEnd

**Framework**: Application Services  
**Kind**: func

Restores the current driver to QuickDraw mode, ready to accept QuickDraw data instead of PostScript data.

> **Deprecated**: Use [`PMPrinterPrintWithFile`](../api-1464600-pmprinterprintwithfile.md), [`PMPrinterPrintWithProvider`](../api-1461110-pmprinterprintwithprovider.md), or [`PMCGImageCreateWithEPSDataProvider`](../api-1462361-pmcgimagecreatewithepsdataprovid.md) instead.

## Declaration

```c
OSStatus PMSessionPostScriptEnd (
   PMPrintSession printSession
);
```

## Return Value

A result code. See [Result Codes](../core_printing.md#1670007).

## Overview

You must call this function between the creation and release of a printing session. See the function [`PMCreateSession`](../api-1463247-pmcreatesession.md). You must also call this function with the scope of calls to the functions `PMSessionBeginPage` and `PMSessionEndPage`.

You call the function `PMSessionPostScriptEnd` to complete a PostScript block started with `PMSessionPostScriptBegin`. The function `PMSessionPostScriptEnd` is not useful unless the current port is the printing port and the document format is PICT + PS. 

### Special Considerations

The PICT + PS spool file format is not available on Intel-based systems.

## Parameters

- `printSession`: The current printing session.

## See Also

### Printing with PostScript Data
- [PMCGImageCreateWithEPSDataProvider](../api-1462361-pmcgimagecreatewithepsdataprovid.md)
  Creates an image that references both the PostScript contents of EPS data and a preview (proxy) image for the data.
- [PMPrinterWritePostScriptToURL](../api-1459729-pmprinterwritepostscripttourl.md)
  Converts an input file of the specified MIME type to printer-ready PostScript for a destination printer.
- [PMSessionPostScriptBegin](./api-1805591-pmsessionpostscriptbegin.md)
  Puts the current printer driver into PostScript mode, ready to accept PostScript data instead of QuickDraw data.
- [PMSessionPostScriptData](./api-1805595-pmsessionpostscriptdata.md)
  Passes PostScript data, referenced by a pointer, to the current printer driver.
- [PMSessionPostScriptFile](./api-1805604-pmsessionpostscriptfile.md)
  Passes the PostScript data, contained in a file, to the current printer driver.
- [PMSessionPostScriptHandle](./api-1805605-pmsessionpostscripthandle.md)
  Passes the PostScript data, referenced by a Memory Manager handle, to the current printer driver.
- [PMSessionSetPSInjectionData](./api-1805610-pmsessionsetpsinjectiondata.md)
  Specifies a set of PostScript code injection points and the PostScript data to be injected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/core_printing/1805601-pmsessionpostscriptend)*