# AEInitializeDesc(_:)

**Framework**: Core Services  
**Kind**: func

Initializes a new descriptor. 

**Availability**:
- macOS 10.0+

## Declaration

```swift
func AEInitializeDesc(_ desc: UnsafeMutablePointer<AEDesc>!)
```

#### Discussion

The function sets the type of the descriptor to `typeNull` and sets the data handle to `NULL`. If you need to initialize a descriptor that already has some data in it, use [`AEDisposeDesc(_:)`](1444208-aedisposedesc.md) to deallocate the memory and initialize the descriptor.

##### 1770232

Thread safe starting in OS X v10.2.

## Parameters

- `desc`: A pointer to a new descriptor. See  .

## See Also

- [func AECheckIsRecord(UnsafePointer<AEDesc>!) -> Bool](1444011-aecheckisrecord.md)
  Determines whether a descriptor is truly an `AERecord`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1446047-aeinitializedesc)*