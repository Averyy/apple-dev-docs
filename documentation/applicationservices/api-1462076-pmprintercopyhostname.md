# PMPrinterCopyHostName(_:_:)

**Framework**: Application Services  
**Kind**: func

Obtains the name of the server hosting the print queue for a given printer.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func PMPrinterCopyHostName(_ printer: PMPrinter, _ hostNameP: UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus
```

#### Return_value

A result code. See [`Result Codes`](core_printing#1670007.md).

#### Discussion

This function is typically used to obtain the name of the computer that hosts a shared printer, possibly for display in a user interface. In macOS 10.5 and later, the typical way that users browse and communicate with a shared printer creates a local print queue and `PMPrinterCopyHostName` for such a print queue will return the name of the local host.

## Parameters

- `printer`: The printer whose print queue host name you want to obtain.
- `hostNameP`: A pointer to your   variable. On return, the variable refers to a Core Foundation string containing the name of the specified printer’s server. You are responsible for releasing the string.

## See Also

- [func PMPrinterCopyDescriptionURL(PMPrinter, CFString, UnsafeMutablePointer<Unmanaged<CFURL>?>) -> OSStatus](1459187-pmprintercopydescriptionurl.md)
  Obtains the URL of the description file for a given printer.
- [func PMPrinterCopyDeviceURI(PMPrinter, UnsafeMutablePointer<Unmanaged<CFURL>?>) -> OSStatus](1460543-pmprintercopydeviceuri.md)
  Obtains the device URI of a given printer.
- [func PMPrinterCopyPresets(PMPrinter, UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus](1459117-pmprintercopypresets.md)
  Obtains a list of print settings presets for a printer.
- [func PMPrinterGetCommInfo(PMPrinter, UnsafeMutablePointer<DarwinBoolean>?, UnsafeMutablePointer<DarwinBoolean>?) -> OSStatus](1461069-pmprintergetcomminfo.md)
  Obtains information about the communication channel for a printer.
- [func PMPrinterGetDriverCreator(PMPrinter, UnsafeMutablePointer<OSType>) -> OSStatus](1459107-pmprintergetdrivercreator.md)
  Obtains the creator of the driver associated with the specified printer.
- [func PMPrinterGetID(PMPrinter) -> Unmanaged<CFString>?](1459606-pmprintergetid.md)
  Returns the unique identifier of a printer.
- [func PMPrinterGetLocation(PMPrinter) -> Unmanaged<CFString>?](1461467-pmprintergetlocation.md)
  Returns the location of a printer.
- [func PMPrinterGetMakeAndModelName(PMPrinter, UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus](1463347-pmprintergetmakeandmodelname.md)
  Obtains the manufacturer and model name of the specified printer.
- [func PMPrinterGetMimeTypes(PMPrinter, PMPrintSettings?, UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus](1460125-pmprintergetmimetypes.md)
  Obtains a list of MIME content types supported by a printer using the specified print settings.
- [func PMPrinterGetName(PMPrinter) -> Unmanaged<CFString>?](1459018-pmprintergetname.md)
  Returns the human-readable name of a printer.
- [func PMPrinterGetOutputResolution(PMPrinter, PMPrintSettings, UnsafeMutablePointer<PMResolution>) -> OSStatus](1459076-pmprintergetoutputresolution.md)
  Obtains the printer hardware output resolution for the specified print settings.
- [func PMPrinterSetOutputResolution(PMPrinter, PMPrintSettings, UnsafePointer<PMResolution>) -> OSStatus](1459931-pmprintersetoutputresolution.md)
  Sets the print settings to reflect the specified printer hardware output resolution.
- [func PMPrinterGetPaperList(PMPrinter, UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus](1460088-pmprintergetpaperlist.md)
  Obtains the list of papers available for a printer.
- [func PMPrinterGetPrinterResolutionCount(PMPrinter, UnsafeMutablePointer<UInt32>) -> OSStatus](1462004-pmprintergetprinterresolutioncou.md)
  Obtains the number of resolution settings supported by the specified printer.
- [func PMPrinterGetIndexedPrinterResolution(PMPrinter, UInt32, UnsafeMutablePointer<PMResolution>) -> OSStatus](1464490-pmprintergetindexedprinterresolu.md)
  Obtains a resolution setting based on an index into the range of settings supported by the specified printer.
- [func PMPrinterGetState(PMPrinter, UnsafeMutablePointer<PMPrinterState>) -> OSStatus](1462954-pmprintergetstate.md)
  Obtains the current state of the print queue for a printer.
- [func PMPrinterSetDefault(PMPrinter) -> OSStatus](1461118-pmprintersetdefault.md)
  Sets the default printer for the current user.
- [func PMPrinterIsDefault(PMPrinter) -> Bool](1459030-pmprinterisdefault.md)
  Returns a Boolean value indicating whether a printer is the default printer for the current user.
- [func PMPrinterIsFavorite(PMPrinter) -> Bool](1462074-pmprinterisfavorite.md)
  Returns a Boolean value indicating whether a printer is in the user’s list of favorite printers.
- [func PMPrinterIsPostScriptCapable(PMPrinter) -> Bool](1464168-pmprinterispostscriptcapable.md)
  Returns a Boolean value indicating whether a printer is PostScript capable.
- [func PMPrinterIsPostScriptPrinter(PMPrinter, UnsafeMutablePointer<DarwinBoolean>) -> OSStatus](1462257-pmprinterispostscriptprinter.md)
  Determines whether a printer is a PostScript printer.
- [func PMPrinterIsRemote(PMPrinter, UnsafeMutablePointer<DarwinBoolean>) -> OSStatus](1461377-pmprinterisremote.md)
  Indicates whether a printer is hosted by a remote print server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1462076-pmprintercopyhostname)*