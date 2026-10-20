# PasteboardCopyPasteLocation(_:_:)

**Framework**: Application Services  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.3+

## Declaration

```swift
func PasteboardCopyPasteLocation(_ inPasteboard: Pasteboard, _ outPasteLocation: UnsafeMutablePointer<CFURL?>) -> OSStatus
```

```c
OSStatus PasteboardCopyPasteLocation(PasteboardRef inPasteboard, CFURLRef  _Nullable *outPasteLocation);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1462546-pasteboardcopypastelocation)*