# PMPresetGetAttributes(_:_:)

**Framework**: Application Services  
**Kind**: func  
**Role**: Function

Obtains the attributes of a preset.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func PMPresetGetAttributes(_ preset: PMPreset, _ attributes: UnsafeMutablePointer<Unmanaged<CFDictionary>?>) -> OSStatus
```

```c
OSStatus PMPresetGetAttributes(PMPreset preset, CFDictionaryRef  _Nullable *attributes);
```

#### Return Value

A result code. See [Result Codes](./core_printing.md#1670007).

#### Discussion

A preset has associated with it a dictionary containing the preset identifier, the localized name, and a description of the environment for which the preset is intended. In addition to these standard attributes, the preset you specify may contain additional attributes that reflect custom print settings.

## Parameters

- `preset`: The preset whose attributes you want to obtain. You can use the function [`PMPrinterCopyPresets(_:_:)`](./api-1459117-pmprintercopypresets.md) to obtain the presets for a given printer.
- `attributes`: A pointer to your [`CFDictionary`](../CoreFoundation/cfdictionary.md) variable. On return, the variable refers to a Core Foundation dictionary containing the attributes of the specified preset, or `NULL` if the attributes could not be obtained. For more information about these attributes, see the Discussion. You should not release this dictionary without first retaining it.

## See Also

### Using Printer Presets
- [func PMPresetCopyName(PMPreset, UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus](./api-1460343-pmpresetcopyname.md)
  Obtains the localized name for a preset.
- [func PMPresetCreatePrintSettings(PMPreset, PMPrintSession, UnsafeMutablePointer<PMPrintSettings?>) -> OSStatus](./api-1463414-pmpresetcreateprintsettings.md)
  Creates a print settings object with settings that correspond to a preset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1459042-pmpresetgetattributes)*