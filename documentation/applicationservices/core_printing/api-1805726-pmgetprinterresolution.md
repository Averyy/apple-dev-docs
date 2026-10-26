# PMGetPrinterResolution

**Framework**: Application Services  
**Kind**: func

Obtains the resolution setting for the current printer according to the tag parameter.

> **Deprecated**: Use [`PMPrinterGetPrinterResolutionCount`](../api-1462004-pmprintergetprinterresolutioncou.md) and [`PMPrinterGetIndexedPrinterResolution`](../api-1464490-pmprintergetindexedprinterresolu.md) to examine the available printer resolutions.

## Declaration

```c
OSStatus PMGetPrinterResolution (
   PMTag tag,
   PMResolution *res
);
```

#### Return Value

A result code. . The result code `kPMNotImplemented` indicates that the printer driver does not support multiple resolution settings.

#### Overview

Valid after calling `PMBegin`.

The following resolution tag constants are recognized:

- **`kPMMinRange`**: The minimum resolution supported by the printer. 
- **`kPMMaxRange`**: The maximum resolution supported by the printer. 
- **`kPMMinSquareResolution`**: The minimum resolution setting for which the horizontal and vertical resolutions are equal. 
- **`kPMMaxSquareResolution`**: The maximum resolution setting for which the horizontal and vertical resolutions are equal. 
- **`kPMDefaultResolution`**: The default resolution setting for the printer (typically 72 dpi). 

## Parameters

- `tag`: Specifies the kind of resolution information required. 
- `res`: The printer resolution setting. 

## See Also

### Legacy Core Printing Functions
- [PMBegin](./api-1805644-pmbegin.md)
  Prepares Core Printing for use.
- [PMConvertOldPrintRecord](./api-1805650-pmconvertoldprintrecord.md)
  Creates a new `PMPageFormat` object and a new `PMPrintSettings` object from a print record created by the classic Printing Manager.
- [PMDefaultPageFormat](./api-1805655-pmdefaultpageformat.md)
  Assigns default parameter values to an existing `PMPageFormat` object, for the current printer.
- [PMDefaultPrintSettings](./api-1805658-pmdefaultprintsettings.md)
  Assigns default parameter values to a `PMPrintSettings` object.
- [PMDisableColorSync](./api-1805663-pmdisablecolorsync.md)
  Disables ColorSync color matching for the current page.
- [PMDisposePageFormat](./api-1805665-pmdisposepageformat.md)
  Releases memory previously allocated for a `PMPageFormat` object.
- [PMDisposePrintSettings](./api-1805670-pmdisposeprintsettings.md)
  Releases memory previously allocated for a `PMPrintSettings` object.
- [PMEnableColorSync](./api-1805675-pmenablecolorsync.md)
  Enables ColorSync color matching for the current page.
- [PMEnd](./api-1805679-pmend.md)
  Closes Core Printing and releases its allocated memory.
- [PMError](./api-1805683-pmerror.md)
  Obtains the result code from the last printing function called by your application.
- [PMGeneral](./api-1805686-pmgeneral.md)
  Maintains compatibility with the `PrGeneral` function in the classic Printing Manager.
- [PMGetDestination](./api-1805692-pmgetdestination.md)
  Obtains the output destination of a print job.
- [PMGetDriverCreator](./api-1805697-pmgetdrivercreator.md)
  Obtains the creator of the driver associated with the current printer.
- [PMGetDriverReleaseInfo](./api-1805701-pmgetdriverreleaseinfo.md)
  Obtains release information for the driver associated with the current printer.
- [PMGetGrafPtr](./api-1805707-pmgetgrafptr.md)
  Obtains the printing port from an opaque printing context.
- [PMGetIndexedPrinterResolution](./api-1805712-pmgetindexedprinterresolution.md)
  Obtains a resolution setting based on an index into the range of settings supported by the current printer.
- [PMGetJobName](./api-1805714-pmgetjobname.md)
  Obtains the name of the print job.
- [PMGetLanguageInfo](./api-1805718-pmgetlanguageinfo.md)
  Obtains information about the current printer’s imaging language.
- [PMGetPhysicalPageSize](./api-1805720-pmgetphysicalpagesize.md)
  Obtains the size of the imageable area in points, unaffected by rotation, resolution, or scaling.
- [PMGetPhysicalPaperSize](./api-1805722-pmgetphysicalpapersize.md)
  Obtains the size of the paper in points, unaffected by rotation, resolution, or scaling.
- [PMGetPrinterResolutionCount](./api-1805729-pmgetprinterresolutioncount.md)
  Obtains the number of resolution settings supported by the current printer.
- [PMIsPostScriptDriver](./api-1805734-pmispostscriptdriver.md)
  Reports whether the current printer driver supports the PostScript language.
- [PMNewPageFormat](./api-1805737-pmnewpageformat.md)
  Creates a new `PMPageFormat` object.
- [PMNewPrintSettings](./api-1805743-pmnewprintsettings.md)
  Creates a new `PMPrintSettings` object.
- [PMMakeOldPrintRecord](./api-1805745-pmmakeoldprintrecord.md)
  Creates an old-style print record from a `PMPageFormat` and a `PMPrintSettings` object.
- [PMPostScriptBegin](./api-1805751-pmpostscriptbegin.md)
  Puts the current driver into PostScript mode, ready to accept PostScript data instead of QuickDraw data.
- [PMPostScriptData](./api-1805754-pmpostscriptdata.md)
  Passes PostScript data, referenced by a pointer, to the current printer driver.
- [PMPostScriptEnd](./api-1805759-pmpostscriptend.md)
  Restores the current driver to QuickDraw mode, ready to accept QuickDraw data instead of PostScript data.
- [PMPostScriptFile](./api-1805762-pmpostscriptfile.md)
  Passes PostScript data, contained in a file, to the current printer driver.
- [PMPostScriptHandle](./api-1805767-pmpostscripthandle.md)
  Passes PostScript data, referenced by a handle, to the current printer driver.
- [PMSessionGetDocumentFormatSupported](./api-1805770-pmsessiongetdocumentformatsuppor.md)
  Obtains the spool file formats that are accepted by the current printer driver.
- [PMSessionIsDocumentFormatSupported](./api-1805774-pmsessionisdocumentformatsupport.md)
  Reports whether the current printer driver supports a specified spool file format.
- [PMGetColorMode](./api-1805779-pmgetcolormode.md)
  Obtains the color mode for the print job.
- [PMSetColorMode](./api-1805783-pmsetcolormode.md)
  Sets the desired color mode for the print job.
- [PMSetError](./api-1805784-pmseterror.md)
  Sets the value of the current result code.
- [PMSetIdleProc](./api-1805789-pmsetidleproc.md)
  Installs an idle callback function in your print loop.
- [PMSetJobName](./api-1805792-pmsetjobname.md)
  Specifies the name of the print job.
- [PMSetPhysicalPaperSize](./api-1805794-pmsetphysicalpapersize.md)
  Requests a particular paper size, unaffected by rotation, resolution, or scaling.
- [PMValidatePageFormat](./api-1805800-pmvalidatepageformat.md)
  Obtains a valid `PMPageFormat` object.
- [PMValidatePrintSettings](./api-1805802-pmvalidateprintsettings.md)
  Obtains a valid `PMPrintSettings` object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/core_printing/1805726-pmgetprinterresolution)*