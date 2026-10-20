# PasteboardCopyItemFlavorData(_:_:_:_:)

**Framework**: Application Services  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.3+

## Declaration

```swift
func PasteboardCopyItemFlavorData(_ inPasteboard: Pasteboard, _ inItem: PasteboardItemID, _ inFlavorType: CFString, _ outData: UnsafeMutablePointer<CFData?>) -> OSStatus
```

```c
OSStatus PasteboardCopyItemFlavorData(PasteboardRef inPasteboard, PasteboardItemID inItem, CFStringRef inFlavorType, CFDataRef  _Nullable *outData);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1458917-pasteboardcopyitemflavordata)*