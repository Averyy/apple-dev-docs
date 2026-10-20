# QuickTime VR sample description ('qtvr')

**Framework**: QuickTime File Format  
**Kind**: class

Describe QuickTime VR samples.

#### Overview

Whereas the QuickTime VR media sample is simply the node information itself, all sample descriptions are required by QuickTime to have a certain structure for the first several bytes. The structure for the QuickTime VR sample description is as follows:

```c
typedef struct QTVRSampleDescription {
    UInt32                              size;
    UInt32                              type;
    UInt32                              reserved1;
    UInt16                              reserved2;
    UInt16                              dataRefIndex;
    UInt32                              data;
} QTVRSampleDescription, *QTVRSampleDescriptionPtr, **QTVRSampleDescriptionHandle;
```

## Topics

### Data fields
- [size](quicktime_vr_sample_description/size.md)
  The size, in bytes, of the sample description header structure.
- [type](quicktime_vr_sample_description/type.md)
  The sample description type.
- [reserved1](quicktime_vr_sample_description/reserved1.md)
  Reserved.
- [reserved2](quicktime_vr_sample_description/reserved2.md)
  Reserved.
- [dataRefIndex](quicktime_vr_sample_description/datarefindex.md)
  Reserved.
- [data](quicktime_vr_sample_description/data.md)
  The VR world atom container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/quicktime_vr_sample_description)*