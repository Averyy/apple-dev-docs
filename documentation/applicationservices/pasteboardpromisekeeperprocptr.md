# PasteboardPromiseKeeperProcPtr

**Framework**: Application Services  
**Kind**: tdef  
**Role**: Type Alias

**Availability**:
- macOS 10.3+

## Declaration

```swift
typealias PasteboardPromiseKeeperProcPtr = (Pasteboard, PasteboardItemID, CFString, UnsafeMutableRawPointer?) -> OSStatus
```

```c
typedef OSStatus (*PasteboardPromiseKeeperProcPtr)(PasteboardRef pasteboard, PasteboardItemID item, CFStringRef flavorType, void *context);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/pasteboardpromisekeeperprocptr)*