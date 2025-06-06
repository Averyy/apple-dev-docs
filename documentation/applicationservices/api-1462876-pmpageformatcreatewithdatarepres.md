# PMPageFormatCreateWithDataRepresentation(_:_:)

**Framework**: Application Services  
**Kind**: func

Creates a page format object from a data representation.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func PMPageFormatCreateWithDataRepresentation(_ data: CFData, _ pageFormat: UnsafeMutablePointer<PMPageFormat?>) -> OSStatus
```

#### Return_value

A result code. See [`Result Codes`](core_printing#1670007.md).

#### Discussion

This function is typically used to convert a data representation stored in a user document back into a page format object. For information about creating a Core Foundation data object from raw data, see `CFData`.

After calling this function, you should call the function [`PMSessionValidatePageFormat(_:_:_:)`](1459090-pmsessionvalidatepageformat.md) to make sure the page format object contains valid values.

## Parameters

- `data`: The data representation of a page format object. The data representation must have been previously created with the function  .
- `pageFormat`: A pointer to your   variable. On return, the variable refers to a new page format object that contains the information stored in the specified data object. You are responsible for releasing the page format object with the function  .

## See Also

- [func PMCreatePageFormat(UnsafeMutablePointer<PMPageFormat?>) -> OSStatus](1459485-pmcreatepageformat.md)
  Creates a new page format object.
- [func PMCreatePageFormatWithPMPaper(UnsafeMutablePointer<PMPageFormat?>, PMPaper) -> OSStatus](1459274-pmcreatepageformatwithpmpaper.md)
  Creates a page format object with a specified paper.
- [func PMCopyPageFormat(PMPageFormat, PMPageFormat) -> OSStatus](1464669-pmcopypageformat.md)
  Copies the settings from one page format object into another.
- [func PMSessionDefaultPageFormat(PMPrintSession, PMPageFormat) -> OSStatus](1462217-pmsessiondefaultpageformat.md)
  Assigns default parameter values to a page format object used in the specified printing session.
- [func PMSessionValidatePageFormat(PMPrintSession, PMPageFormat, UnsafeMutablePointer<DarwinBoolean>?) -> OSStatus](1459090-pmsessionvalidatepageformat.md)
  Updates the values in a page format object and validates them against the current formatting printer.
- [func PMSessionCreatePageFormatList(PMPrintSession, PMPrinter?, UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus](1463985-pmsessioncreatepageformatlist.md)
  Obtains a list of page format objects, each of which describes a paper size available on the specified printer.
- [func PMPageFormatCreateDataRepresentation(PMPageFormat, UnsafeMutablePointer<Unmanaged<CFData>?>, PMDataFormat) -> OSStatus](1464227-pmpageformatcreatedatarepresenta.md)
  Creates a data representation of a page format object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1462876-pmpageformatcreatewithdatarepres)*