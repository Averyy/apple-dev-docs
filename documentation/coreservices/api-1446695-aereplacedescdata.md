# AEReplaceDescData(_:_:_:_:)

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Copies the specified data into the specified descriptor, replacing any previous data.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func AEReplaceDescData(_ typeCode: DescType, _ dataPtr: UnsafeRawPointer!, _ dataSize: Size, _ theAEDesc: UnsafeMutablePointer<AEDesc>!) -> OSErr
```

```c
OSErr AEReplaceDescData(DescType typeCode, const void *dataPtr, Size dataSize, AEDesc *theAEDesc);
```

## Return Value

A result code. See [Result Codes](../applicationservices/apple_event_manager.md#1656145).

## Discussion

Thread safe starting in OS X v10.2.

## Parameters

- `typeCode`: Specifies the descriptor type of the data pointed to by `dataPtr`. For a list of AppleScript’s predefined descriptor types, see [Descriptor Type Constants](./apple_events/api-1542788-descriptor_type_constants.md). See [`DescType`](./desctype.md).
- `dataPtr`: A pointer to the data to store in the specified descriptor.
- `dataSize`: The size, in bytes, of the data pointed to by the `dataSize` parameter. 
- `theAEDesc`: A pointer to a descriptor. On return, contains the copied data. See [`AEDesc`](./aedesc.md).

## See Also

### Operating On Descriptor Data
- [func AEGetDescData(UnsafePointer<AEDesc>!, UnsafeMutableRawPointer!, Size) -> OSErr](./api-1444427-aegetdescdata.md)
  Gets the data from the specified descriptor.
- [func AEGetDescDataSize(UnsafePointer<AEDesc>!) -> Size](./api-1450119-aegetdescdatasize.md)
  Gets the size, in bytes, of the data in the specified descriptor.
- [func AEGetDescDataRange(UnsafePointer<AEDesc>!, UnsafeMutableRawPointer!, Size, Size) -> OSStatus](./api-1446560-aegetdescdatarange.md)
  Retrieves a specified series of bytes from the specified descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1446695-aereplacedescdata)*