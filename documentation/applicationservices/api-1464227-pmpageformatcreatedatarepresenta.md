# PMPageFormatCreateDataRepresentation(_:_:_:)

**Framework**: Application Services  
**Kind**: func

Creates a data representation of a page format object.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func PMPageFormatCreateDataRepresentation(_ pageFormat: PMPageFormat, _ data: UnsafeMutablePointer<Unmanaged<CFData>?>, _ format: PMDataFormat) -> OSStatus
```

#### Return_value

A result code. See [`Result Codes`](core_printing#1670007.md).

#### Discussion

This function is typically used to convert a page format object into a data representation suitable for storage in a user document. For information about using a Core Foundation data object, see `CFData`.

Before calling this function, you should call the function [`PMSessionValidatePageFormat(_:_:_:)`](1459090-pmsessionvalidatepageformat.md) to make sure the page format object contains valid values.

## Parameters

- `pageFormat`: The page format object to convert.
- `data`: A pointer to your   variable. On return, the variable refers to a new Core Foundation data object that contains a representation of the specified page format object in the specified data format. You are responsible for releasing the data object.
- `format`: See   for a full description of these formats.

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
- [func PMPageFormatCreateWithDataRepresentation(CFData, UnsafeMutablePointer<PMPageFormat?>) -> OSStatus](1462876-pmpageformatcreatewithdatarepres.md)
  Creates a page format object from a data representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1464227-pmpageformatcreatedatarepresenta)*