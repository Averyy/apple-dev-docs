# PMCreateGenericPrinter(_:)

**Framework**: Application Services  
**Kind**: func

Creates a generic printer object.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func PMCreateGenericPrinter(_ printer: UnsafeMutablePointer<PMPrinter?>) -> OSStatus
```

#### Return_value

A result code. See [`Result Codes`](core_printing#1670007.md).

#### Discussion

This function provides a way to create a `PMPrinter` object that represents the generic formatting printer.

## Parameters

- `printer`: A pointer to your   variable. On return, the variable refers to a new printer object that represents the generic formatting printer. You are responsible for releasing the printer object with the function  .

## See Also

- [func PMServerLaunchPrinterBrowser(PMServer?, CFDictionary?) -> OSStatus](1460175-pmserverlaunchprinterbrowser.md)
  Launches the printer browser to browse the printers available for a print server.
- [func PMServerCreatePrinterList(PMServer?, UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus](1459953-pmservercreateprinterlist.md)
  Creates a list of printers available to a print server.
- [func PMSessionCreatePrinterList(PMPrintSession, UnsafeMutablePointer<Unmanaged<CFArray>?>, UnsafeMutablePointer<CFIndex>?, UnsafeMutablePointer<PMPrinter?>?) -> OSStatus](1460119-pmsessioncreateprinterlist.md)
  Creates a list of printers available in the specified printing session.
- [func PMPrinterCreateFromPrinterID(CFString) -> PMPrinter?](1461363-pmprintercreatefromprinterid.md)
  Creates a printer object from a print queue identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1461960-pmcreategenericprinter)*