# AEUnflattenDescFromBytes(_:_:_:)

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 11.0+

## Declaration

```swift
func AEUnflattenDescFromBytes(_ buffer: UnsafeRawPointer!, _ bufferLen: Int, _ result: UnsafeMutablePointer<AEDesc>!) -> OSStatus
```

```c
OSStatus AEUnflattenDescFromBytes(const void *buffer, size_t bufferLen, AEDesc *result);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/3553279-aeunflattendescfrombytes)*