# SBP2ClientOrbData

**Framework**: Kernel  
**Kind**: tdef

## Declaration

```swift
typedef struct {
      IOFireWireSBP2ORB *orb;
      SCSITaskIdentifier scsiTask;
      SCSIServiceResponse serviceResponse;
      SCSITaskStatus taskStatus;
      IOBufferMemoryDescriptor *quadletAlignedBuffer;
} SBP2ClientOrbData;
```

#### Overview

This structure is stuffed into the refcon so we can associate which IOFireWireSBP2ORB and SCSITaskIdentifier is completing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofirewireserialbusprotocoltransport/sbp2clientorbdata)*