# PMPresetCreatePrintSettings(_:_:_:)

**Framework**: Application Services  
**Kind**: func

Creates a print settings object with settings that correspond to a preset.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func PMPresetCreatePrintSettings(_ preset: PMPreset, _ session: PMPrintSession, _ printSettings: UnsafeMutablePointer<PMPrintSettings?>) -> OSStatus
```

#### Return_value

A result code. See [`Result Codes`](core_printing#1670007.md).

## Parameters

- `preset`: The preset whose settings you want to obtain. You can use the function   to obtain the presets for a given printer.
- `session`: The session you use to present the Print dialog.
- `printSettings`: A pointer to your   variable. On return, the variable refers to a print settings object with settings that correspond to the specified preset. You are responsible for releasing the print settings object with the function  .

## See Also

- [func PMPresetCopyName(PMPreset, UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus](1460343-pmpresetcopyname.md)
  Obtains the localized name for a preset.
- [func PMPresetGetAttributes(PMPreset, UnsafeMutablePointer<Unmanaged<CFDictionary>?>) -> OSStatus](1459042-pmpresetgetattributes.md)
  Obtains the attributes of a preset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1463414-pmpresetcreateprintsettings)*