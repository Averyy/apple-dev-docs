# TranslationCreateWithSourceArray(_:_:_:_:)

**Framework**: Application Services  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.3+

## Declaration

```swift
func TranslationCreateWithSourceArray(_ inSourceTypes: CFArray!, _ inTranslationFlags: TranslationFlags, _ outDestinationTypes: UnsafeMutablePointer<Unmanaged<CFArray>?>!, _ outTranslations: UnsafeMutablePointer<Unmanaged<CFDictionary>?>!) -> OSStatus
```

```c
OSStatus TranslationCreateWithSourceArray(CFArrayRef inSourceTypes, TranslationFlags inTranslationFlags, CFArrayRef *outDestinationTypes, CFDictionaryRef *outTranslations);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1464306-translationcreatewithsourcearray)*