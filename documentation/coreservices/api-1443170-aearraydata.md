# AEArrayData

**Framework**: Core Services  
**Kind**: union  
**Role**: Union

Stores array information to be put into a descriptor listwith the `AEPutArray` functionor extracted from a descriptor list with the `AEGetArray` function.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
typedef union AEArrayData {
    ...
} AEArrayData;
```

## Discussion

When your application calls the [`AEPutArray`](./api-1442535-aeputarray.md) function to put informationinto a descriptor list or the [`AEGetArray`](./api-1445720-aegetarray.md) functionto get information from a descriptor list, it uses an to store theinformation. The type of array depends on the data for the array,as specified by one of the constants described in [Data Array Constants](./api-1542848-data_array_constants.md).

Array items in Apple event arrays of type `kAEDataArray`, `kAEPackedArray`,or `kAEHandleArray` mustbe factored—that is, contained in a factored descriptor list.Before adding array items to a factored descriptor list, you shouldprovide both a pointer to the data that is common to all array itemsand the size of that common data when you first call [`AECreateList`](./api-1448643-aecreatelist.md) to createa factored descriptor list. When you call `AEPutArray` toadd the array data to such a descriptor list, the Apple Event Managerautomatically isolates the common data you specified in the callto `AECreateList`.

When you call `AEGetArray` or `AEPutArray`,you specify a pointer of data type `AEArrayDataPointer` thatpoints to a buffer containing the data for the array. 

## Topics

### Instance Properties
- [kAEDataArray](./api-1443170-aearraydata/api-1443096-kaedataarray.md)
- [kAEDescArray](./api-1443170-aearraydata/api-1442921-kaedescarray.md)
- [kAEHandleArray](./api-1443170-aearraydata/api-1444461-kaehandlearray.md)
- [kAEKeyDescArray](./api-1443170-aearraydata/api-1444282-kaekeydescarray.md)
- [kAEPackedArray](./api-1443170-aearraydata/api-1449947-kaepackedarray.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1443170-aearraydata)*