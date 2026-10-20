# TranslationCreate(_:_:_:_:)

**Framework**: Application Services  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.3+

## Declaration

```swift
func TranslationCreate(_ inSourceType: CFString!, _ inDestinationType: CFString!, _ inTranslationFlags: TranslationFlags, _ outTranslation: UnsafeMutablePointer<Unmanaged<Translation>?>!) -> OSStatus
```

```c
OSStatus TranslationCreate(CFStringRef inSourceType, CFStringRef inDestinationType, TranslationFlags inTranslationFlags, TranslationRef *outTranslation);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1459231-translationcreate)*