# PMUnflattenPrintSettingsWithURL

**Framework**: Application Services  
**Kind**: func

Rebuilds a print settings object from a file that contains flattened print settings data.

> **Deprecated**: Instead read the data into a CFData object and use [`PMPrintSettingsCreateWithDataRepresentation`](../api-1462203-pmprintsettingscreatewithdatarep.md).

## Declaration

```c
OSStatus PMUnflattenPrintSettingsWithURL (
   CFURLRef flattenFileURL,
   PMPrintSettings *printSettings
);
```

#### Return Value

A result code. See [Result Codes](../core_printing.md#1670007).

## Parameters

- `flattenFileURL`: A file containing a flattened representation of a print settings object. 
- `printSettings`: A pointer to your [`PMPrintSettings`](../pmprintsettings.md) variable. On return, the variable refers to a print settings object rebuilt from the specified file. You are responsible for releasing the print settings object with the function [`PMRelease`](../api-1461402-pmrelease.md).

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
- [PMFlattenPrintSettingsToURL](./api-1805473-pmflattenprintsettingstourl.md)
  Flattens a print settings object into a URL for storage in a user document.
- [PMUnflattenPrintSettings](./api-1805476-pmunflattenprintsettings.md)
  Rebuilds a print settings object from a Memory Manager handle that contains flattened print settings data.
- [PMUnflattenPrintSettingsWithCFData](./api-1805479-pmunflattenprintsettingswithcfda.md)
  Rebuilds a print settings object from a Core Foundation data object that contains flattened print settings data.
- [PMCopyPrintSettings](../api-1462491-pmcopyprintsettings.md)
  Copies the settings from one print settings object into another. 
- [PMPrintSettingsToOptions](../api-1459069-pmprintsettingstooptions.md)
  Converts print settings into a CUPS options string.
- [PMPrintSettingsToOptionsWithPrinterAndPageFormat](../api-1459435-pmprintsettingstooptionswithprin.md)
  Converts print settings and page format data into a CUPS options string for a specified printer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/core_printing/1805481-pmunflattenprintsettingswithurl)*