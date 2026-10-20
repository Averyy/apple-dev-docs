# PasteboardCopyName(_:_:)

**Framework**: Application Services  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.4+

## Declaration

```swift
func PasteboardCopyName(_ inPasteboard: Pasteboard, _ outName: UnsafeMutablePointer<CFString?>) -> OSStatus
```

```c
OSStatus PasteboardCopyName(PasteboardRef inPasteboard, CFStringRef  _Nullable *outName);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1459455-pasteboardcopyname)*