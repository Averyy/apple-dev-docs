# PMPageFormatCreateWithDataRepresentation(_:_:)

**Framework**: Application Services  
**Kind**: func  
**Role**: Function

Creates a page format object from a data representation.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func PMPageFormatCreateWithDataRepresentation(_ data: CFData, _ pageFormat: UnsafeMutablePointer<PMPageFormat?>) -> OSStatus
```

```c
OSStatus PMPageFormatCreateWithDataRepresentation(CFDataRef data, PMPageFormat  _Nullable *pageFormat);
```

#### Return Value

A result code. See [Result Codes](./core_printing.md#1670007).

#### Discussion

This function is typically used to convert a data representation stored in a user document back into a page format object. For information about creating a Core Foundation data object from raw data, see `CFData`.

After calling this function, you should call the function [`PMSessionValidatePageFormat(_:_:_:)`](./api-1459090-pmsessionvalidatepageformat.md) to make sure the page format object contains valid values.

## Parameters

- `data`: The data representation of a page format object. The data representation must have been previously created with the function [`PMPageFormatCreateDataRepresentation(_:_:_:)`](./api-1464227-pmpageformatcreatedatarepresenta.md).
- `pageFormat`: A pointer to your [`PMPageFormat`](./pmpageformat.md) variable. On return, the variable refers to a new page format object that contains the information stored in the specified data object. You are responsible for releasing the page format object with the function [`PMRelease(_:)`](./api-1461402-pmrelease.md).

## See Also

### Creating and Using Page Format Objects
- [func PMCreatePageFormat(UnsafeMutablePointer<PMPageFormat?>) -> OSStatus](./api-1459485-pmcreatepageformat.md)
  Creates a new page format object.
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

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1462876-pmpageformatcreatewithdatarepres)*