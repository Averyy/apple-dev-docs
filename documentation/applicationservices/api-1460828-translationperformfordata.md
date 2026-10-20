# TranslationPerformForData(_:_:_:)

**Framework**: Application Services  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.3+

## Declaration

```swift
func TranslationPerformForData(_ inTranslation: Translation!, _ inSourceData: CFData!, _ outDestinationData: UnsafeMutablePointer<Unmanaged<CFData>?>!) -> OSStatus
```

```c
OSStatus TranslationPerformForData(TranslationRef inTranslation, CFDataRef inSourceData, CFDataRef *outDestinationData);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1460828-translationperformfordata)*