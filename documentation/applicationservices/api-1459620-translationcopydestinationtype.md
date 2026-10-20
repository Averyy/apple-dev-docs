# TranslationCopyDestinationType(_:_:)

**Framework**: Application Services  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.3+

## Declaration

```swift
func TranslationCopyDestinationType(_ inTranslation: Translation!, _ outDestinationType: UnsafeMutablePointer<Unmanaged<CFString>?>!) -> OSStatus
```

```c
OSStatus TranslationCopyDestinationType(TranslationRef inTranslation, CFStringRef *outDestinationType);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1459620-translationcopydestinationtype)*