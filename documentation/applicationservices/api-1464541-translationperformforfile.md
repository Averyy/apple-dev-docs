# TranslationPerformForFile(_:_:_:_:_:)

**Framework**: Application Services  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.3+

## Declaration

```swift
func TranslationPerformForFile(_ inTranslation: Translation!, _ inSourceFile: UnsafePointer<FSRef>!, _ inDestinationDirectory: UnsafePointer<FSRef>!, _ inDestinationName: CFString!, _ outTranslatedFile: UnsafeMutablePointer<FSRef>!) -> OSStatus
```

```c
OSStatus TranslationPerformForFile(TranslationRef inTranslation, const FSRef *inSourceFile, const FSRef *inDestinationDirectory, CFStringRef inDestinationName, FSRef *outTranslatedFile);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1464541-translationperformforfile)*