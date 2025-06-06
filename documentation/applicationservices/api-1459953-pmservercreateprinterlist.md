# PMServerCreatePrinterList(_:_:)

**Framework**: Application Services  
**Kind**: func

Creates a list of printers available to a print server.

**Availability**:
- macOS 10.2+

## Declaration

```swift
func PMServerCreatePrinterList(_ server: PMServer?, _ printerList: UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus
```

#### Return_value

A result code. See [`Result Codes`](core_printing#1670007.md).

## Parameters

- `server`: The print server whose printers you want to obtain. To specify the local print server, pass the constant  . Currently, you may specify only the local print server.
- `printerList`: A pointer to your   variable. On return, the variable refers to a Core Foundation array containing the printers available to the specified print server. Each element in the array is a   object. You are responsible for releasing the array.

## See Also

- [func PMServerLaunchPrinterBrowser(PMServer?, CFDictionary?) -> OSStatus](1460175-pmserverlaunchprinterbrowser.md)
  Launches the printer browser to browse the printers available for a print server.
- [func PMSessionCreatePrinterList(PMPrintSession, UnsafeMutablePointer<Unmanaged<CFArray>?>, UnsafeMutablePointer<CFIndex>?, UnsafeMutablePointer<PMPrinter?>?) -> OSStatus](1460119-pmsessioncreateprinterlist.md)
  Creates a list of printers available in the specified printing session.
- [func PMPrinterCreateFromPrinterID(CFString) -> PMPrinter?](1461363-pmprintercreatefromprinterid.md)
  Creates a printer object from a print queue identifier.
- [func PMCreateGenericPrinter(UnsafeMutablePointer<PMPrinter?>) -> OSStatus](1461960-pmcreategenericprinter.md)
  Creates a generic printer object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1459953-pmservercreateprinterlist)*