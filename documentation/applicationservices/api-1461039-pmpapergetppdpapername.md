# PMPaperGetPPDPaperName(_:_:)

**Framework**: Application Services  
**Kind**: func

Obtains the PPD paper name for a given paper.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func PMPaperGetPPDPaperName(_ paper: PMPaper, _ paperName: UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus
```

#### Return_value

A result code. See [`Result Codes`](core_printing#1670007.md).

#### Discussion

The macOS printing system uses a PostScript Printer Description (PPD) file to describe a given printer and print queue for that printer. The PPD paper name is the name that uniquely identifies a given paper for the printer to which the paper corresponds. To obtain a list of papers for a given printer, use the function [`PMPrinterGetPaperList(_:_:)`](1460088-pmprintergetpaperlist.md).

## Parameters

- `paper`: The paper whose PPD paper name you want to obtain.
- `paperName`: A pointer to your   variable. On return, the variable refers to a Core Foundation string that contains the PPD paper name for the specified paper. If an error occurs, the variable is set to  . You should not release the string without first retaining it.

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
- [func PMPaperGetPrinterID(PMPaper, UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus](1461737-pmpapergetprinterid.md)
  Obtains the printer ID of the printer to which a given paper corresponds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1461039-pmpapergetppdpapername)*