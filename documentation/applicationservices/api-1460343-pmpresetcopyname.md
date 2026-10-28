# PMPresetCopyName(_:_:)

**Framework**: Application Services  
**Kind**: func  
**Role**: Function

Obtains the localized name for a preset.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func PMPresetCopyName(_ preset: PMPreset, _ name: UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus
```

```c
OSStatus PMPresetCopyName(PMPreset preset, CFStringRef  _Nullable *name);
```

## Return Value

A result code. See [Result Codes](./core_printing.md#1670007).

## Parameters

- `preset`: The preset object whose localized name you want to obtain. You can use the function [`PMPrinterCopyPresets(_:_:)`](./api-1459117-pmprintercopypresets.md) to obtain the presets for a given printer.
- `paperID`: A pointer to your [`CFString`](../CoreFoundation/cfstring.md) variable. On return, the variable refers to a Core Foundation string containing the localized name of the specified preset. You are responsible for releasing the string.

## See Also

### Using Printer Presets
- [func PMPresetCreatePrintSettings(PMPreset, PMPrintSession, UnsafeMutablePointer<PMPrintSettings?>) -> OSStatus](./api-1463414-pmpresetcreateprintsettings.md)
  Creates a print settings object with settings that correspond to a preset.
- [func PMPresetGetAttributes(PMPreset, UnsafeMutablePointer<Unmanaged<CFDictionary>?>) -> OSStatus](./api-1459042-pmpresetgetattributes.md)
  Obtains the attributes of a preset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1460343-pmpresetcopyname)*