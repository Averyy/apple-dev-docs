# CSIdentityQueryExecuteAsynchronously(_:_:_:_:_:)

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.5+

## Declaration

```swift
func CSIdentityQueryExecuteAsynchronously(_ query: CSIdentityQuery!, _ flags: CSIdentityQueryFlags, _ clientContext: UnsafePointer<CSIdentityQueryClientContext>!, _ runLoop: CFRunLoop!, _ runLoopMode: CFString!) -> Bool
```

```c
Boolean CSIdentityQueryExecuteAsynchronously(CSIdentityQueryRef query, CSIdentityQueryFlags flags, const CSIdentityQueryClientContext *clientContext, CFRunLoopRef runLoop, CFStringRef runLoopMode);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1429011-csidentityqueryexecuteasynchrono)*