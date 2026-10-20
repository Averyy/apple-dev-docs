# TranslationPerformForURL(_:_:_:_:)

**Framework**: Application Services  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.3+

## Declaration

```swift
func TranslationPerformForURL(_ inTranslation: Translation!, _ inSourceURL: CFURL!, _ inDestinationURL: CFURL!, _ outTranslatedURL: UnsafeMutablePointer<Unmanaged<CFURL>?>!) -> OSStatus
```

```c
OSStatus TranslationPerformForURL(TranslationRef inTranslation, CFURLRef inSourceURL, CFURLRef inDestinationURL, CFURLRef *outTranslatedURL);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1460118-translationperformforurl)*