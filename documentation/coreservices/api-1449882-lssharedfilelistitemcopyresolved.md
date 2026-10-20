# LSSharedFileListItemCopyResolvedURL(_:_:_:)

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.10+ - Deprecated in 10.11

## Declaration

```swift
func LSSharedFileListItemCopyResolvedURL(_ inItem: LSSharedFileListItem, _ inFlags: LSSharedFileListResolutionFlags, _ outError: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Unmanaged<CFURL>?
```

```c
CFURLRef LSSharedFileListItemCopyResolvedURL(LSSharedFileListItemRef inItem, LSSharedFileListResolutionFlags inFlags, CFErrorRef  _Nullable *outError);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1449882-lssharedfilelistitemcopyresolved)*