# PMSetResolution

**Framework**: Application Services  
**Kind**: func

Sets the application drawing resolution.

> **Deprecated**: Draw using Quartz 2D and call [`CGContextScaleCTM`](../../CoreGraphics/cgcontext/scaleby%28x,y%29.md) instead.

## Declaration

```c
OSStatus PMSetResolution (
   PMPageFormat pageFormat,
   const PMResolution *res
);
```

#### Return Value

A result code. See [Result Codes](../core_printing.md#1670007).

#### Overview

If you call this function after initiating a print job, the change is ignored for the current job.

##### Special Considerations

This function was needed in the past because QuickDraw uses integer coordinates and has no notion of scaling coordinate systems. For Quartz drawing, this function is obsolete. To change the resolution, draw with fractional coordinates or scale the coordinate system and draw with integer coordinates.

## Parameters

- `pageFormat`: The page format object whose drawing resolution you want to set.
- `res`: A pointer to a structure of type [PMResolution](./pmresolution.md) that specifies the desired drawing resolution for your application. You should specify the best resolution for your data. The printing system handles the mapping between the resolution you specify and the printer resolution.

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
- [PMGetScale](../api-1458796-pmgetscale.md)
  Obtains the scaling factor currently applied to the page and paper rectangles.
- [PMSetScale](../api-1463343-pmsetscale.md)
  Sets the scaling factor for the page and paper rectangles.
- [PMGetAdjustedPageRect](../api-1461543-pmgetadjustedpagerect.md)
  Obtains the imageable area or page rectangle, taking into account orientation, application drawing resolution, and scaling settings.
- [PMSetAdjustedPageRect](./api-1805455-pmsetadjustedpagerect.md)
  Requests a particular page size, adjusted for the current rotation, resolution, or scaling settings.
- [PMGetAdjustedPaperRect](../api-1459167-pmgetadjustedpaperrect.md)
  Obtains the rectangle defining the paper size, taking into account orientation, application drawing resolution, and scaling settings.
- [PMGetUnadjustedPageRect](../api-1462944-pmgetunadjustedpagerect.md)
  Obtains the imageable area or page rectangle, unaffected by orientation, resolution, or scaling.
- [PMGetUnadjustedPaperRect](../api-1462939-pmgetunadjustedpaperrect.md)
  Obtains the paper rectangle, unaffected by rotation, resolution, or scaling.
- [PMSetUnadjustedPaperRect](./api-1805459-pmsetunadjustedpaperrect.md)
  Requests a particular paper size, unaffected by rotation, resolution, or scaling.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/core_printing/1805452-pmsetresolution)*