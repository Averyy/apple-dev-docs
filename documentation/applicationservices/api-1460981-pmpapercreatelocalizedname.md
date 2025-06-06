# PMPaperCreateLocalizedName(_:_:_:)

**Framework**: Application Services  
**Kind**: func

Obtains the localized name for a given paper.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func PMPaperCreateLocalizedName(_ paper: PMPaper, _ printer: PMPrinter, _ paperName: UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus
```

#### Return_value

A result code. See [`Result Codes`](core_printing#1670007.md).

#### Discussion

Not all printers have the same way of referring to a given paper. Generally, if you want to obtain the name of a paper, you want to localize the paper name for a particular printer. For example, if you were displaying a list of papers for a given printer, you would want the paper names to be localized for that printer.

##### 1771098

In macOS 10.5 and later, Apple recommends using this function instead of [`PMPaperGetName`](core_printing/1805534-pmpapergetname.md).

## Parameters

- `paper`: The paper whose localized name you want to obtain.
- `printer`: The printer for which the localization should be performed.
- `paperName`: A pointer to your   variable. On return, the variable refers to a Core Foundation string that contains the localized name of the paper. This name is appropriate to display in the user interface. If an error occurs, the variable is set to  . You are responsible for releasing the string.

## See Also

- [func PMPaperGetID(PMPaper, UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus](1462910-pmpapergetid.md)
  Obtains the identifier of a paper object.
- [func PMPaperGetWidth(PMPaper, UnsafeMutablePointer<Double>) -> OSStatus](1459209-pmpapergetwidth.md)
  Obtains the width of the sheet of paper represented by a paper object.
- [func PMPaperGetHeight(PMPaper, UnsafeMutablePointer<Double>) -> OSStatus](1460389-pmpapergetheight.md)
  Obtains the height of the sheet of paper represented by a paper object.
- [func PMPaperGetMargins(PMPaper, UnsafeMutablePointer<PMPaperMargins>) -> OSStatus](1461994-pmpapergetmargins.md)
  Obtains the margins describing the unprintable area of the sheet represented by a paper object.
- [func PMPaperGetPrinterID(PMPaper, UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus](1461737-pmpapergetprinterid.md)
  Obtains the printer ID of the printer to which a given paper corresponds.
- [func PMPaperGetPPDPaperName(PMPaper, UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus](1461039-pmpapergetppdpapername.md)
  Obtains the PPD paper name for a given paper.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1460981-pmpapercreatelocalizedname)*