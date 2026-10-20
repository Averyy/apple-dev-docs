# PasteboardCreate(_:_:)

**Framework**: Application Services  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.3+

## Declaration

```swift
func PasteboardCreate(_ inName: CFString?, _ outPasteboard: UnsafeMutablePointer<Pasteboard?>) -> OSStatus
```

```c
OSStatus PasteboardCreate(CFStringRef inName, PasteboardRef  _Nullable *outPasteboard);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1461248-pasteboardcreate)*