# PMPrinterCreateFromPrinterID(_:)

**Framework**: Application Services  
**Kind**: func

Creates a printer object from a print queue identifier.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func PMPrinterCreateFromPrinterID(_ printerID: CFString) -> PMPrinter?
```

#### Return_value

A new printer object, or `NULL` if no print queue is available with the specified identifier. You are responsible for releasing the printer object with the function [`PMRelease(_:)`](1461402-pmrelease.md).

#### Discussion

This function is typically used to re-create a printer object using the print queue ID obtained by a call to `PMPrinterGetID` at an earlier time. If the print queue is deleted after obtaining the ID, this function returns `NULL` for that ID.

## Parameters

- `printerID`: The unique identifier of a print queue.

## See Also

- [func PMServerLaunchPrinterBrowser(PMServer?, CFDictionary?) -> OSStatus](1460175-pmserverlaunchprinterbrowser.md)
  Launches the printer browser to browse the printers available for a print server.
- [func PMServerCreatePrinterList(PMServer?, UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus](1459953-pmservercreateprinterlist.md)
  Creates a list of printers available to a print server.
- [func PMSessionCreatePrinterList(PMPrintSession, UnsafeMutablePointer<Unmanaged<CFArray>?>, UnsafeMutablePointer<CFIndex>?, UnsafeMutablePointer<PMPrinter?>?) -> OSStatus](1460119-pmsessioncreateprinterlist.md)
  Creates a list of printers available in the specified printing session.
- [func PMCreateGenericPrinter(UnsafeMutablePointer<PMPrinter?>) -> OSStatus](1461960-pmcreategenericprinter.md)
  Creates a generic printer object.
- [func PMPrinterGetID(PMPrinter) -> Unmanaged<CFString>?](1459606-pmprintergetid.md)
  Returns the unique identifier of a printer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1461363-pmprintercreatefromprinterid)*