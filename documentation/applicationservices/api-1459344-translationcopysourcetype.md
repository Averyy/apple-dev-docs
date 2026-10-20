# TranslationCopySourceType(_:_:)

**Framework**: Application Services  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.3+

## Declaration

```swift
func TranslationCopySourceType(_ inTranslation: Translation!, _ outSourceType: UnsafeMutablePointer<Unmanaged<CFString>?>!) -> OSStatus
```

```c
OSStatus TranslationCopySourceType(TranslationRef inTranslation, CFStringRef *outSourceType);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1459344-translationcopysourcetype)*