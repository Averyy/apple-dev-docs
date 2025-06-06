# AEDisposeDesc(_:)

**Framework**: Core Services  
**Kind**: func

Deallocates the memory used by a descriptor.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func AEDisposeDesc(_ theAEDesc: UnsafeMutablePointer<AEDesc>!) -> OSErr
```

#### Return_value

A result code. See [`Result Codes`](https://developer.apple.com/documentation/applicationservices/apple_event_manager#1656145). As currently implemented, `AEDisposeDesc` always returns `noErr`.

#### Discussion

The `AEDisposeDesc` function deallocates the memory used by a descriptor. After calling this method, the descriptor becomes an empty descriptor with a type of `typeNULL`. Because all Apple event structures (except for keyword-specified descriptors) are descriptors, you can use `AEDisposeDesc` for any of them.

Do not call `AEDisposeDesc` on a descriptor obtained from another Apple Event Manager function (such as the reply event from a call to `AESend(_:_:_:_:_:_:_:)`) unless that function returns successfully.

##### 1770178

If the `AEDesc` might contain an OSL token, dispose of it with [`AEDisposeToken(_:)`](1446783-aedisposetoken.md).

##### 1770179

Thread safe starting in OS X v10.2.

## Parameters

- `theAEDesc`: A pointer to the descriptor to deallocate. On return, a null descriptor. If you pass a null descriptor in this parameter,   returns  . See  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1444208-aedisposedesc)*