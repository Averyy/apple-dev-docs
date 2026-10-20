# LSSharedFileListInsertItemURL(_:_:_:_:_:_:_:)

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.5+ - Deprecated in 10.11

## Declaration

```swift
func LSSharedFileListInsertItemURL(_ inList: LSSharedFileList, _ insertAfterThisItem: LSSharedFileListItem, _ inDisplayName: CFString?, _ inIconRef: IconRef?, _ inURL: CFURL, _ inPropertiesToSet: CFDictionary?, _ inPropertiesToClear: CFArray?) -> LSSharedFileListItem?
```

```c
LSSharedFileListItemRef LSSharedFileListInsertItemURL(LSSharedFileListRef inList, LSSharedFileListItemRef insertAfterThisItem, CFStringRef inDisplayName, IconRef inIconRef, CFURLRef inURL, CFDictionaryRef inPropertiesToSet, CFArrayRef inPropertiesToClear);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1444471-lssharedfilelistinsertitemurl)*