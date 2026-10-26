# Key Output Index Masks

**Framework**: Core Services  
**Kind**: enum  
**Role**: Enumeration

Test the bits in `UCKeyOutput` values.

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
enum : unsigned int {
    ...
};
```

## Topics

### Constants
- [kUCKeyOutputStateIndexMask](./api-1390638-key_output_index_masks/kuckeyoutputstateindexmask.md)
  If the bit specified by this mask is set, the [`UCKeyStateRecordsIndex`](./uckeystaterecordsindex.md) `UCKeyOutput` value contains an index into a structure of type [`UCKeyStateRecordsIndex`](./uckeystaterecordsindex.md).
- [kUCKeyOutputSequenceIndexMask](./api-1390638-key_output_index_masks/kuckeyoutputsequenceindexmask.md)
  If the bit specified by this mask is set, the `UCKeyOutput` value contains an index into a structure of type [`UCKeySequenceDataIndex`](./uckeysequencedataindex.md).
- [kUCKeyOutputTestForIndexMask](./api-1390638-key_output_index_masks/kuckeyoutputtestforindexmask.md)
- [kUCKeyOutputGetIndexMask](./api-1390638-key_output_index_masks/kuckeyoutputgetindexmask.md)
  You can use this mask to test the bits (0–13) in a `UCKeyOutput` value that provide the actual index to another structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1390638-key_output_index_masks)*