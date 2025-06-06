# AEGetDescData(_:_:_:)

**Framework**: Core Services  
**Kind**: func

Gets the data from the specified descriptor.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func AEGetDescData(_ theAEDesc: UnsafePointer<AEDesc>!, _ dataPtr: UnsafeMutableRawPointer!, _ maximumSize: Size) -> OSErr
```

#### Return_value

A result code. See [`Result Codes`](https://developer.apple.com/documentation/applicationservices/apple_event_manager#1656145).

#### Discussion

Your application can call [`AEGetDescDataSize(_:)`](1450119-aegetdescdatasize.md) to get the size, in bytes, of the data in a descriptor, allocate a buffer or variable of that size, then call `AEGetDescData` to get the data.

This function works only with value descriptors created by [`AECreateDesc(_:_:_:_:)`](1448535-aecreatedesc.md). You cannot get the data of an [`AERecord`](aerecord.md) or [`AEDescList`](aedesclist.md), for example.

##### 1770212

Thread safe starting in OS X v10.2.

## Parameters

- `theAEDesc`: A pointer to the descriptor to get the data from. See  .
- `dataPtr`: A pointer to a buffer, local variable, or other storage location created and disposed of by your application. The size in bytes should be the same as the value you pass in the   parameter. On return, contains the data from the descriptor.
- `maximumSize`: The length, in bytes, of the expected descriptor data. The   function will not return more data than you specify in this parameter. You typically determine the maximum size by calling  .

## See Also

- [func AEGetDescDataSize(UnsafePointer<AEDesc>!) -> Size](1450119-aegetdescdatasize.md)
  Gets the size, in bytes, of the data in the specified descriptor.
- [func AEGetDescDataRange(UnsafePointer<AEDesc>!, UnsafeMutableRawPointer!, Size, Size) -> OSStatus](1446560-aegetdescdatarange.md)
  Retrieves a specified series of bytes from the specified descriptor.
- [func AEReplaceDescData(DescType, UnsafeRawPointer!, Size, UnsafeMutablePointer<AEDesc>!) -> OSErr](1446695-aereplacedescdata.md)
  Copies the specified data into the specified descriptor, replacing any previous data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1444427-aegetdescdata)*