# AEReplaceDescData(_:_:_:_:)

**Framework**: Core Services  
**Kind**: func

Copies the specified data into the specified descriptor, replacing any previous data.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func AEReplaceDescData(_ typeCode: DescType, _ dataPtr: UnsafeRawPointer!, _ dataSize: Size, _ theAEDesc: UnsafeMutablePointer<AEDesc>!) -> OSErr
```

#### Return_value

A result code. See [`Result Codes`](https://developer.apple.com/documentation/applicationservices/apple_event_manager#1656145).

#### Discussion

Thread safe starting in OS X v10.2.

## Parameters

- `typeCode`: Specifies the descriptor type of the data pointed to by  . For a list of AppleScript’s predefined descriptor types, see  . See  .
- `dataPtr`: A pointer to the data to store in the specified descriptor.
- `dataSize`: The size, in bytes, of the data pointed to by the   parameter. 
- `theAEDesc`: A pointer to a descriptor. On return, contains the copied data. See  .

## See Also

- [func AEGetDescData(UnsafePointer<AEDesc>!, UnsafeMutableRawPointer!, Size) -> OSErr](1444427-aegetdescdata.md)
  Gets the data from the specified descriptor.
- [func AEGetDescDataSize(UnsafePointer<AEDesc>!) -> Size](1450119-aegetdescdatasize.md)
  Gets the size, in bytes, of the data in the specified descriptor.
- [func AEGetDescDataRange(UnsafePointer<AEDesc>!, UnsafeMutableRawPointer!, Size, Size) -> OSStatus](1446560-aegetdescdatarange.md)
  Retrieves a specified series of bytes from the specified descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1446695-aereplacedescdata)*