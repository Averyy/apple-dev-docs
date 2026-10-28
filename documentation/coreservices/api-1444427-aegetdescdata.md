# AEGetDescData(_:_:_:)

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Gets the data from the specified descriptor.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func AEGetDescData(_ theAEDesc: UnsafePointer<AEDesc>!, _ dataPtr: UnsafeMutableRawPointer!, _ maximumSize: Size) -> OSErr
```

```c
OSErr AEGetDescData(const AEDesc *theAEDesc, void *dataPtr, Size maximumSize);
```

## Return Value

A result code. See [Result Codes](../applicationservices/apple_event_manager.md#1656145).

## Discussion

Your application can call [`AEGetDescDataSize(_:)`](./api-1450119-aegetdescdatasize.md) to get the size, in bytes, of the data in a descriptor, allocate a buffer or variable of that size, then call `AEGetDescData` to get the data.

This function works only with value descriptors created by [`AECreateDesc(_:_:_:_:)`](./api-1448535-aecreatedesc.md). You cannot get the data of an [`AERecord`](./aerecord.md) or [`AEDescList`](./aedesclist.md), for example.

### Version-Notes

Thread safe starting in OS X v10.2.

## Parameters

- `theAEDesc`: A pointer to the descriptor to get the data from. See [`AEDesc`](./aedesc.md).
- `dataPtr`: A pointer to a buffer, local variable, or other storage location created and disposed of by your application. The size in bytes should be the same as the value you pass in the `maximumSize` parameter. On return, contains the data from the descriptor.
- `maximumSize`: The length, in bytes, of the expected descriptor data. The `AEGetDescData` function will not return more data than you specify in this parameter. You typically determine the maximum size by calling [`AEGetDescDataSize(_:)`](./api-1450119-aegetdescdatasize.md).

## See Also

### Operating On Descriptor Data
- [func AEGetDescDataSize(UnsafePointer<AEDesc>!) -> Size](./api-1450119-aegetdescdatasize.md)
  Gets the size, in bytes, of the data in the specified descriptor.
- [func AEGetDescDataRange(UnsafePointer<AEDesc>!, UnsafeMutableRawPointer!, Size, Size) -> OSStatus](./api-1446560-aegetdescdatarange.md)
  Retrieves a specified series of bytes from the specified descriptor.
- [func AEReplaceDescData(DescType, UnsafeRawPointer!, Size, UnsafeMutablePointer<AEDesc>!) -> OSErr](./api-1446695-aereplacedescdata.md)
  Copies the specified data into the specified descriptor, replacing any previous data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1444427-aegetdescdata)*