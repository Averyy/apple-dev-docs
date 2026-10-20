# CSDiskSpaceRecoveryCallback

**Framework**: Core Services  
**Kind**: tdef  
**Role**: Type Alias

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.7+

## Declaration

```swift
typealias CSDiskSpaceRecoveryCallback = (Bool, UInt64, CFError?) -> Void
```

```c
typedef void (^CSDiskSpaceRecoveryCallback)(Boolean succeeded, UInt64 bytesFree, CFErrorRef error);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/csdiskspacerecoverycallback)*