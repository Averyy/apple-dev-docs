# PMPaperGetPrinterID(_:_:)

**Framework**: Application Services  
**Kind**: func

Obtains the printer ID of the printer to which a given paper corresponds.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func PMPaperGetPrinterID(_ paper: PMPaper, _ printerID: UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus
```

#### Return_value

A result code. See [`Result Codes`](core_printing#1670007.md).

#### Discussion

Not all papers have a printer ID associated with them. If the printer ID is known, the printer is displayed in the Page Setup dialog’s Format for pop-up menu. If the printer ID is not known, the default formatting printer is the generic Any Printer. The printing system provides default paper sizes for the generic printer.

## Parameters

- `paper`: The paper whose printer ID you want to obtain.
- `printerID`: A pointer to your   variable. On return, the variable refers to a Core Foundation string that contains the printer ID for the specified paper. If an error occurs, the variable is set to  . You should not release the string without first retaining it.

## See Also

- [func PMPaperGetID(PMPaper, UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus](1462910-pmpapergetid.md)
  Obtains the identifier of a paper object.
- [func PMPaperGetWidth(PMPaper, UnsafeMutablePointer<Double>) -> OSStatus](1459209-pmpapergetwidth.md)
  Obtains the width of the sheet of paper represented by a paper object.
- [func PMPaperGetHeight(PMPaper, UnsafeMutablePointer<Double>) -> OSStatus](1460389-pmpapergetheight.md)
  Obtains the height of the sheet of paper represented by a paper object.
- [func PMPaperGetMargins(PMPaper, UnsafeMutablePointer<PMPaperMargins>) -> OSStatus](1461994-pmpapergetmargins.md)
  Obtains the margins describing the unprintable area of the sheet represented by a paper object.
- [func PMPaperCreateLocalizedName(PMPaper, PMPrinter, UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus](1460981-pmpapercreatelocalizedname.md)
  Obtains the localized name for a given paper.
- [func PMPaperGetPPDPaperName(PMPaper, UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus](1461039-pmpapergetppdpapername.md)
  Obtains the PPD paper name for a given paper.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1461737-pmpapergetprinterid)*