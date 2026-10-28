# PMCreateGenericPrinter(_:)

**Framework**: Application Services  
**Kind**: func  
**Role**: Function

Creates a generic printer object.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func PMCreateGenericPrinter(_ printer: UnsafeMutablePointer<PMPrinter?>) -> OSStatus
```

```c
OSStatus PMCreateGenericPrinter(PMPrinter  _Nullable *printer);
```

## Return Value

A result code. See [Result Codes](./core_printing.md#1670007).

## Discussion

This function provides a way to create a `PMPrinter` object that represents the generic formatting printer.

## Parameters

- `printer`: A pointer to your [`PMPrinter`](./pmprinter.md) variable. On return, the variable refers to a new printer object that represents the generic formatting printer. You are responsible for releasing the printer object with the function [`PMRelease(_:)`](./api-1461402-pmrelease.md).

## See Also

### Creating Printer Objects
- [func PMServerLaunchPrinterBrowser(PMServer?, CFDictionary?) -> OSStatus](./api-1460175-pmserverlaunchprinterbrowser.md)
  Launches the printer browser to browse the printers available for a print server.
- [func PMServerCreatePrinterList(PMServer?, UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus](./api-1459953-pmservercreateprinterlist.md)
  Creates a list of printers available to a print server.
- [func PMSessionCreatePrinterList(PMPrintSession, UnsafeMutablePointer<Unmanaged<CFArray>?>, UnsafeMutablePointer<CFIndex>?, UnsafeMutablePointer<PMPrinter?>?) -> OSStatus](./api-1460119-pmsessioncreateprinterlist.md)
  Creates a list of printers available in the specified printing session.
- [func PMPrinterCreateFromPrinterID(CFString) -> PMPrinter?](./api-1461363-pmprintercreatefromprinterid.md)
  Creates a printer object from a print queue identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1461960-pmcreategenericprinter)*