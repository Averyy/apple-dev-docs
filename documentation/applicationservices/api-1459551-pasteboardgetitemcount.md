# PasteboardGetItemCount(_:_:)

**Framework**: Application Services  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.3+

## Declaration

```swift
func PasteboardGetItemCount(_ inPasteboard: Pasteboard, _ outItemCount: UnsafeMutablePointer<Int>) -> OSStatus
```

```c
OSStatus PasteboardGetItemCount(PasteboardRef inPasteboard, ItemCount *outItemCount);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1459551-pasteboardgetitemcount)*