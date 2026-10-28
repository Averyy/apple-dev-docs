# PMGetAdjustedPaperRect(_:_:)

**Framework**: Application Services  
**Kind**: func  
**Role**: Function

Obtains the rectangle defining the paper size, taking into account orientation, application drawing resolution, and scaling settings.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func PMGetAdjustedPaperRect(_ pageFormat: PMPageFormat, _ paperRect: UnsafeMutablePointer<PMRect>) -> OSStatus
```

```c
OSStatus PMGetAdjustedPaperRect(PMPageFormat pageFormat, PMRect *paperRect);
```

## Return Value

A result code. See [Result Codes](./core_printing.md#1670007).

## Discussion

Before using this function, you must call the function [`PMSessionValidatePageFormat(_:_:_:)`](./api-1459090-pmsessionvalidatepageformat.md) to ensure that the values for the adjusted paper rectangle correctly account for scaling, rotation, and application resolution settings.

## Parameters

- `pageFormat`: The page format object whose adjusted paper rectangle you want to obtain.
- `paperRect`: A pointer to your [PMRect](./core_printing/pmrect.md) structure. On return, the structure describes the current paper size, in points, taking into account scaling, rotation, and application resolution settings. The coordinates of the upper-left corner of the paper rectangle are specified relative to the page rectangle. The coordinates of the upper-left corner of the page rectangle are always (0,0), which means the coordinates of the upper-left corner of the paper rectangle are always negative or (0,0). See Supporting Printing in Your Carbon Application for more information on page and paper rectangles.

## See Also

### Accessing Data in Page Format Objects
- [func PMGetPageFormatExtendedData(PMPageFormat, OSType, UnsafeMutablePointer<UInt32>?, UnsafeMutableRawPointer?) -> OSStatus](./api-1464455-pmgetpageformatextendeddata.md)
  Obtains extended page format data previously stored by your application.
- [func PMSetPageFormatExtendedData(PMPageFormat, OSType, UInt32, UnsafeMutableRawPointer) -> OSStatus](./api-1463464-pmsetpageformatextendeddata.md)
  Stores your application-specific data in a page format object.
- [func PMGetPageFormatPaper(PMPageFormat, UnsafeMutablePointer<PMPaper?>) -> OSStatus](./api-1461319-pmgetpageformatpaper.md)
  Obtains the paper associated with a page format object.
- [func PMPageFormatGetPrinterID(PMPageFormat, UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus](./api-1462961-pmpageformatgetprinterid.md)
  Obtains the identifier of the formatting printer for a page format object.
- [func PMGetOrientation(PMPageFormat, UnsafeMutablePointer<PMOrientation>) -> OSStatus](./api-1459144-pmgetorientation.md)
  Obtains the current setting for page orientation.
- [func PMSetOrientation(PMPageFormat, PMOrientation, Bool) -> OSStatus](./api-1459016-pmsetorientation.md)
  Sets the page orientation for printing.
- [func PMGetScale(PMPageFormat, UnsafeMutablePointer<Double>) -> OSStatus](./api-1458796-pmgetscale.md)
  Obtains the scaling factor currently applied to the page and paper rectangles.
- [func PMSetScale(PMPageFormat, Double) -> OSStatus](./api-1463343-pmsetscale.md)
  Sets the scaling factor for the page and paper rectangles.
- [func PMGetAdjustedPageRect(PMPageFormat, UnsafeMutablePointer<PMRect>) -> OSStatus](./api-1461543-pmgetadjustedpagerect.md)
  Obtains the imageable area or page rectangle, taking into account orientation, application drawing resolution, and scaling settings.
- [func PMGetUnadjustedPageRect(PMPageFormat, UnsafeMutablePointer<PMRect>) -> OSStatus](./api-1462944-pmgetunadjustedpagerect.md)
  Obtains the imageable area or page rectangle, unaffected by orientation, resolution, or scaling.
- [func PMGetUnadjustedPaperRect(PMPageFormat, UnsafeMutablePointer<PMRect>) -> OSStatus](./api-1462939-pmgetunadjustedpaperrect.md)
  Obtains the paper rectangle, unaffected by rotation, resolution, or scaling.
- [PMGetResolution](./core_printing/api-1805451-pmgetresolution.md)
  Obtains the current application’s drawing resolution.
- [PMSetResolution](./core_printing/api-1805452-pmsetresolution.md)
  Sets the application drawing resolution.
- [PMSetAdjustedPageRect](./core_printing/api-1805455-pmsetadjustedpagerect.md)
  Requests a particular page size, adjusted for the current rotation, resolution, or scaling settings.
- [PMSetUnadjustedPaperRect](./core_printing/api-1805459-pmsetunadjustedpaperrect.md)
  Requests a particular paper size, unaffected by rotation, resolution, or scaling.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1459167-pmgetadjustedpaperrect)*