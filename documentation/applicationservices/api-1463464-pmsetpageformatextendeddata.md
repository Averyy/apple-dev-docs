# PMSetPageFormatExtendedData(_:_:_:_:)

**Framework**: Application Services  
**Kind**: func  
**Role**: Function

Stores your application-specific data in a page format object.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func PMSetPageFormatExtendedData(_ pageFormat: PMPageFormat, _ dataID: OSType, _ size: UInt32, _ extendedData: UnsafeMutableRawPointer) -> OSStatus
```

```c
OSStatus PMSetPageFormatExtendedData(PMPageFormat pageFormat, OSType dataID, UInt32 size, void *extendedData);
```

#### Return Value

A result code. See [Result Codes](./core_printing.md#1670007).

#### Discussion

You can retrieve the data you store with the function `PMSetPageFormatExtendedData` by calling the function `PMGetPageFormatExtendedData`.

## Parameters

- `pageFormat`: The page format object in which to store your extended data.
- `dataID`: A 4-character code that identifies your data. This is typically your application’s creator code. If your creator code is outside the ASCII 7-bit character range 0x20–0x7F, you need to use a different 4-character code.
- `size`: The size, in bytes, of the data to be stored in the page format object.
- `extendedData`: A pointer to the application-specific data you want to store in the page format object.

## See Also

### Accessing Data in Page Format Objects
- [func PMGetPageFormatExtendedData(PMPageFormat, OSType, UnsafeMutablePointer<UInt32>?, UnsafeMutableRawPointer?) -> OSStatus](./api-1464455-pmgetpageformatextendeddata.md)
  Obtains extended page format data previously stored by your application.
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
- [func PMGetAdjustedPaperRect(PMPageFormat, UnsafeMutablePointer<PMRect>) -> OSStatus](./api-1459167-pmgetadjustedpaperrect.md)
  Obtains the rectangle defining the paper size, taking into account orientation, application drawing resolution, and scaling settings.
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

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1463464-pmsetpageformatextendeddata)*