# PMGetPageFormatExtendedData(_:_:_:_:)

**Framework**: Application Services  
**Kind**: func

Obtains extended page format data previously stored by your application.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func PMGetPageFormatExtendedData(_ pageFormat: PMPageFormat, _ dataID: OSType, _ size: UnsafeMutablePointer<UInt32>?, _ extendedData: UnsafeMutableRawPointer?) -> OSStatus
```

#### Return_value

A result code. See [`Result Codes`](core_printing#1670007.md).

#### Discussion

Your application typically needs to call the function `PMGetPageFormatExtendedData` two times in order to retrieve the extended page format data. The first time, pass the constant `kPMDontWantData` in the parameter `extendedData` to obtain the buffer size required for the extended data. Then allocate the buffer and call the function a second time to read the extended data into your buffer.

If you write a printing dialog extension for your application that stores data in the page format object, you use the function `PMGetPageFormatExtendedData` to retrieve the data associated with it. 

## Parameters

- `pageFormat`: The page format object that contains your extended data.
- `dataID`: A 4-character code that identifies your data. This is typically your application’s creator code. If your creator code is outside the ASCII 7-bit character range 0x20–0x7F, you need to use a different 4-character code.
- `size`: A pointer to a value that specifies the size of the buffer you have allocated for the extended page format data. On return, this variable contains the number of bytes read into the buffer or the size of the extended data. You can pass the constant   if you do not need this information. (See   for more information.)
- `extendedData`: A pointer to a buffer to receive the extended data. Pass the constant   if you do not want to read the data. (See   for more information.)

## See Also

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
- [func PMGetScale(PMPageFormat, UnsafeMutablePointer<Double>) -> OSStatus](1458796-pmgetscale.md)
  Obtains the scaling factor currently applied to the page and paper rectangles.
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

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1464455-pmgetpageformatextendeddata)*