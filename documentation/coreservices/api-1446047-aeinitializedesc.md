# AEInitializeDesc(_:)

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Initializes a new descriptor. 

**Availability**:
- macOS 10.0+

## Declaration

```swift
func AEInitializeDesc(_ desc: UnsafeMutablePointer<AEDesc>!)
```

```c
void AEInitializeDesc(AEDesc *desc);
```

## Discussion

The function sets the type of the descriptor to `typeNull` and sets the data handle to `NULL`. If you need to initialize a descriptor that already has some data in it, use [`AEDisposeDesc(_:)`](./api-1444208-aedisposedesc.md) to deallocate the memory and initialize the descriptor.

### Version-Notes

Thread safe starting in OS X v10.2.

## Parameters

- `desc`: A pointer to a new descriptor. See [`AEDesc`](./aedesc.md).

## See Also

### Miscellaneous
- [func AECheckIsRecord(UnsafePointer<AEDesc>!) -> Bool](./api-1444011-aecheckisrecord.md)
  Determines whether a descriptor is truly an `AERecord`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1446047-aeinitializedesc)*