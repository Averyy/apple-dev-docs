# PMSessionDefaultPageFormat(_:_:)

**Framework**: Application Services  
**Kind**: func

Assigns default parameter values to a page format object used in the specified printing session.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func PMSessionDefaultPageFormat(_ printSession: PMPrintSession, _ pageFormat: PMPageFormat) -> OSStatus
```

#### Return_value

A result code. See [`Result Codes`](core_printing#1670007.md).

#### Discussion

You must call the function `PMSessionDefaultPageFormat` between the creation and release of the printing session. See the function [`PMCreateSession(_:)`](1463247-pmcreatesession.md).

## Parameters

- `printSession`: The printing session for the specified page format object.
- `pageFormat`: The page format object to which you want to assign default values.

## See Also

- [func PMCreatePageFormat(UnsafeMutablePointer<PMPageFormat?>) -> OSStatus](1459485-pmcreatepageformat.md)
  Creates a new page format object.
- [func PMCreatePageFormatWithPMPaper(UnsafeMutablePointer<PMPageFormat?>, PMPaper) -> OSStatus](1459274-pmcreatepageformatwithpmpaper.md)
  Creates a page format object with a specified paper.
- [func PMCopyPageFormat(PMPageFormat, PMPageFormat) -> OSStatus](1464669-pmcopypageformat.md)
  Copies the settings from one page format object into another.
- [func PMSessionValidatePageFormat(PMPrintSession, PMPageFormat, UnsafeMutablePointer<DarwinBoolean>?) -> OSStatus](1459090-pmsessionvalidatepageformat.md)
  Updates the values in a page format object and validates them against the current formatting printer.
- [func PMSessionCreatePageFormatList(PMPrintSession, PMPrinter?, UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus](1463985-pmsessioncreatepageformatlist.md)
  Obtains a list of page format objects, each of which describes a paper size available on the specified printer.
- [func PMPageFormatCreateDataRepresentation(PMPageFormat, UnsafeMutablePointer<Unmanaged<CFData>?>, PMDataFormat) -> OSStatus](1464227-pmpageformatcreatedatarepresenta.md)
  Creates a data representation of a page format object.
- [func PMPageFormatCreateWithDataRepresentation(CFData, UnsafeMutablePointer<PMPageFormat?>) -> OSStatus](1462876-pmpageformatcreatewithdatarepres.md)
  Creates a page format object from a data representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1462217-pmsessiondefaultpageformat)*