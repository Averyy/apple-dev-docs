# PasteboardCopyItemFlavors(_:_:_:)

**Framework**: Application Services  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.3+

## Declaration

```swift
func PasteboardCopyItemFlavors(_ inPasteboard: Pasteboard, _ inItem: PasteboardItemID, _ outFlavorTypes: UnsafeMutablePointer<CFArray?>) -> OSStatus
```

```c
OSStatus PasteboardCopyItemFlavors(PasteboardRef inPasteboard, PasteboardItemID inItem, CFArrayRef  _Nullable *outFlavorTypes);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1460005-pasteboardcopyitemflavors)*