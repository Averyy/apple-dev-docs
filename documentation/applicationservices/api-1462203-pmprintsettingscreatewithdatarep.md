# PMPrintSettingsCreateWithDataRepresentation(_:_:)

**Framework**: Application Services  
**Kind**: func

Creates a print settings object from a data representation.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func PMPrintSettingsCreateWithDataRepresentation(_ data: CFData, _ printSettings: UnsafeMutablePointer<PMPrintSettings?>) -> OSStatus
```

#### Return_value

A result code. See [`Result Codes`](core_printing#1670007.md).

#### Discussion

This function is typically used to convert a data representation stored in a user document back into a print settings object. For information about creating a Core Foundation data object from raw data, see `CFData`.

After calling this function, you should call the function [`PMSessionValidatePrintSettings(_:_:_:)`](1458994-pmsessionvalidateprintsettings.md) to make sure the print settings object contains valid values.

## Parameters

- `data`: The data representation of a print settings object. The data representation must have been previously created with the function  .
- `printSettings`: A pointer to your   variable. On return, the variable refers to a new print settings object that contains the printing information stored in the specified data object. You are responsible for releasing the print settings object with the function  .

## See Also

- [func PMCreatePrintSettings(UnsafeMutablePointer<PMPrintSettings?>) -> OSStatus](1463239-pmcreateprintsettings.md)
  Creates a new print settings object.
- [func PMSessionDefaultPrintSettings(PMPrintSession, PMPrintSettings) -> OSStatus](1460138-pmsessiondefaultprintsettings.md)
  Assigns default parameter values to a print settings object for the specified printing session.
- [func PMSessionValidatePrintSettings(PMPrintSession, PMPrintSettings, UnsafeMutablePointer<DarwinBoolean>?) -> OSStatus](1458994-pmsessionvalidateprintsettings.md)
  Validates a print settings object within the context of the specified printing session.
- [func PMPrintSettingsCreateDataRepresentation(PMPrintSettings, UnsafeMutablePointer<Unmanaged<CFData>?>, PMDataFormat) -> OSStatus](1464570-pmprintsettingscreatedatareprese.md)
  Creates a data representation of a print settings object.
- [func PMCopyPrintSettings(PMPrintSettings, PMPrintSettings) -> OSStatus](1462491-pmcopyprintsettings.md)
  Copies the settings from one print settings object into another. 
- [func PMPrintSettingsToOptions(PMPrintSettings, UnsafeMutablePointer<UnsafeMutablePointer<CChar>?>) -> OSStatus](1459069-pmprintsettingstooptions.md)
  Converts print settings into a CUPS options string.
- [func PMPrintSettingsToOptionsWithPrinterAndPageFormat(PMPrintSettings, PMPrinter, PMPageFormat?, UnsafeMutablePointer<UnsafeMutablePointer<CChar>?>) -> OSStatus](1459435-pmprintsettingstooptionswithprin.md)
  Converts print settings and page format data into a CUPS options string for a specified printer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1462203-pmprintsettingscreatewithdatarep)*