# PasteboardGetItemIdentifier(_:_:_:)

**Framework**: Application Services  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.3+

## Declaration

```swift
func PasteboardGetItemIdentifier(_ inPasteboard: Pasteboard, _ inIndex: CFIndex, _ outItem: UnsafeMutablePointer<PasteboardItemID?>) -> OSStatus
```

```c
OSStatus PasteboardGetItemIdentifier(PasteboardRef inPasteboard, CFIndex inIndex, PasteboardItemID  _Nullable *outItem);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1463412-pasteboardgetitemidentifier)*