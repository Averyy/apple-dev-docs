# AEGetDescDataSize(_:)

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Gets the size, in bytes, of the data in the specified descriptor.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func AEGetDescDataSize(_ theAEDesc: UnsafePointer<AEDesc>!) -> Size
```

```c
Size AEGetDescDataSize(const AEDesc *theAEDesc);
```

#### Return Value

Returns the size, in bytes, of the data in the specified descriptor.

#### Discussion

This function works only with value descriptors created by [`AECreateDesc(_:_:_:_:)`](./api-1448535-aecreatedesc.md). You cannot get the data size of an [`AERecord`](./aerecord.md) or [`AEDescList`](./aedesclist.md), for example.

##### Version-Notes

Thread safe starting in OS X v10.2.

## Parameters

- `theAEDesc`: A pointer to the descriptor to obtain the data size for. See [`AEDesc`](./aedesc.md).

## See Also

### Operating On Descriptor Data
- [func AEGetDescData(UnsafePointer<AEDesc>!, UnsafeMutableRawPointer!, Size) -> OSErr](./api-1444427-aegetdescdata.md)
  Gets the data from the specified descriptor.
- [func AEGetDescDataRange(UnsafePointer<AEDesc>!, UnsafeMutableRawPointer!, Size, Size) -> OSStatus](./api-1446560-aegetdescdatarange.md)
  Retrieves a specified series of bytes from the specified descriptor.
- [func AEReplaceDescData(DescType, UnsafeRawPointer!, Size, UnsafeMutablePointer<AEDesc>!) -> OSErr](./api-1446695-aereplacedescdata.md)
  Copies the specified data into the specified descriptor, replacing any previous data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1450119-aegetdescdatasize)*