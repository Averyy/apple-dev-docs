# PMServerLaunchPrinterBrowser(_:_:)

**Framework**: Application Services  
**Kind**: func

Launches the printer browser to browse the printers available for a print server.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func PMServerLaunchPrinterBrowser(_ server: PMServer?, _ options: CFDictionary?) -> OSStatus
```

#### Return_value

A result code. See [`Result Codes`](core_printing#1670007.md).  If you specify a server whose printers cannot be browsed, this function returns the error code `kPMInvalidParameter`.

#### Discussion

This function displays the standard printer browser to allow the user to create a new print queue.

## Parameters

- `server`: The print server to browse. Pass   to specify the local print server. Currently, you may specify only the local print server.
- `options`: This parameter is reserved for future use. At the present time, pass  . Passing   presents the printer browser in the default fashion.

## See Also

- [func PMServerCreatePrinterList(PMServer?, UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus](1459953-pmservercreateprinterlist.md)
  Creates a list of printers available to a print server.
- [func PMSessionCreatePrinterList(PMPrintSession, UnsafeMutablePointer<Unmanaged<CFArray>?>, UnsafeMutablePointer<CFIndex>?, UnsafeMutablePointer<PMPrinter?>?) -> OSStatus](1460119-pmsessioncreateprinterlist.md)
  Creates a list of printers available in the specified printing session.
- [func PMPrinterCreateFromPrinterID(CFString) -> PMPrinter?](1461363-pmprintercreatefromprinterid.md)
  Creates a printer object from a print queue identifier.
- [func PMCreateGenericPrinter(UnsafeMutablePointer<PMPrinter?>) -> OSStatus](1461960-pmcreategenericprinter.md)
  Creates a generic printer object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1460175-pmserverlaunchprinterbrowser)*