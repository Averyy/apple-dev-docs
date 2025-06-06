# PMSessionValidatePageFormat(_:_:_:)

**Framework**: Application Services  
**Kind**: func

Updates the values in a page format object and validates them against the current formatting printer.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func PMSessionValidatePageFormat(_ printSession: PMPrintSession, _ pageFormat: PMPageFormat, _ changed: UnsafeMutablePointer<DarwinBoolean>?) -> OSStatus
```

#### Return_value

A result code. See [`Result Codes`](core_printing#1670007.md).

#### Discussion

You must call this function between the creation and release of the printing session. See the function [`PMCreateSession(_:)`](1463247-pmcreatesession.md).

The function `PMSessionValidatePageFormat` validates the page format object against the current formatting printer. The formatting printer is displayed in the Format for pop-up menu in the Page Setup dialog. The default formatting printer is the generic Any Printer. If the page format object contains values that are not valid for the formatting printer, the page format object is set to default values and the `result` parameter is set to `true`.

Validating a page format object also causes calculated fields (such as the adjusted paper and page rectangles) to be updated based on the changed settings (such as resolution, scaling, and page orientation). If the page format object contains values that are valid for the formatting printer but need to be updated, the `result` parameter is set to `false`.

After you call any function that makes changes to a page format object (such as `PMSetOrientation`), you should call the function `PMSessionValidatePageFormat` to validate the page format object before using that object. 

## Parameters

- `printSession`: The printing session for the specified page format object.
- `pageFormat`: The page format object to validate.
- `result`: A pointer to your Boolean variable. On return,   if the function set the page format object to default values; otherwise,  .

## See Also

- [func PMCreatePageFormat(UnsafeMutablePointer<PMPageFormat?>) -> OSStatus](1459485-pmcreatepageformat.md)
  Creates a new page format object.
- [func PMCreatePageFormatWithPMPaper(UnsafeMutablePointer<PMPageFormat?>, PMPaper) -> OSStatus](1459274-pmcreatepageformatwithpmpaper.md)
  Creates a page format object with a specified paper.
- [func PMCopyPageFormat(PMPageFormat, PMPageFormat) -> OSStatus](1464669-pmcopypageformat.md)
  Copies the settings from one page format object into another.
- [func PMSessionDefaultPageFormat(PMPrintSession, PMPageFormat) -> OSStatus](1462217-pmsessiondefaultpageformat.md)
  Assigns default parameter values to a page format object used in the specified printing session.
- [func PMSessionCreatePageFormatList(PMPrintSession, PMPrinter?, UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus](1463985-pmsessioncreatepageformatlist.md)
  Obtains a list of page format objects, each of which describes a paper size available on the specified printer.
- [func PMPageFormatCreateDataRepresentation(PMPageFormat, UnsafeMutablePointer<Unmanaged<CFData>?>, PMDataFormat) -> OSStatus](1464227-pmpageformatcreatedatarepresenta.md)
  Creates a data representation of a page format object.
- [func PMPageFormatCreateWithDataRepresentation(CFData, UnsafeMutablePointer<PMPageFormat?>) -> OSStatus](1462876-pmpageformatcreatewithdatarepres.md)
  Creates a page format object from a data representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1459090-pmsessionvalidatepageformat)*