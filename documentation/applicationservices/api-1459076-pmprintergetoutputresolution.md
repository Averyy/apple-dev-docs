# PMPrinterGetOutputResolution(_:_:_:)

**Framework**: Application Services  
**Kind**: func

Obtains the printer hardware output resolution for the specified print settings.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func PMPrinterGetOutputResolution(_ printer: PMPrinter, _ printSettings: PMPrintSettings, _ resolutionP: UnsafeMutablePointer<PMResolution>) -> OSStatus
```

#### Return_value

A result code. If the resolution cannot be reliably determined, this function returns an error.

#### Discussion

Some printers allow programmatic control of their hardware output resolution on a print job basis. The hardware resolution is determined by the combination of printer and print settings used for the print job. This function returns the best guess as to what printer resolution setting will be used for the destination print job.

Most applications do not need to use this function because they draw the same content regardless of the destination device. For those few applications that do adjust their drawing based on the output device, they should only do so when the print job destination is `kPMDestinationPrinter` or `kPMDestinationFax`. You can use the function `PMSessionGetDestinationType` to determine the destination for a print job.

This function should be used after displaying the Print dialog to the user so that it correctly reflects changes in print settings performed prior to printing.

## Parameters

- `printer`: The printer whose output resolution you want to obtain.
- `printSettings`: The print settings you want to use.
- `resolutionP`: A pointer to your   structure. On return, the structure contains the output resolution of the specified printer in pixels per inch.

## See Also

- [func PMPrinterCopyDescriptionURL(PMPrinter, CFString, UnsafeMutablePointer<Unmanaged<CFURL>?>) -> OSStatus](1459187-pmprintercopydescriptionurl.md)
  Obtains the URL of the description file for a given printer.
- [func PMPrinterCopyDeviceURI(PMPrinter, UnsafeMutablePointer<Unmanaged<CFURL>?>) -> OSStatus](1460543-pmprintercopydeviceuri.md)
  Obtains the device URI of a given printer.
- [func PMPrinterCopyHostName(PMPrinter, UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus](1462076-pmprintercopyhostname.md)
  Obtains the name of the server hosting the print queue for a given printer.
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

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1459076-pmprintergetoutputresolution)*