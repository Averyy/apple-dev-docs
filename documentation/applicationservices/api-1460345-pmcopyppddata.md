# PMCopyPPDData(_:_:)

**Framework**: Application Services  
**Kind**: func

Obtains the uncompressed PPD data for a PostScript printer description (PPD) file.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func PMCopyPPDData(_ ppd: CFURL, _ data: UnsafeMutablePointer<Unmanaged<CFData>?>) -> OSStatus
```

#### Return_value

A result code. See [`Result Codes`](core_printing#1670007.md).

## Parameters

- `ppd`: A URL for a PPD or compressed PPD file. You can obtain a PPD URL using the function   or  .
- `data`: A pointer to your   variable. On return, the variable refers to a Core Foundation data object containing the uncompressed PPD data from the specified PPD file. You are responsible for releasing the data object. If the   parameter does not reference a PPD file, the variable is set to  .

## See Also

- [func PMCopyAvailablePPDs(PMPPDDomain, UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus](1464170-pmcopyavailableppds.md)
  Obtains the list of PostScript printer description (PPD) files in a PPD domain.
- [func PMCopyLocalizedPPD(CFURL, UnsafeMutablePointer<Unmanaged<CFURL>?>) -> OSStatus](1459690-pmcopylocalizedppd.md)
  Obtains a localized PostScript printer description (PPD) file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1460345-pmcopyppddata)*