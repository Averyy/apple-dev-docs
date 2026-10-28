# PMSessionSetPSInjectionData

**Framework**: Application Services  
**Kind**: func

Specifies a set of PostScript code injection points and the PostScript data to be injected.

> **Deprecated**: Use [`PMPrinterPrintWithFile`](../api-1464600-pmprinterprintwithfile.md) or [`PMPrinterPrintWithProvider`](../api-1461110-pmprinterprintwithprovider.md) instead.

## Declaration

```c
OSStatus PMSessionSetPSInjectionData (
   PMPrintSession printSession,
   PMPrintSettings printSettings,
   CFArrayRef injectionDictArray
);
```

## Return Value

A result code. See [Result Codes](../core_printing.md#1670007). The result code `kPMInvalidParameter` is returned if the `injectionDictArray` object contains any invalid entries. The result code `kPMInvalidPrintSession` is returned if the document format has not been set to `kPMDocumentFormatPICTPS` for the specified printing session.

## Overview

You must call this function between the creation and release of a printing session. See the function [`PMCreateSession`](../api-1463247-pmcreatesession.md). Before calling `PMSessionSetPSInjectionData`, your application must set the document format of the printing session to `kPMDocumentFormatPICTPS` using the function [PMSessionSetDocumentFormatGeneration](./api-1805527-pmsessionsetdocumentformatgenera.md).

For applications that require extensive control over PostScript code generation, the function `PMSessionSetPSInjectionData` provides the ability to insert PostScript code into specified places in the print stream. It is intended for use by desktop publishing applications for which functions such as `PMSessionPostScriptData` do not provide sufficient control.

You specify the injection points by creating an array of `CFDictionary` entries. Each dictionary consists of key-value pairs in which the key specifies where to inject the PostScript and the value specifies the PostScript data you want to inject. The function verifies that the `injectionDictArray` parameter is properly formed, and returns the `kPMInvalidParameter` result code if the array does not contain valid entries.

If you call the function `PMSessionSetPSInjectionData` a second time for a given print settings object, the injection points you specified previously are replaced with the new injection points.

## Parameters

- `printSession`: The current printing session.
- `printSettings`: The print settings object in which to place the specified injection points.
- `injectionDictArray`: A reference to a Core Foundation array that contains one or more Core Foundation dictionary (`CFDictionary`) entries. Each dictionary entry specifies PostScript injection data you want inserted at a specific point in the print stream. See [PostScript Injection Dictionary Keys](./postscript_injection_dictionary_keys.md) for a description of the constants you can use as keys for these dictionary entries. 

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
- [PMSessionPostScriptEnd](./api-1805601-pmsessionpostscriptend.md)
  Restores the current driver to QuickDraw mode, ready to accept QuickDraw data instead of PostScript data.
- [PMSessionPostScriptFile](./api-1805604-pmsessionpostscriptfile.md)
  Passes the PostScript data, contained in a file, to the current printer driver.
- [PMSessionPostScriptHandle](./api-1805605-pmsessionpostscripthandle.md)
  Passes the PostScript data, referenced by a Memory Manager handle, to the current printer driver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/core_printing/1805610-pmsessionsetpsinjectiondata)*