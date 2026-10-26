# kSKLanguageTypes

**Framework**: Core Services  
**Kind**: data  
**Role**: Global Variable

**Availability**:
- macOS 10.3+ - Deprecated in 10.4

## Declaration

```c
const CFStringRef kSKLanguageTypes;
```

#### Discussion

Deprecated—Search Kit ignores this constant.

In releases of macOS previous to version 10.4, each string in this key’s corresponding value specifies a language to use for indexing. Each such string is a two character ISO 639-1 code. For example, `'en'` for English, `'ja'` for Japanese, and so on. If this key is not present, Search Kit uses the macOS preferences system to determine the primary language from the user’s locale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/ksklanguagetypes)*