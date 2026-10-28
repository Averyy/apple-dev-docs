# AESizeOfFlattenedDesc(_:)

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Returns the amount of buffer space needed to store the descriptor after flattening it.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func AESizeOfFlattenedDesc(_ theAEDesc: UnsafePointer<AEDesc>!) -> Size
```

```c
Size AESizeOfFlattenedDesc(const AEDesc *theAEDesc);
```

## Return Value

The size, in bytes, required to store the flattened descriptor.

## Discussion

You call this function before calling [`AEFlattenDesc(_:_:_:_:)`](./api-1441808-aeflattendesc.md) to determine the required size of the buffer for the flatten operation.

### Version-Notes

Thread safe starting in OS X v10.2.

## Parameters

- `theAEDesc`: A pointer to the descriptor to be flattened. See [`AEDesc`](./aedesc.md).

## See Also

### Serializing Apple Event Data
- [func AEFlattenDesc(UnsafePointer<AEDesc>!, Ptr!, Size, UnsafeMutablePointer<Size>!) -> OSStatus](./api-1441808-aeflattendesc.md)
  Flattens the specified descriptor and stores the data in the supplied buffer.
- [func AEUnflattenDesc(UnsafeRawPointer!, UnsafeMutablePointer<AEDesc>!) -> OSStatus](./api-1448997-aeunflattendesc.md)
  Unflattens the data in the passed buffer and creates a descriptor from it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1447305-aesizeofflatteneddesc)*