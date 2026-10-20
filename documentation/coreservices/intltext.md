# IntlText

**Framework**: Core Services  
**Kind**: struct  
**Role**: Structure

International text consists of an ordered series of bytes, beginning with a 4-byte language code and a 4-byte script code that together determine the format of the bytes that follow.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

> **Deprecated**: Use Unicode text instead.

## Declaration

```swift
struct IntlText
```

```c
typedef struct IntlText {
    ...
} IntlText;
```

## Topics

### Initializers
- [init()](./intltext/api-1449738-init.md)
- [init(theScriptCode: ScriptCode, theLangCode: LangCode, theText: CChar)](./intltext/api-1442684-init.md)
### Instance Properties
- [var theLangCode: LangCode](./intltext/api-1441911-thelangcode.md)
- [var theScriptCode: ScriptCode](./intltext/api-1441824-thescriptcode.md)
- [var theText: CChar](./intltext/api-1442075-thetext.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/intltext)*