# PMGetScale(_:_:)

**Framework**: Application Services  
**Kind**: func

Obtains the scaling factor currently applied to the page and paper rectangles.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func PMGetScale(_ pageFormat: PMPageFormat, _ scale: UnsafeMutablePointer<Double>) -> OSStatus
```

#### Return_value

A result code. See [`Result Codes`](core_printing#1670007.md).

## Parameters

- `pageFormat`: The page format object whose scaling factor you want to obtain.
- `scale`: A pointer to your double-precision variable. On return, the variable contains the scaling factor expressed as a percentage. For example, a value of 100.0 means 100 percent (that is, no scaling); a value of 50.0 means 50 percent scaling.

## See Also

- [func PMGetPageFormatExtendedData(PMPageFormat, OSType, UnsafeMutablePointer<UInt32>?, UnsafeMutableRawPointer?) -> OSStatus](1464455-pmgetpageformatextendeddata.md)
  Obtains extended page format data previously stored by your application.
- [func PMSetPageFormatExtendedData(PMPageFormat, OSType, UInt32, UnsafeMutableRawPointer) -> OSStatus](1463464-pmsetpageformatextendeddata.md)
  Stores your application-specific data in a page format object.
- [func PMGetPageFormatPaper(PMPageFormat, UnsafeMutablePointer<PMPaper?>) -> OSStatus](1461319-pmgetpageformatpaper.md)
  Obtains the paper associated with a page format object.
- [func PMPageFormatGetPrinterID(PMPageFormat, UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus](1462961-pmpageformatgetprinterid.md)
  Obtains the identifier of the formatting printer for a page format object.
- [func PMGetOrientation(PMPageFormat, UnsafeMutablePointer<PMOrientation>) -> OSStatus](1459144-pmgetorientation.md)
  Obtains the current setting for page orientation.
- [func PMSetOrientation(PMPageFormat, PMOrientation, Bool) -> OSStatus](1459016-pmsetorientation.md)
  Sets the page orientation for printing.
- [func PMSetScale(PMPageFormat, Double) -> OSStatus](1463343-pmsetscale.md)
  Sets the scaling factor for the page and paper rectangles.
- [func PMGetAdjustedPageRect(PMPageFormat, UnsafeMutablePointer<PMRect>) -> OSStatus](1461543-pmgetadjustedpagerect.md)
  Obtains the imageable area or page rectangle, taking into account orientation, application drawing resolution, and scaling settings.
- [func PMGetAdjustedPaperRect(PMPageFormat, UnsafeMutablePointer<PMRect>) -> OSStatus](1459167-pmgetadjustedpaperrect.md)
  Obtains the rectangle defining the paper size, taking into account orientation, application drawing resolution, and scaling settings.
- [func PMGetUnadjustedPageRect(PMPageFormat, UnsafeMutablePointer<PMRect>) -> OSStatus](1462944-pmgetunadjustedpagerect.md)
  Obtains the imageable area or page rectangle, unaffected by orientation, resolution, or scaling.
- [func PMGetUnadjustedPaperRect(PMPageFormat, UnsafeMutablePointer<PMRect>) -> OSStatus](1462939-pmgetunadjustedpaperrect.md)
  Obtains the paper rectangle, unaffected by rotation, resolution, or scaling.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1458796-pmgetscale)*