# AEArrayData

**Framework**: Core Services  
**Kind**: struct

Stores array information to be put into a descriptor listwith the `AEPutArray` functionor extracted from a descriptor list with the `AEGetArray` function.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
struct AEArrayData
```

#### Overview

When your application calls the [`AEPutArray(_:_:_:_:_:_:)`](1442535-aeputarray.md) function to put informationinto a descriptor list or the [`AEGetArray(_:_:_:_:_:_:_:)`](1445720-aegetarray.md) functionto get information from a descriptor list, it uses an to store theinformation. The type of array depends on the data for the array,as specified by one of the constants described in [`Data Array Constants`](apple_events/1542848-data_array_constants.md).

Array items in Apple event arrays of type `kAEDataArray`, `kAEPackedArray`,or `kAEHandleArray` mustbe factored—that is, contained in a factored descriptor list.Before adding array items to a factored descriptor list, you shouldprovide both a pointer to the data that is common to all array itemsand the size of that common data when you first call [`AECreateList(_:_:_:_:)`](1448643-aecreatelist.md) to createa factored descriptor list. When you call `AEPutArray` toadd the array data to such a descriptor list, the Apple Event Managerautomatically isolates the common data you specified in the callto `AECreateList`.

When you call `AEGetArray` or `AEPutArray`,you specify a pointer of data type `AEArrayDataPointer` thatpoints to a buffer containing the data for the array. 

## Topics

### Instance Properties
- [var kAEDataArray: Int16](aearraydata/1443096-kaedataarray.md)
- [var kAEDescArray: AEDesc](aearraydata/1442921-kaedescarray.md)
- [var kAEHandleArray: Handle?](aearraydata/1444461-kaehandlearray.md)
- [var kAEKeyDescArray: AEKeyDesc](aearraydata/1444282-kaekeydescarray.md)
- [var kAEPackedArray: CChar](aearraydata/1449947-kaepackedarray.md)
### Initializers
- [init()](aearraydata/1447814-init.md)
- [init(kAEDataArray: Int16)](aearraydata/1442679-init.md)
- [init(kAEDescArray: AEDesc)](aearraydata/1450575-init.md)
- [init(kAEHandleArray: Handle?)](aearraydata/1448794-init.md)
- [init(kAEKeyDescArray: AEKeyDesc)](aearraydata/1442181-init.md)
- [init(kAEPackedArray: CChar)](aearraydata/1449681-init.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/aearraydata)*