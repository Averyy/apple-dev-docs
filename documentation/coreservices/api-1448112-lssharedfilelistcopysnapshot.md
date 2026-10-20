# LSSharedFileListCopySnapshot(_:_:)

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.5+ - Deprecated in 10.11

## Declaration

```swift
func LSSharedFileListCopySnapshot(_ inList: LSSharedFileList, _ outSnapshotSeed: UnsafeMutablePointer<UInt32>?) -> Unmanaged<CFArray>?
```

```c
CFArrayRef LSSharedFileListCopySnapshot(LSSharedFileListRef inList, UInt32 *outSnapshotSeed);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1448112-lssharedfilelistcopysnapshot)*