# PMCreatePageFormat(_:)

**Framework**: Application Services  
**Kind**: func  
**Role**: Function

Creates a new page format object.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func PMCreatePageFormat(_ pageFormat: UnsafeMutablePointer<PMPageFormat?>) -> OSStatus
```

```c
OSStatus PMCreatePageFormat(PMPageFormat  _Nullable *pageFormat);
```

## Return Value

A result code. See [Result Codes](./core_printing.md#1670007).

## Discussion

This function allocates memory for a new page format object in your application’s memory space and sets its reference count to 1. The new page format object is empty and unusable until you call [`PMSessionDefaultPageFormat(_:_:)`](./api-1462217-pmsessiondefaultpageformat.md) or [`PMCopyPageFormat(_:_:)`](./api-1464669-pmcopypageformat.md).

## Parameters

- `pageFormat`: A pointer to your [`PMPageFormat`](./pmpageformat.md) variable. On return, the variable refers to a new page format object. You are responsible for releasing the page format object with the function [`PMRelease(_:)`](./api-1461402-pmrelease.md).

## See Also

### Creating and Using Page Format Objects
- [func PMCreatePageFormatWithPMPaper(UnsafeMutablePointer<PMPageFormat?>, PMPaper) -> OSStatus](./api-1459274-pmcreatepageformatwithpmpaper.md)
  Creates a page format object with a specified paper.
- [func PMCopyPageFormat(PMPageFormat, PMPageFormat) -> OSStatus](./api-1464669-pmcopypageformat.md)
  Copies the settings from one page format object into another.
- [func PMSessionDefaultPageFormat(PMPrintSession, PMPageFormat) -> OSStatus](./api-1462217-pmsessiondefaultpageformat.md)
  Assigns default parameter values to a page format object used in the specified printing session.
- [func PMSessionValidatePageFormat(PMPrintSession, PMPageFormat, UnsafeMutablePointer<DarwinBoolean>?) -> OSStatus](./api-1459090-pmsessionvalidatepageformat.md)
  Updates the values in a page format object and validates them against the current formatting printer.
- [func PMSessionCreatePageFormatList(PMPrintSession, PMPrinter?, UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus](./api-1463985-pmsessioncreatepageformatlist.md)
  Obtains a list of page format objects, each of which describes a paper size available on the specified printer.
- [func PMPageFormatCreateDataRepresentation(PMPageFormat, UnsafeMutablePointer<Unmanaged<CFData>?>, PMDataFormat) -> OSStatus](./api-1464227-pmpageformatcreatedatarepresenta.md)
  Creates a data representation of a page format object.
- [func PMPageFormatCreateWithDataRepresentation(CFData, UnsafeMutablePointer<PMPageFormat?>) -> OSStatus](./api-1462876-pmpageformatcreatewithdatarepres.md)
  Creates a page format object from a data representation.
- [PMFlattenPageFormat](./core_printing/api-1805421-pmflattenpageformat.md)
  Flattens a page format object into a Memory Manager handle for storage in a user document.
- [PMFlattenPageFormatToCFData](./core_printing/api-1805425-pmflattenpageformattocfdata.md)
  Flattens a page format object into a Core Foundation data object for storage in a user document.
- [PMFlattenPageFormatToURL](./core_printing/api-1805429-pmflattenpageformattourl.md)
  Flattens a page format object into a file for storage in a user document.
- [PMUnflattenPageFormat](./core_printing/api-1805434-pmunflattenpageformat.md)
  Rebuilds a page format object from a Memory Manager handle that contains flattened page format data.
- [PMUnflattenPageFormatWithCFData](./core_printing/api-1805439-pmunflattenpageformatwithcfdata.md)
  Rebuilds a page format object from a Core Foundation data object that contains flattened page format data.
- [PMUnflattenPageFormatWithURL](./core_printing/api-1805441-pmunflattenpageformatwithurl.md)
  Rebuilds a page format object from a file system URL that contains flattened page format data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1459485-pmcreatepageformat)*