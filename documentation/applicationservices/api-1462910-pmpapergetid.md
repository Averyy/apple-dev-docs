# PMPaperGetID(_:_:)

**Framework**: Application Services  
**Kind**: func

Obtains the identifier of a paper object.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func PMPaperGetID(_ paper: PMPaper, _ paperID: UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus
```

#### Return_value

A result code. See [`Result Codes`](core_printing#1670007.md).

## Parameters

- `paper`: The paper whose identifier you want to obtain.
- `paperID`: A pointer to your   variable. On return, the variable refers to a Core Foundation string containing the unique identifier for this paper. You should not release the string without first retaining it.

## See Also

- [func PMPaperGetWidth(PMPaper, UnsafeMutablePointer<Double>) -> OSStatus](1459209-pmpapergetwidth.md)
  Obtains the width of the sheet of paper represented by a paper object.
- [func PMPaperGetHeight(PMPaper, UnsafeMutablePointer<Double>) -> OSStatus](1460389-pmpapergetheight.md)
  Obtains the height of the sheet of paper represented by a paper object.
- [func PMPaperGetMargins(PMPaper, UnsafeMutablePointer<PMPaperMargins>) -> OSStatus](1461994-pmpapergetmargins.md)
  Obtains the margins describing the unprintable area of the sheet represented by a paper object.
- [func PMPaperCreateLocalizedName(PMPaper, PMPrinter, UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus](1460981-pmpapercreatelocalizedname.md)
  Obtains the localized name for a given paper.
- [func PMPaperGetPrinterID(PMPaper, UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus](1461737-pmpapergetprinterid.md)
  Obtains the printer ID of the printer to which a given paper corresponds.
- [func PMPaperGetPPDPaperName(PMPaper, UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus](1461039-pmpapergetppdpapername.md)
  Obtains the PPD paper name for a given paper.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1462910-pmpapergetid)*