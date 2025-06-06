# LSSharedFileListInsertItemFSRef(_:_:_:_:_:_:_:)

**Framework**: Core Services  
**Kind**: func

**Availability**:
- macOS 10.5+ - Deprecated in 10.10

## Declaration

```swift
func LSSharedFileListInsertItemFSRef(_ inList: LSSharedFileList, _ insertAfterThisItem: LSSharedFileListItem, _ inDisplayName: CFString?, _ inIconRef: IconRef?, _ inFSRef: UnsafePointer<FSRef>, _ inPropertiesToSet: CFDictionary?, _ inPropertiesToClear: CFArray?) -> LSSharedFileListItem?
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1449884-lssharedfilelistinsertitemfsref)*