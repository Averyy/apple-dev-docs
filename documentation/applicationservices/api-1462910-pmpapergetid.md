# PMPaperGetID(_:_:)

**Framework**: Application Services  
**Kind**: func  
**Role**: Function

Obtains the identifier of a paper object.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func PMPaperGetID(_ paper: PMPaper, _ paperID: UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus
```

```c
OSStatus PMPaperGetID(PMPaper paper, CFStringRef  _Nullable *paperID);
```

## Return Value

A result code. See [Result Codes](./core_printing.md#1670007).

## Parameters

- `paper`: The paper whose identifier you want to obtain.
- `paperID`: A pointer to your [`CFString`](../CoreFoundation/cfstring.md) variable. On return, the variable refers to a Core Foundation string containing the unique identifier for this paper. You should not release the string without first retaining it.

## See Also

### Accessing Data in Paper Objects
- [func PMPaperGetWidth(PMPaper, UnsafeMutablePointer<Double>) -> OSStatus](./api-1459209-pmpapergetwidth.md)
  Obtains the width of the sheet of paper represented by a paper object.
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
- [PMPaperGetName](./core_printing/api-1805534-pmpapergetname.md)
  Obtains the name for a given paper.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1462910-pmpapergetid)*