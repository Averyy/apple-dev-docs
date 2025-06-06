# Data Array Constants

**Framework**: Core Services

Specify an array type for storing or extracting descriptor lists with the `AEPutArray` and `AEGetArray` functions.

#### Overview

When your application calls the [`AEPutArray(_:_:_:_:_:_:)`](1442535-aeputarray.md) function to put information into a descriptor list or the [`AEGetArray(_:_:_:_:_:_:_:)`](1445720-aegetarray.md) function to get information from a descriptor list, it uses an array to store the information. The type of array depends on the data for the array, as specified by one of these constants.

Array items in Apple event arrays of type `kAEDataArray`, `kAEPackedArray`, or `kAEHandleArray` must be factored—that is, contained in a factored descriptor list. For more information, see [`AEPutArray(_:_:_:_:_:_:)`](1442535-aeputarray.md). 

## Topics

### Constants
- [var kAEDataArray: Int](kaedataarray.md)
  Array items consist of data of the same size and same type, and are aligned on word boundaries.
- [var kAEPackedArray: Int](kaepackedarray.md)
  Array items consist of data of the same size and same type, and are packed without regard for word boundaries.
- [var kAEDescArray: Int](kaedescarray.md)
  Array items consist of descriptors of different descriptor types with data of variable size.
- [var kAEKeyDescArray: Int](kaekeydescarray.md)
  Array items consist of keyword-specified descriptors with different keywords, different descriptor types, and data of variable size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/apple_events/1542848-data_array_constants)*