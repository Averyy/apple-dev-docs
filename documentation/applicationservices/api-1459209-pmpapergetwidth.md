# PMPaperGetWidth(_:_:)

**Framework**: Application Services  
**Kind**: func  
**Role**: Function

Obtains the width of the sheet of paper represented by a paper object.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func PMPaperGetWidth(_ paper: PMPaper, _ paperWidth: UnsafeMutablePointer<Double>) -> OSStatus
```

```c
OSStatus PMPaperGetWidth(PMPaper paper, double *paperWidth);
```

#### Return Value

A result code. See [Result Codes](./core_printing.md#1670007).

## Parameters

- `paper`: The paper whose width you want to obtain.
- `paperWidth`: A pointer to your double-precision variable. On return, the variable contains the width of the specified paper, in points.

## See Also

### Accessing Data in Paper Objects
- [func PMPaperGetID(PMPaper, UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus](./api-1462910-pmpapergetid.md)
  Obtains the identifier of a paper object.
- [func PMPaperGetHeight(PMPaper, UnsafeMutablePointer<Double>) -> OSStatus](./api-1460389-pmpapergetheight.md)
  Obtains the height of the sheet of paper represented by a paper object.
- [func PMPaperGetMargins(PMPaper, UnsafeMutablePointer<PMPaperMargins>) -> OSStatus](./api-1461994-pmpapergetmargins.md)
  Obtains the margins describing the unprintable area of the sheet represented by a paper object.
- [func PMPaperCreateLocalizedName(PMPaper, PMPrinter, UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus](./api-1460981-pmpapercreatelocalizedname.md)
  Obtains the localized name for a given paper.
- [func PMPaperGetPrinterID(PMPaper, UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus](./api-1461737-pmpapergetprinterid.md)
  Obtains the printer ID of the printer to which a given paper corresponds.
- [func PMPaperGetPPDPaperName(PMPaper, UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus](./api-1461039-pmpapergetppdpapername.md)
  Obtains the PPD paper name for a given paper.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1459209-pmpapergetwidth)*