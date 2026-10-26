# PMPaperGetMargins(_:_:)

**Framework**: Application Services  
**Kind**: func  
**Role**: Function

Obtains the margins describing the unprintable area of the sheet represented by a paper object.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func PMPaperGetMargins(_ paper: PMPaper, _ paperMargins: UnsafeMutablePointer<PMPaperMargins>) -> OSStatus
```

```c
OSStatus PMPaperGetMargins(PMPaper paper, PMPaperMargins *paperMargins);
```

#### Return Value

A result code. See [Result Codes](./core_printing.md#1670007).

## Parameters

- `paper`: The paper whose margins you want to obtain.
- `paperMargins`: A pointer to your [`PMPaperMargins`](./pmpapermargins.md) structure. On return, the structure contains the unprintable margins of the specified paper, in points. The four values in the structure specify the top, left, bottom, and right imageable area margins of the paper. 

## See Also

### Accessing Data in Paper Objects
- [func PMPaperGetID(PMPaper, UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus](./api-1462910-pmpapergetid.md)
  Obtains the identifier of a paper object.
- [func PMPaperGetWidth(PMPaper, UnsafeMutablePointer<Double>) -> OSStatus](./api-1459209-pmpapergetwidth.md)
  Obtains the width of the sheet of paper represented by a paper object.
- [func PMPaperGetHeight(PMPaper, UnsafeMutablePointer<Double>) -> OSStatus](./api-1460389-pmpapergetheight.md)
  Obtains the height of the sheet of paper represented by a paper object.
- [func PMPaperCreateLocalizedName(PMPaper, PMPrinter, UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus](./api-1460981-pmpapercreatelocalizedname.md)
  Obtains the localized name for a given paper.
- [func PMPaperGetPrinterID(PMPaper, UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus](./api-1461737-pmpapergetprinterid.md)
  Obtains the printer ID of the printer to which a given paper corresponds.
- [func PMPaperGetPPDPaperName(PMPaper, UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus](./api-1461039-pmpapergetppdpapername.md)
  Obtains the PPD paper name for a given paper.
- [PMPaperGetName](./core_printing/api-1805534-pmpapergetname.md)
  Obtains the name for a given paper.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1461994-pmpapergetmargins)*