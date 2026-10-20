# PasteboardSetPromiseKeeper(_:_:_:)

**Framework**: Application Services  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.3+

## Declaration

```swift
func PasteboardSetPromiseKeeper(_ inPasteboard: Pasteboard, _ inPromiseKeeper: PasteboardPromiseKeeperProcPtr, _ inContext: UnsafeMutableRawPointer?) -> OSStatus
```

```c
OSStatus PasteboardSetPromiseKeeper(PasteboardRef inPasteboard, PasteboardPromiseKeeperProcPtr inPromiseKeeper, void *inContext);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1463604-pasteboardsetpromisekeeper)*