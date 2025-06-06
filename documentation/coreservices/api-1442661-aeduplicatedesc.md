# AEDuplicateDesc(_:_:)

**Framework**: Core Services  
**Kind**: func

Creates a copy of a descriptor.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func AEDuplicateDesc(_ theAEDesc: UnsafePointer<AEDesc>!, _ result: UnsafeMutablePointer<AEDesc>!) -> OSErr
```

#### Return_value

A result code. See [`Result Codes`](https://developer.apple.com/documentation/applicationservices/apple_event_manager#1656145).

#### Discussion

It is common for applications to send Apple events that have one or more attributes or parameters in common. For example, if you send a series of Apple events to the same application, the address attribute is the same. In these cases, the most efficient way to create the necessary Apple events is to make a template Apple event that you can then copy—by calling the `AEDuplicateDesc` function—as needed. You then fill in or change the remaining parameters and attributes of the copy, send the copy by calling the `AESend(_:_:_:_:_:_:_:)` function and, after `AESend` returns a result code, dispose of the copy by calling [`AEDisposeDesc(_:)`](1444208-aedisposedesc.md). You can use this approach to prepare structures of type [`AEDesc`](aedesc.md), [`AEDescList`](aedesclist.md), [`AERecord`](aerecord.md), and [`AppleEvent`](appleevent.md). 

##### 1770174

Thread safe starting in OS X v10.2.

## Parameters

- `theAEDesc`: A pointer to the descriptor to duplicate. See  .
- `result`: A pointer to a descriptor. On return, the descriptor contains a copy of the descriptor specified by the   parameter. If the function returns successfully, your application should call the   function to dispose of the resulting descriptor after it has finished using it.

## See Also

- [func AECreateDesc(DescType, UnsafeRawPointer!, Size, UnsafeMutablePointer<AEDesc>!) -> OSErr](1448535-aecreatedesc.md)
  Creates a new descriptor that incorporates the specified data.
- [func AECreateDescFromExternalPtr(OSType, UnsafeRawPointer!, Size, AEDisposeExternalUPP!, SRefCon!, UnsafeMutablePointer<AEDesc>!) -> OSStatus](1446239-aecreatedescfromexternalptr.md)
  Creates a new descriptor that uses a memory buffer supplied by the caller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1442661-aeduplicatedesc)*