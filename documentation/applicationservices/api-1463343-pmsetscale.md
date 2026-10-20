# PMSetScale(_:_:)

**Framework**: Application Services  
**Kind**: func  
**Role**: Function

Sets the scaling factor for the page and paper rectangles.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func PMSetScale(_ pageFormat: PMPageFormat, _ scale: Double) -> OSStatus
```

```c
OSStatus PMSetScale(PMPageFormat pageFormat, double scale);
```

#### Return Value

A result code. See [Result Codes](./core_printing.md#1670007).

#### Discussion

You can call the function `PMSetScale` to change the scaling factor that appears when your application invokes the Page Setup dialog.

If you call `PMSetScale` after calling `PMSessionPageSetupDialog`, make sure you call [`PMSessionValidatePageFormat(_:_:_:)`](./api-1459090-pmsessionvalidatepageformat.md) before you call `PMSessionBeginCGDocument` or PMSessionBeginDocument.

If you call this function after initiating a print job, the change is ignored for the current job.

## Parameters

- `pageFormat`: The page format object whose scaling factor you want to set.
- `scale`: The desired scaling factor expressed as a percentage. For example, for 50 percent scaling, pass a value of 50.0; for no scaling, pass 100.0.

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
- [func PMGetAdjustedPageRect(PMPageFormat, UnsafeMutablePointer<PMRect>) -> OSStatus](./api-1461543-pmgetadjustedpagerect.md)
  Obtains the imageable area or page rectangle, taking into account orientation, application drawing resolution, and scaling settings.
- [func PMGetAdjustedPaperRect(PMPageFormat, UnsafeMutablePointer<PMRect>) -> OSStatus](./api-1459167-pmgetadjustedpaperrect.md)
  Obtains the rectangle defining the paper size, taking into account orientation, application drawing resolution, and scaling settings.
- [func PMGetUnadjustedPageRect(PMPageFormat, UnsafeMutablePointer<PMRect>) -> OSStatus](./api-1462944-pmgetunadjustedpagerect.md)
  Obtains the imageable area or page rectangle, unaffected by orientation, resolution, or scaling.
- [func PMGetUnadjustedPaperRect(PMPageFormat, UnsafeMutablePointer<PMRect>) -> OSStatus](./api-1462939-pmgetunadjustedpaperrect.md)
  Obtains the paper rectangle, unaffected by rotation, resolution, or scaling.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1463343-pmsetscale)*