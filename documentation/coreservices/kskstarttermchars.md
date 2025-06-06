# kSKStartTermChars

**Framework**: Core Services  
**Kind**: data

**Availability**:
- macOS 10.4+

## Declaration

```swift
let kSKStartTermChars: CFString!
```

#### Discussion

Additional valid starting-position “word” characters for indexing and querying. The corresponding value, a CFString object, specifies the additional valid “word” characters that you want to be considered as valid starting characters of terms for indexing and querying. “Word” characters are contrasted with nonword characters, such as spaces.

The value of `kSKStartTermChars`, if this key is present, overrides the value of `kSKTermChars` for the first character of a term.

By default, Search Kit considers alphanumeric characters as valid starting characters for terms, and considers all others (including the underscore character) to be nonword characters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/kskstarttermchars)*