# PMCopyLocalizedPPD(_:_:)

**Framework**: Application Services  
**Kind**: func  
**Role**: Function

Obtains a localized PostScript printer description (PPD) file.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func PMCopyLocalizedPPD(_ ppd: CFURL, _ localizedPPD: UnsafeMutablePointer<Unmanaged<CFURL>?>) -> OSStatus
```

```c
OSStatus PMCopyLocalizedPPD(CFURLRef ppd, CFURLRef  _Nullable *localizedPPD);
```

#### Return Value

A result code. See [Result Codes](./core_printing.md#1670007).

#### Discussion

To access the data in the PPD file, you can use the function [`PMCopyPPDData(_:_:)`](./api-1460345-pmcopyppddata.md).

##### Special Considerations

In macOS 10.5 and later, the printing system supports globalized PPD files as defined in CUPS version 1.2 and later. A globalized PPD file contains multiple localizations within a single file. If a globalized PPD file exists, this function returns the URL to this file and it is up to the application to obtain the correct localized data. For more information, see [CUPS PPD Extensions](http://www.cups.org/documentation.php/spec-ppd.html).

## Parameters

- `ppd`: A Core Foundation URL object for a PPD file. You can obtain a PPD URL using the function [`PMCopyAvailablePPDs(_:_:)`](./api-1464170-pmcopyavailableppds.md).
- `localizedPPD`: A pointer to your [`CFURL`](../CoreFoundation/cfurl.md) variable. On return, the variable refers to a Core Foundation URL object. The URL specifies the location of a PPD file or a compressed PPD file that has been localized for the current user's language preference. You are responsible for releasing the URL. If the `ppd` parameter is not valid, the variable is set to `NULL`.

## See Also

### Accessing PostScript Printer Description Files
- [func PMCopyAvailablePPDs(PMPPDDomain, UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus](./api-1464170-pmcopyavailableppds.md)
  Obtains the list of PostScript printer description (PPD) files in a PPD domain.
- [func PMCopyPPDData(CFURL, UnsafeMutablePointer<Unmanaged<CFData>?>) -> OSStatus](./api-1460345-pmcopyppddata.md)
  Obtains the uncompressed PPD data for a PostScript printer description (PPD) file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1459690-pmcopylocalizedppd)*