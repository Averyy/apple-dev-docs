# CMAccelerationTableData

**Framework**: Application Services  
**Kind**: tdef

## Declaration

```c
struct CMAccelerationTableData {
   SInt32 inputLutEntryCount;
   SInt32 inputLutWordSize;
   Handle inputLut;
   SInt32 outputLutEntryCount;
   SInt32 outputLutWordSize;
   Handle outputLut;
   SInt32 colorLutInDim;
   SInt32 colorLutOutDim;
   SInt32 colorLutGridPoints;
   SInt32 colorLutWordSize;
   Handle colorLut;
   CMBitmapColorSpace inputColorSpace;
   CMBitmapColorSpace outputColorSpace;
   void *userData;
   UInt32 reserved1;
   UInt32 reserved2;
   UInt32 reserved3;
   UInt32 reserved4;
   UInt32 reserved5;
};
typedef struct CMAccelerationTableData CMAccelerationTableData;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/cmaccelerationtabledata)*