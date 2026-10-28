# PMUnflattenPageFormatWithURL

**Framework**: Application Services  
**Kind**: func

Rebuilds a page format object from a file system URL that contains flattened page format data.

> **Deprecated**: Instead read the data into a CFData object and use [`PMPageFormatCreateWithDataRepresentation`](../api-1462876-pmpageformatcreatewithdatarepres.md).

## Declaration

```c
OSStatus PMUnflattenPageFormatWithURL (
   CFURLRef flattenFileURL,
   PMPageFormat *pageFormat
);
```

## Return Value

A result code. See [Result Codes](../core_printing.md#1670007).

## Parameters

- `flattenFileURL`: A Core Foundation URL that specifies a file containing a flattened representation of a page format object.
- `pageFormat`: A pointer to your [`PMPageFormat`](../pmpageformat.md) variable. On return, the variable refers to a page format object that is rebuilt from the specified file. You are responsible for releasing the page format object with the function [`PMRelease`](../api-1461402-pmrelease.md).

## See Also

### Creating and Using Page Format Objects
- [PMCreatePageFormat](../api-1459485-pmcreatepageformat.md)
  Creates a new page format object.
- [PMCreatePageFormatWithPMPaper](../api-1459274-pmcreatepageformatwithpmpaper.md)
  Creates a page format object with a specified paper.
- [PMCopyPageFormat](../api-1464669-pmcopypageformat.md)
  Copies the settings from one page format object into another.
- [PMSessionDefaultPageFormat](../api-1462217-pmsessiondefaultpageformat.md)
  Assigns default parameter values to a page format object used in the specified printing session.
- [PMSessionValidatePageFormat](../api-1459090-pmsessionvalidatepageformat.md)
  Updates the values in a page format object and validates them against the current formatting printer.
- [PMSessionCreatePageFormatList](../api-1463985-pmsessioncreatepageformatlist.md)
  Obtains a list of page format objects, each of which describes a paper size available on the specified printer.
- [PMPageFormatCreateDataRepresentation](../api-1464227-pmpageformatcreatedatarepresenta.md)
  Creates a data representation of a page format object.
- [PMPageFormatCreateWithDataRepresentation](../api-1462876-pmpageformatcreatewithdatarepres.md)
  Creates a page format object from a data representation.
- [PMFlattenPageFormat](./api-1805421-pmflattenpageformat.md)
  Flattens a page format object into a Memory Manager handle for storage in a user document.
- [PMFlattenPageFormatToCFData](./api-1805425-pmflattenpageformattocfdata.md)
  Flattens a page format object into a Core Foundation data object for storage in a user document.
- [PMFlattenPageFormatToURL](./api-1805429-pmflattenpageformattourl.md)
  Flattens a page format object into a file for storage in a user document.
- [PMUnflattenPageFormat](./api-1805434-pmunflattenpageformat.md)
  Rebuilds a page format object from a Memory Manager handle that contains flattened page format data.
- [PMUnflattenPageFormatWithCFData](./api-1805439-pmunflattenpageformatwithcfdata.md)
  Rebuilds a page format object from a Core Foundation data object that contains flattened page format data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/core_printing/1805441-pmunflattenpageformatwithurl)*