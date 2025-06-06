# kAXFontTextAttribute

**Framework**: Application Services  
**Kind**: data

A dictionary (a `CFDictionaryRef`) of two or more font keys.

**Availability**:
- macOS 10.4+

## Declaration

```swift
var kAXFontTextAttribute: Unmanaged<CFString>
```

#### Discussion

The dictionary associated with this attribute must contain the [`kAXFontNameKey`](kaxfontnamekey.md) and [`kAXFontSizeKey`](kaxfontsizekey.md) font keys. It may also contain the [`kAXFontFamilyKey`](kaxfontfamilykey.md) and [`kAXVisibleNameKey`](kaxvisiblenamekey.md) font keys.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/kaxfonttextattribute)*