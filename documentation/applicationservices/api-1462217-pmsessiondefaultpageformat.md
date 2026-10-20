# PMSessionDefaultPageFormat(_:_:)

**Framework**: Application Services  
**Kind**: func  
**Role**: Function

Assigns default parameter values to a page format object used in the specified printing session.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func PMSessionDefaultPageFormat(_ printSession: PMPrintSession, _ pageFormat: PMPageFormat) -> OSStatus
```

```c
OSStatus PMSessionDefaultPageFormat(PMPrintSession printSession, PMPageFormat pageFormat);
```

#### Return Value

A result code. See [Result Codes](./core_printing.md#1670007).

#### Discussion

You must call the function `PMSessionDefaultPageFormat` between the creation and release of the printing session. See the function [`PMCreateSession(_:)`](./api-1463247-pmcreatesession.md).

## Parameters

- `printSession`: The printing session for the specified page format object.
- `pageFormat`: The page format object to which you want to assign default values.

## See Also

### Creating and Using Page Format Objects
- [func PMCreatePageFormat(UnsafeMutablePointer<PMPageFormat?>) -> OSStatus](./api-1459485-pmcreatepageformat.md)
  Creates a new page format object.
- [func PMCreatePageFormatWithPMPaper(UnsafeMutablePointer<PMPageFormat?>, PMPaper) -> OSStatus](./api-1459274-pmcreatepageformatwithpmpaper.md)
  Creates a page format object with a specified paper.
- [func PMCopyPageFormat(PMPageFormat, PMPageFormat) -> OSStatus](./api-1464669-pmcopypageformat.md)
  Copies the settings from one page format object into another.
- [func PMSessionValidatePageFormat(PMPrintSession, PMPageFormat, UnsafeMutablePointer<DarwinBoolean>?) -> OSStatus](./api-1459090-pmsessionvalidatepageformat.md)
  Updates the values in a page format object and validates them against the current formatting printer.
- [func PMSessionCreatePageFormatList(PMPrintSession, PMPrinter?, UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus](./api-1463985-pmsessioncreatepageformatlist.md)
  Obtains a list of page format objects, each of which describes a paper size available on the specified printer.
- [func PMPageFormatCreateDataRepresentation(PMPageFormat, UnsafeMutablePointer<Unmanaged<CFData>?>, PMDataFormat) -> OSStatus](./api-1464227-pmpageformatcreatedatarepresenta.md)
  Creates a data representation of a page format object.
- [func PMPageFormatCreateWithDataRepresentation(CFData, UnsafeMutablePointer<PMPageFormat?>) -> OSStatus](./api-1462876-pmpageformatcreatewithdatarepres.md)
  Creates a page format object from a data representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1462217-pmsessiondefaultpageformat)*