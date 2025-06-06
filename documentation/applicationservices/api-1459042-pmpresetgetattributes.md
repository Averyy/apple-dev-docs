# PMPresetGetAttributes(_:_:)

**Framework**: Application Services  
**Kind**: func

Obtains the attributes of a preset.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func PMPresetGetAttributes(_ preset: PMPreset, _ attributes: UnsafeMutablePointer<Unmanaged<CFDictionary>?>) -> OSStatus
```

#### Return_value

A result code. See [`Result Codes`](core_printing#1670007.md).

#### Discussion

A preset has associated with it a dictionary containing the preset identifier, the localized name, and a description of the environment for which the preset is intended. In addition to these standard attributes, the preset you specify may contain additional attributes that reflect custom print settings.

## Parameters

- `preset`: The preset whose attributes you want to obtain. You can use the function   to obtain the presets for a given printer.
- `attributes`: A pointer to your   variable. On return, the variable refers to a Core Foundation dictionary containing the attributes of the specified preset, or   if the attributes could not be obtained. For more information about these attributes, see the Discussion. You should not release this dictionary without first retaining it.

## See Also

- [func PMPresetCopyName(PMPreset, UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus](1460343-pmpresetcopyname.md)
  Obtains the localized name for a preset.
- [func PMPresetCreatePrintSettings(PMPreset, PMPrintSession, UnsafeMutablePointer<PMPrintSettings?>) -> OSStatus](1463414-pmpresetcreateprintsettings.md)
  Creates a print settings object with settings that correspond to a preset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1459042-pmpresetgetattributes)*