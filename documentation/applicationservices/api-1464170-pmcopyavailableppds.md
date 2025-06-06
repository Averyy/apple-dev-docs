# PMCopyAvailablePPDs(_:_:)

**Framework**: Application Services  
**Kind**: func

Obtains the list of PostScript printer description (PPD) files in a PPD domain.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func PMCopyAvailablePPDs(_ domain: PMPPDDomain, _ ppds: UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus
```

#### Return_value

A result code. See [`Result Codes`](core_printing#1670007.md).

## Parameters

- `domain`: The PPD domain to search. See   for a description of the constants you can use to specify the domain.
- `ppds`: A pointer to your   variable. On return, the variable refers to a Core Foundation array of PPD files in the specified domain. Each element in the array is a Core Foundation URL object that specifies the location of a PPD file or a compressed PPD file. You are responsible for releasing the array. If the specified domain is not valid, the variable is set to  .

## See Also

- [func PMCopyLocalizedPPD(CFURL, UnsafeMutablePointer<Unmanaged<CFURL>?>) -> OSStatus](1459690-pmcopylocalizedppd.md)
  Obtains a localized PostScript printer description (PPD) file.
- [func PMCopyPPDData(CFURL, UnsafeMutablePointer<Unmanaged<CFData>?>) -> OSStatus](1460345-pmcopyppddata.md)
  Obtains the uncompressed PPD data for a PostScript printer description (PPD) file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1464170-pmcopyavailableppds)*