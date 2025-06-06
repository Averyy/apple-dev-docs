# PMCreatePageFormat(_:)

**Framework**: Application Services  
**Kind**: func

Creates a new page format object.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func PMCreatePageFormat(_ pageFormat: UnsafeMutablePointer<PMPageFormat?>) -> OSStatus
```

#### Return_value

A result code. See [`Result Codes`](core_printing#1670007.md).

#### Discussion

This function allocates memory for a new page format object in your application’s memory space and sets its reference count to 1. The new page format object is empty and unusable until you call [`PMSessionDefaultPageFormat(_:_:)`](1462217-pmsessiondefaultpageformat.md) or [`PMCopyPageFormat(_:_:)`](1464669-pmcopypageformat.md).

## Parameters

- `pageFormat`: A pointer to your   variable. On return, the variable refers to a new page format object. You are responsible for releasing the page format object with the function  .

## See Also

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
- [func PMPageFormatCreateWithDataRepresentation(CFData, UnsafeMutablePointer<PMPageFormat?>) -> OSStatus](1462876-pmpageformatcreatewithdatarepres.md)
  Creates a page format object from a data representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1459485-pmcreatepageformat)*