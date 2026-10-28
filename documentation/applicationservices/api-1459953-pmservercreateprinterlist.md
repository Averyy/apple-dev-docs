# PMServerCreatePrinterList(_:_:)

**Framework**: Application Services  
**Kind**: func  
**Role**: Function

Creates a list of printers available to a print server.

**Availability**:
- macOS 10.2+

## Declaration

```swift
func PMServerCreatePrinterList(_ server: PMServer?, _ printerList: UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus
```

```c
OSStatus PMServerCreatePrinterList(PMServer server, CFArrayRef  _Nullable *printerList);
```

## Return Value

A result code. See [Result Codes](./core_printing.md#1670007).

## Parameters

- `server`: The print server whose printers you want to obtain. To specify the local print server, pass the constant `kPMServerLocal`. Currently, you may specify only the local print server.
- `printerList`: A pointer to your [`CFArray`](../CoreFoundation/cfarray.md) variable. On return, the variable refers to a Core Foundation array containing the printers available to the specified print server. Each element in the array is a `PMPrinter` object. You are responsible for releasing the array.

## See Also

### Creating Printer Objects
- [func PMServerLaunchPrinterBrowser(PMServer?, CFDictionary?) -> OSStatus](./api-1460175-pmserverlaunchprinterbrowser.md)
  Launches the printer browser to browse the printers available for a print server.
- [func PMSessionCreatePrinterList(PMPrintSession, UnsafeMutablePointer<Unmanaged<CFArray>?>, UnsafeMutablePointer<CFIndex>?, UnsafeMutablePointer<PMPrinter?>?) -> OSStatus](./api-1460119-pmsessioncreateprinterlist.md)
  Creates a list of printers available in the specified printing session.
- [func PMPrinterCreateFromPrinterID(CFString) -> PMPrinter?](./api-1461363-pmprintercreatefromprinterid.md)
  Creates a printer object from a print queue identifier.
- [func PMCreateGenericPrinter(UnsafeMutablePointer<PMPrinter?>) -> OSStatus](./api-1461960-pmcreategenericprinter.md)
  Creates a generic printer object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1459953-pmservercreateprinterlist)*