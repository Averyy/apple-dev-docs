# Data Array Constants

**Framework**: Core Services  
**Kind**: enum  
**Role**: Enumeration

Specify an array type for storing or extracting descriptor lists with the `AEPutArray` and `AEGetArray` functions.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
enum : unsigned int {
    ...
};
```

## Topics

### Constants
- [kAEDataArray](./api-1542848-data_array_constants/kaedataarray.md)
  Array items consist of data of the same size and same type, and are aligned on word boundaries.
- [kAEPackedArray](./api-1542848-data_array_constants/kaepackedarray.md)
  Array items consist of data of the same size and same type, and are packed without regard for word boundaries.
- [kAEDescArray](./api-1542848-data_array_constants/kaedescarray.md)
  Array items consist of descriptors of different descriptor types with data of variable size.
- [kAEKeyDescArray](./api-1542848-data_array_constants/kaekeydescarray.md)
  Array items consist of keyword-specified descriptors with different keywords, different descriptor types, and data of variable size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1542848-data_array_constants)*