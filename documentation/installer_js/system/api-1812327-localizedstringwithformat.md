# localizedStringWithFormat

**Framework**: Installer JS  
**Kind**: instm

Provides the formatted localized string in the installation package for the current locale, for a given key and a set of additional arguments.

## Declaration

```swift
localizedStringWithFormat(stringKey, args...)
```

#### Return_value

The localized string, if found in the installation package; `null` otherwise.

## Parameters

- `stringKey`: A string that identifies the desired localized string.
- `args...`: Arguments that replace placeholders ( ) in the formatted localized string.

## See Also

- [localizedString](system/1812321-localizedstring.md)
  Provides the localized string in the installation package for the current locale for a given key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/installer_js/system/1812327-localizedstringwithformat)*