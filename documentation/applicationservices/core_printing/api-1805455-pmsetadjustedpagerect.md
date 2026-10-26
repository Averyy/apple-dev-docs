# PMSetAdjustedPageRect

**Framework**: Application Services  
**Kind**: func

Requests a particular page size, adjusted for the current rotation, resolution, or scaling settings.

> **Deprecated**: To set a particular paper size and margins, obtain or create a [`PMPaper`](../pmpaper.md) object and call [`PMCreatePageFormatWithPMPaper`](../api-1459274-pmcreatepageformatwithpmpaper.md).

## Declaration

```c
OSStatus PMSetAdjustedPageRect (
   PMPageFormat pageFormat,
   const PMRect *pageRect
);
```

#### Return Value

A result code. See [Result Codes](../core_printing.md#1670007).

#### Overview

This function is not recommended. You should call this function only if your application provides desktop publishing and the Page Setup dialog does not provide sufficient control. Typically, such applications display their own specialized document format dialog.

If you decide to use this function, you must call the function between the creation and release of a printing session. See the function [`PMCreateSession`](../api-1463247-pmcreatesession.md). You can use `PMSetAdjustedPageRect` to set a drawing rectangle without going through the Page Setup dialog or calling other page format accessor functions. This function allows an application to specify the dimensions of the imageable area into which it draws. 

If you call this function after initiating a print job, the change is ignored for the current job.

## Parameters

- `pageFormat`: The page format object whose page rectangle you want to set.
- `pageRect`: A pointer to your [PMRect](./pmrect.md) data structure that specifies the desired size of the page rectangle, in points. The top-left coordinates should be (0,0). See Supporting Printing in Your Carbon Application for more information on page and paper rectangles.

## See Also

### Accessing Data in Page Format Objects
- [PMGetPageFormatExtendedData](../api-1464455-pmgetpageformatextendeddata.md)
  Obtains extended page format data previously stored by your application.
- [PMSetPageFormatExtendedData](../api-1463464-pmsetpageformatextendeddata.md)
  Stores your application-specific data in a page format object.
- [PMGetPageFormatPaper](../api-1461319-pmgetpageformatpaper.md)
  Obtains the paper associated with a page format object.
- [PMPageFormatGetPrinterID](../api-1462961-pmpageformatgetprinterid.md)
  Obtains the identifier of the formatting printer for a page format object.
- [PMGetOrientation](../api-1459144-pmgetorientation.md)
  Obtains the current setting for page orientation.
- [PMSetOrientation](../api-1459016-pmsetorientation.md)
  Sets the page orientation for printing.
- [PMGetResolution](./api-1805451-pmgetresolution.md)
  Obtains the current application’s drawing resolution.
- [PMSetResolution](./api-1805452-pmsetresolution.md)
  Sets the application drawing resolution.
- [PMGetScale](../api-1458796-pmgetscale.md)
  Obtains the scaling factor currently applied to the page and paper rectangles.
- [PMSetScale](../api-1463343-pmsetscale.md)
  Sets the scaling factor for the page and paper rectangles.
- [PMGetAdjustedPageRect](../api-1461543-pmgetadjustedpagerect.md)
  Obtains the imageable area or page rectangle, taking into account orientation, application drawing resolution, and scaling settings.
- [PMGetAdjustedPaperRect](../api-1459167-pmgetadjustedpaperrect.md)
  Obtains the rectangle defining the paper size, taking into account orientation, application drawing resolution, and scaling settings.
- [PMGetUnadjustedPageRect](../api-1462944-pmgetunadjustedpagerect.md)
  Obtains the imageable area or page rectangle, unaffected by orientation, resolution, or scaling.
- [PMGetUnadjustedPaperRect](../api-1462939-pmgetunadjustedpaperrect.md)
  Obtains the paper rectangle, unaffected by rotation, resolution, or scaling.
- [PMSetUnadjustedPaperRect](./api-1805459-pmsetunadjustedpaperrect.md)
  Requests a particular paper size, unaffected by rotation, resolution, or scaling.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/core_printing/1805455-pmsetadjustedpagerect)*