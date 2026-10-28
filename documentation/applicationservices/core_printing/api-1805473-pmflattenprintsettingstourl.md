# PMFlattenPrintSettingsToURL

**Framework**: Application Services  
**Kind**: func

Flattens a print settings object into a URL for storage in a user document.

> **Deprecated**: Instead use [`PMPrintSettingsCreateDataRepresentation`](../api-1464570-pmprintsettingscreatedatareprese.md) and write the resulting data to your destination.

## Declaration

```c
OSStatus PMFlattenPrintSettingsToURL (
   PMPrintSettings printSettings,
   CFURLRef flattenFileURL
);
```

## Return Value

A result code. See [Result Codes](../core_printing.md#1670007).

## Parameters

- `printSettings`: The print settings object to flatten.
- `flattenFileURL`: A Core Foundation URL specifying a file to contain a flattened representation of the specified print settings object. If the file already exists, it is overwritten. Only file-based URLs are supported.

## See Also

### Creating and Using Print Settings Objects
- [PMCreatePrintSettings](../api-1463239-pmcreateprintsettings.md)
  Creates a new print settings object.
- [PMSessionDefaultPrintSettings](../api-1460138-pmsessiondefaultprintsettings.md)
  Assigns default parameter values to a print settings object for the specified printing session.
- [PMSessionValidatePrintSettings](../api-1458994-pmsessionvalidateprintsettings.md)
  Validates a print settings object within the context of the specified printing session.
- [PMPrintSettingsCreateDataRepresentation](../api-1464570-pmprintsettingscreatedatareprese.md)
  Creates a data representation of a print settings object.
- [PMPrintSettingsCreateWithDataRepresentation](../api-1462203-pmprintsettingscreatewithdatarep.md)
  Creates a print settings object from a data representation.
- [PMFlattenPrintSettings](./api-1805469-pmflattenprintsettings.md)
  Flattens a print settings object into a Memory Manager handle for storage in a user document.
- [PMFlattenPrintSettingsToCFData](./api-1805472-pmflattenprintsettingstocfdata.md)
  Flattens a print settings object into a Core Foundation data object for storage in a user document.
- [PMUnflattenPrintSettings](./api-1805476-pmunflattenprintsettings.md)
  Rebuilds a print settings object from a Memory Manager handle that contains flattened print settings data.
- [PMUnflattenPrintSettingsWithCFData](./api-1805479-pmunflattenprintsettingswithcfda.md)
  Rebuilds a print settings object from a Core Foundation data object that contains flattened print settings data.
- [PMUnflattenPrintSettingsWithURL](./api-1805481-pmunflattenprintsettingswithurl.md)
  Rebuilds a print settings object from a file that contains flattened print settings data.
- [PMCopyPrintSettings](../api-1462491-pmcopyprintsettings.md)
  Copies the settings from one print settings object into another. 
- [PMPrintSettingsToOptions](../api-1459069-pmprintsettingstooptions.md)
  Converts print settings into a CUPS options string.
- [PMPrintSettingsToOptionsWithPrinterAndPageFormat](../api-1459435-pmprintsettingstooptionswithprin.md)
  Converts print settings and page format data into a CUPS options string for a specified printer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/core_printing/1805473-pmflattenprintsettingstourl)*