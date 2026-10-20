# PasteboardGetItemFlavorFlags(_:_:_:_:)

**Framework**: Application Services  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.3+

## Declaration

```swift
func PasteboardGetItemFlavorFlags(_ inPasteboard: Pasteboard, _ inItem: PasteboardItemID, _ inFlavorType: CFString, _ outFlags: UnsafeMutablePointer<PasteboardFlavorFlags>) -> OSStatus
```

```c
OSStatus PasteboardGetItemFlavorFlags(PasteboardRef inPasteboard, PasteboardItemID inItem, CFStringRef inFlavorType, PasteboardFlavorFlags *outFlags);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1459353-pasteboardgetitemflavorflags)*