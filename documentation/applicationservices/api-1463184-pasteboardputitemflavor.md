# PasteboardPutItemFlavor(_:_:_:_:_:)

**Framework**: Application Services  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.3+

## Declaration

```swift
func PasteboardPutItemFlavor(_ inPasteboard: Pasteboard, _ inItem: PasteboardItemID, _ inFlavorType: CFString, _ inData: CFData?, _ inFlags: PasteboardFlavorFlags) -> OSStatus
```

```c
OSStatus PasteboardPutItemFlavor(PasteboardRef inPasteboard, PasteboardItemID inItem, CFStringRef inFlavorType, CFDataRef inData, PasteboardFlavorFlags inFlags);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1463184-pasteboardputitemflavor)*