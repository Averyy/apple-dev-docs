# PMPaperCreateLocalizedName(_:_:_:)

**Framework**: Application Services  
**Kind**: func  
**Role**: Function

Obtains the localized name for a given paper.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func PMPaperCreateLocalizedName(_ paper: PMPaper, _ printer: PMPrinter, _ paperName: UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus
```

```c
OSStatus PMPaperCreateLocalizedName(PMPaper paper, PMPrinter printer, CFStringRef  _Nullable *paperName);
```

## Return Value

A result code. See [Result Codes](./core_printing.md#1670007).

## Discussion

Not all printers have the same way of referring to a given paper. Generally, if you want to obtain the name of a paper, you want to localize the paper name for a particular printer. For example, if you were displaying a list of papers for a given printer, you would want the paper names to be localized for that printer.

### Special Considerations

In macOS 10.5 and later, Apple recommends using this function instead of [PMPaperGetName](./core_printing/api-1805534-pmpapergetname.md).

## Parameters

- `paper`: The paper whose localized name you want to obtain.
- `printer`: The printer for which the localization should be performed.
- `paperName`: A pointer to your [`CFString`](../CoreFoundation/cfstring.md) variable. On return, the variable refers to a Core Foundation string that contains the localized name of the paper. This name is appropriate to display in the user interface. If an error occurs, the variable is set to `NULL`. You are responsible for releasing the string.

## See Also

### Accessing Data in Paper Objects
- [func PMPaperGetID(PMPaper, UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus](./api-1462910-pmpapergetid.md)
  Obtains the identifier of a paper object.
- [func PMPaperGetWidth(PMPaper, UnsafeMutablePointer<Double>) -> OSStatus](./api-1459209-pmpapergetwidth.md)
  Obtains the width of the sheet of paper represented by a paper object.
- [func PMPaperGetHeight(PMPaper, UnsafeMutablePointer<Double>) -> OSStatus](./api-1460389-pmpapergetheight.md)
  Obtains the height of the sheet of paper represented by a paper object.
- [func PMPaperGetMargins(PMPaper, UnsafeMutablePointer<PMPaperMargins>) -> OSStatus](./api-1461994-pmpapergetmargins.md)
  Obtains the margins describing the unprintable area of the sheet represented by a paper object.
- [func PMPaperGetPrinterID(PMPaper, UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus](./api-1461737-pmpapergetprinterid.md)
  Obtains the printer ID of the printer to which a given paper corresponds.
- [func PMPaperGetPPDPaperName(PMPaper, UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus](./api-1461039-pmpapergetppdpapername.md)
  Obtains the PPD paper name for a given paper.
- [PMPaperGetName](./core_printing/api-1805534-pmpapergetname.md)
  Obtains the name for a given paper.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1460981-pmpapercreatelocalizedname)*