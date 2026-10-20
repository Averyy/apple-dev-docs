# LSSharedFileListItemResolve(_:_:_:_:)

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.5+ - Deprecated in 10.10

## Declaration

```swift
func LSSharedFileListItemResolve(_ inItem: LSSharedFileListItem, _ inFlags: LSSharedFileListResolutionFlags, _ outURL: UnsafeMutablePointer<Unmanaged<CFURL>?>?, _ outRef: UnsafeMutablePointer<FSRef>?) -> OSStatus
```

```c
OSStatus LSSharedFileListItemResolve(LSSharedFileListItemRef inItem, LSSharedFileListResolutionFlags inFlags, CFURLRef  _Nullable *outURL, FSRef *outRef);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1447347-lssharedfilelistitemresolve)*