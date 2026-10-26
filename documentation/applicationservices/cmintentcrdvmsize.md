# CMIntentCRDVMSize

**Framework**: Application Services  
**Kind**: struct  
**Role**: Structure

Defines the rendering intent and its maximum VM size. 

**Availability**:
- macOS 10.0+ - Deprecated in 10.6

## Declaration

```c
typedef struct CMIntentCRDVMSize {
    ...
} CMIntentCRDVMSize;
```

#### Overview

To specify the maximum virtual memory (VM) size of the color rendering dictionary (CRD) for a specific rendering intent for a particular PostScript(TM) Level 2 printer type, a printer profile can include the optional Apple-defined `'psvm'` tag. The PostScript CRD virtual memory size tag structure’s element data includes an array containing one entry for each rendering intent and its virtual memory size.

If a PostScript printer profile includes this tag, the default CMM uses the tag and returns the values specified by the tag when your application or device driver calls the function [CMGetPS2ColorRenderingVMSize](./colorsync_manager/api-1805206-cmgetps2colorrenderingvmsize.md).

If a PostScript printer profile does not include this tag, the CMM uses an algorithm to determine the VM size of the CRD. This may result in a size that is greater than the actual VM size.

The `CMPS2CRDVMSizeType` data type for the tag includes an array containing one or more members of type `CMIntentCRDVMSize. `

## Topics

### Instance Properties
- [VMSize](./cmintentcrdvmsize/api-1560469-vmsize.md)
  The virtual memory size of the CRD for the rendering intent specified for the `renderingIntent` field.
- [renderingIntent](./cmintentcrdvmsize/api-1560554-renderingintent.md)
  The rendering intent whose CRD virtual memory size you want to obtain. The rendering intent values are described in [Rendering Intent Values for Version 2.x Profiles](./api-1560278-x_profiles.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/cmintentcrdvmsize)*