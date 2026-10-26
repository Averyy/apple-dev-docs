# CMPS2CRDVMSizeType

**Framework**: Application Services  
**Kind**: struct  
**Role**: Structure

Defines the Apple-defined `'psvm'` optional tag.

**Availability**:
- macOS 10.0+ - Deprecated in 10.6

## Declaration

```c
typedef struct CMPS2CRDVMSizeType {
    ...
} CMPS2CRDVMSizeType;
```

## Topics

### Instance Properties
- [count](./cmps2crdvmsizetype/api-1560398-count.md)
  The number of entries in the `intentCRD` array. You should specify at least four entries: 0, 1, 2, and 3.
- [intentCRD](./cmps2crdvmsizetype/api-1560725-intentcrd.md)
  A variable-sized array of four or more members defined by the `CMIntentCRDSize` data type. 
- [reserved](./cmps2crdvmsizetype/api-1560735-reserved.md)
  Reserved for future use.
- [typeDescriptor](./cmps2crdvmsizetype/api-1560713-typedescriptor.md)
  The `'psvm'` tag signature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/cmps2crdvmsizetype)*