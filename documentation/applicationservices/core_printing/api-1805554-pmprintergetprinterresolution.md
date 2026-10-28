# PMPrinterGetPrinterResolution

**Framework**: Application Services  
**Kind**: func

Obtains a resolution setting for the specified printer.

> **Deprecated**: Use [`PMPrinterGetPrinterResolutionCount`](../api-1462004-pmprintergetprinterresolutioncou.md) and [`PMPrinterGetIndexedPrinterResolution`](../api-1464490-pmprintergetindexedprinterresolu.md) to examine the available printer resolutions.

## Declaration

```c
OSStatus PMPrinterGetPrinterResolution (
   PMPrinter printer,
   PMTag tag,
   PMResolution *res
);
```

## Return Value

A result code. The result code `kPMNotImplemented` indicates that the printer driver does not support multiple resolution settings.

## Parameters

- `printer`: The printer whose resolution you want to obtain.
- `tag`: A tag that specifies the kind of resolution information you want to obtain (minimum, maximum, default, and so forth). See [Tag Constants](./tag_constants.md) for a description of the constants you can pass in this parameter.
- `res`: A pointer to your [PMResolution](./pmresolution.md) data structure. On return, the structure contains the resolution setting associated with the tag value.

## See Also

### Accessing Information About a Printer
- [PMPrinterCopyDescriptionURL](../api-1459187-pmprintercopydescriptionurl.md)
  Obtains the URL of the description file for a given printer.
- [PMPrinterCopyDeviceURI](../api-1460543-pmprintercopydeviceuri.md)
  Obtains the device URI of a given printer.
- [PMPrinterCopyHostName](../api-1462076-pmprintercopyhostname.md)
  Obtains the name of the server hosting the print queue for a given printer.
- [PMPrinterCopyPresets](../api-1459117-pmprintercopypresets.md)
  Obtains a list of print settings presets for a printer.
- [PMPrinterGetCommInfo](../api-1461069-pmprintergetcomminfo.md)
  Obtains information about the communication channel for a printer.
- [PMPrinterGetDescriptionURL](./api-1805546-pmprintergetdescriptionurl.md)
  Obtains a reference to the specified printer’s description file.
- [PMPrinterGetDeviceURI](./api-1805547-pmprintergetdeviceuri.md)
  Obtains a copy of a printer's device URI.
- [PMPrinterGetDriverCreator](../api-1459107-pmprintergetdrivercreator.md)
  Obtains the creator of the driver associated with the specified printer.
- [PMPrinterGetDriverReleaseInfo](../api-1464149-pmprintergetdriverreleaseinfo.md)
  Obtains version information for the driver associated with the specified printer.
- [PMPrinterGetID](../api-1459606-pmprintergetid.md)
  Returns the unique identifier of a printer.
- [PMPrinterGetLanguageInfo](../api-1458956-pmprintergetlanguageinfo.md)
  Obtains information about the imaging language for the specified printer.
- [PMPrinterGetLocation](../api-1461467-pmprintergetlocation.md)
  Returns the location of a printer.
- [PMPrinterGetMakeAndModelName](../api-1463347-pmprintergetmakeandmodelname.md)
  Obtains the manufacturer and model name of the specified printer.
- [PMPrinterGetMimeTypes](../api-1460125-pmprintergetmimetypes.md)
  Obtains a list of MIME content types supported by a printer using the specified print settings.
- [PMPrinterGetName](../api-1459018-pmprintergetname.md)
  Returns the human-readable name of a printer.
- [PMPrinterGetOutputResolution](../api-1459076-pmprintergetoutputresolution.md)
  Obtains the printer hardware output resolution for the specified print settings.
- [PMPrinterSetOutputResolution](../api-1459931-pmprintersetoutputresolution.md)
  Sets the print settings to reflect the specified printer hardware output resolution.
- [PMPrinterGetPaperList](../api-1460088-pmprintergetpaperlist.md)
  Obtains the list of papers available for a printer.
- [PMPrinterGetPrinterResolutionCount](../api-1462004-pmprintergetprinterresolutioncou.md)
  Obtains the number of resolution settings supported by the specified printer.
- [PMPrinterGetIndexedPrinterResolution](../api-1464490-pmprintergetindexedprinterresolu.md)
  Obtains a resolution setting based on an index into the range of settings supported by the specified printer.
- [PMPrinterGetState](../api-1462954-pmprintergetstate.md)
  Obtains the current state of the print queue for a printer.
- [PMPrinterSetDefault](../api-1461118-pmprintersetdefault.md)
  Sets the default printer for the current user.
- [PMPrinterIsDefault](../api-1459030-pmprinterisdefault.md)
  Returns a Boolean value indicating whether a printer is the default printer for the current user.
- [PMPrinterIsFavorite](../api-1462074-pmprinterisfavorite.md)
  Returns a Boolean value indicating whether a printer is in the user’s list of favorite printers.
- [PMPrinterIsPostScriptCapable](../api-1464168-pmprinterispostscriptcapable.md)
  Returns a Boolean value indicating whether a printer is PostScript capable.
- [PMPrinterIsPostScriptPrinter](../api-1462257-pmprinterispostscriptprinter.md)
  Determines whether a printer is a PostScript printer.
- [PMPrinterIsRemote](../api-1461377-pmprinterisremote.md)
  Indicates whether a printer is hosted by a remote print server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/core_printing/1805554-pmprintergetprinterresolution)*