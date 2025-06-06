# PMPresetCopyName(_:_:)

**Framework**: Application Services  
**Kind**: func

Obtains the localized name for a preset.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func PMPresetCopyName(_ preset: PMPreset, _ name: UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus
```

#### Return_value

A result code. See [`Result Codes`](core_printing#1670007.md).

## Parameters

- `preset`: The preset object whose localized name you want to obtain. You can use the function   to obtain the presets for a given printer.
- `paperID`: A pointer to your   variable. On return, the variable refers to a Core Foundation string containing the localized name of the specified preset. You are responsible for releasing the string.

## See Also

- [func PMPresetCreatePrintSettings(PMPreset, PMPrintSession, UnsafeMutablePointer<PMPrintSettings?>) -> OSStatus](1463414-pmpresetcreateprintsettings.md)
  Creates a print settings object with settings that correspond to a preset.
- [func PMPresetGetAttributes(PMPreset, UnsafeMutablePointer<Unmanaged<CFDictionary>?>) -> OSStatus](1459042-pmpresetgetattributes.md)
  Obtains the attributes of a preset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1460343-pmpresetcopyname)*