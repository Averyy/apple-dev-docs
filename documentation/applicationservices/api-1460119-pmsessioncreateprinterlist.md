# PMSessionCreatePrinterList(_:_:_:_:)

**Framework**: Application Services  
**Kind**: func

Creates a list of printers available in the specified printing session.

**Availability**:
- macOS 10.1+

## Declaration

```swift
func PMSessionCreatePrinterList(_ printSession: PMPrintSession, _ printerList: UnsafeMutablePointer<Unmanaged<CFArray>?>, _ currentIndex: UnsafeMutablePointer<CFIndex>?, _ currentPrinter: UnsafeMutablePointer<PMPrinter?>?) -> OSStatus
```

#### Return_value

A result code. See [`Result Codes`](core_printing#1670007.md).

#### Discussion

You must call this function between the creation and release of a printing session. See the function [`PMCreateSession(_:)`](1463247-pmcreatesession.md). 

You can call the function `PMSessionCreatePrinterList` to obtain a valid printer name to pass to the function `PMSessionSetCurrentPrinter`.

##### 1771103

In macOS 10.2 and later, Apple recommends using the function [`PMServerCreatePrinterList(_:_:)`](1459953-pmservercreateprinterlist.md) instead. `PMServerCreatePrinterList` doesn’t require a `PMSession` object; it can be called at any time. It also works directly with `PMPrinter` objects.

## Parameters

- `printSession`: The printing session whose printer list you want to obtain.
- `printerList`: A pointer to your   variable. On return, the variable refers to a Core Foundation array containing a list of printers available in the specified printing session. Each element in the array is a Core Foundation string that contains a printer’s name as shown in the user interface. You are responsible for releasing the array.
- `currentIndex`: A pointer to your   variable. On return, the variable contains a value specifying where the current printer is in the printer list.
- `currentPrinter`: A pointer to your   variable. On return, the variable refers to a printer object that represents the current printer. You should not release the printer object without first retaining it. If the printer is the generic printer, the variable is set to  .

## See Also

- [func PMServerLaunchPrinterBrowser(PMServer?, CFDictionary?) -> OSStatus](1460175-pmserverlaunchprinterbrowser.md)
  Launches the printer browser to browse the printers available for a print server.
- [func PMServerCreatePrinterList(PMServer?, UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus](1459953-pmservercreateprinterlist.md)
  Creates a list of printers available to a print server.
- [func PMPrinterCreateFromPrinterID(CFString) -> PMPrinter?](1461363-pmprintercreatefromprinterid.md)
  Creates a printer object from a print queue identifier.
- [func PMCreateGenericPrinter(UnsafeMutablePointer<PMPrinter?>) -> OSStatus](1461960-pmcreategenericprinter.md)
  Creates a generic printer object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1460119-pmsessioncreateprinterlist)*