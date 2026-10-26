# BigEndianOSType

**Framework**: Core Services  
**Kind**: tag

Protects a big-endian OSType value from being changedby little-endian code.

## Declaration

```c
// Little-endian host
struct BigEndianOSType {
   OSType    bigEndianValue;
};
typedef struct BigEndianOStype  BigEndianOStype;
   // Big-endian host
   typedef OSType BigEndianOSType;
```

## Topics

### Fields
- [bigEndianValue](./bigendianostype/api-1805539-bigendianvalue.md)
  An OSType value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/carbon_core/core_endian/bigendianostype)*