# PMCreatePrintSettings(_:)

**Framework**: Application Services  
**Kind**: func  
**Role**: Function

Creates a new print settings object.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func PMCreatePrintSettings(_ printSettings: UnsafeMutablePointer<PMPrintSettings?>) -> OSStatus
```

```c
OSStatus PMCreatePrintSettings(PMPrintSettings  _Nullable *printSettings);
```

#### Return Value

A result code. See [Result Codes](./core_printing.md#1670007).

#### Discussion

This function allocates memory for a new print settings object in your application’s memory space and sets its reference count to 1. The new print settings object is empty and unusable until you call [`PMSessionDefaultPrintSettings(_:_:)`](./api-1460138-pmsessiondefaultprintsettings.md) or [`PMCopyPrintSettings(_:_:)`](./api-1462491-pmcopyprintsettings.md).

## Parameters

- `printSettings`: A pointer to your [`PMPrintSettings`](./pmprintsettings.md) variable. On return, the variable refers to a new print settings object. You are responsible for releasing the print settings object with the function [`PMRelease(_:)`](./api-1461402-pmrelease.md).

## See Also

### Creating and Using Print Settings Objects
- [func PMSessionDefaultPrintSettings(PMPrintSession, PMPrintSettings) -> OSStatus](./api-1460138-pmsessiondefaultprintsettings.md)
  Assigns default parameter values to a print settings object for the specified printing session.
- [func PMSessionValidatePrintSettings(PMPrintSession, PMPrintSettings, UnsafeMutablePointer<DarwinBoolean>?) -> OSStatus](./api-1458994-pmsessionvalidateprintsettings.md)
  Validates a print settings object within the context of the specified printing session.
- [func PMPrintSettingsCreateDataRepresentation(PMPrintSettings, UnsafeMutablePointer<Unmanaged<CFData>?>, PMDataFormat) -> OSStatus](./api-1464570-pmprintsettingscreatedatareprese.md)
  Creates a data representation of a print settings object.
- [func PMPrintSettingsCreateWithDataRepresentation(CFData, UnsafeMutablePointer<PMPrintSettings?>) -> OSStatus](./api-1462203-pmprintsettingscreatewithdatarep.md)
  Creates a print settings object from a data representation.
- [func PMCopyPrintSettings(PMPrintSettings, PMPrintSettings) -> OSStatus](./api-1462491-pmcopyprintsettings.md)
  Copies the settings from one print settings object into another. 
- [func PMPrintSettingsToOptions(PMPrintSettings, UnsafeMutablePointer<UnsafeMutablePointer<CChar>?>) -> OSStatus](./api-1459069-pmprintsettingstooptions.md)
  Converts print settings into a CUPS options string.
- [func PMPrintSettingsToOptionsWithPrinterAndPageFormat(PMPrintSettings, PMPrinter, PMPageFormat?, UnsafeMutablePointer<UnsafeMutablePointer<CChar>?>) -> OSStatus](./api-1459435-pmprintsettingstooptionswithprin.md)
  Converts print settings and page format data into a CUPS options string for a specified printer.
- [PMFlattenPrintSettings](./core_printing/api-1805469-pmflattenprintsettings.md)
  Flattens a print settings object into a Memory Manager handle for storage in a user document.
- [PMFlattenPrintSettingsToCFData](./core_printing/api-1805472-pmflattenprintsettingstocfdata.md)
  Flattens a print settings object into a Core Foundation data object for storage in a user document.
- [PMFlattenPrintSettingsToURL](./core_printing/api-1805473-pmflattenprintsettingstourl.md)
  Flattens a print settings object into a URL for storage in a user document.
- [PMUnflattenPrintSettings](./core_printing/api-1805476-pmunflattenprintsettings.md)
  Rebuilds a print settings object from a Memory Manager handle that contains flattened print settings data.
- [PMUnflattenPrintSettingsWithCFData](./core_printing/api-1805479-pmunflattenprintsettingswithcfda.md)
  Rebuilds a print settings object from a Core Foundation data object that contains flattened print settings data.
- [PMUnflattenPrintSettingsWithURL](./core_printing/api-1805481-pmunflattenprintsettingswithurl.md)
  Rebuilds a print settings object from a file that contains flattened print settings data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1463239-pmcreateprintsettings)*