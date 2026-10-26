# CMGetPS2ColorRenderingVMSize

**Framework**: Application Services  
**Kind**: func

Determines the virtual memory size of the color rendering dictionary (CRD) for a printer profile before your application or driver obtains the CRD and sends it to the printer.

## Declaration

```c
CMError CMGetPS2ColorRenderingVMSize (
   CMProfileRef srcProf,
   CMProfileRef dstProf,
   UInt32 *vmSize,
   Boolean *preferredCMMnotfound
);
```

#### Return Value

A `CMError` value. See [Result Codes](../colorsync_manager.md#1670295).

#### Overview

Your application or device driver can call this function to determine if the virtual memory size of the color rendering dictionary exceeds the printer’s capacity before sending the CRD to the printer. If the printer’s profile contains the Apple-defined optional tag `'psvm'` described in [`CMConcatProfileSet`](../cmconcatprofileset.md), then the default CMM will return the data supplied by this tag specifying the CRD virtual memory size for the rendering intent’s CRD. If the printer’s profile does not contain this tag, then the CMM uses an algorithm to assess the VM size of the CRD, in which case the assessment can be larger than the actual maximum VM size. 

The CMM uses the profile specified by the `srcProf` parameter to determine the rendering intent to use. 

## Parameters

- `srcProf`: A profile reference to a profile that supplies the rendering intent for the CRD. 
- `dstProf`: A profile reference to the destination printer profile.
- `vmSize`: A pointer to a memory size. On return, the virtual memory size of the CRD. 
- `preferredCMMnotfound`: A pointer to a flag for whether the preferred CMM was found. On return, has the value `true` if the CMM corresponding to profile was not available or if it was unable to perform the function and the default CMM was used. Otherwise, has the value `false`. 

## See Also

### Working With PostScript
- [CMGetPS2ColorSpace](./api-1805191-cmgetps2colorspace.md)
  Obtains color space element data in text format usable as the parameter to the PostScript `setColorSpace` operator, which characterizes the color space of subsequent graphics data. 
- [CMGetPS2ColorRenderingIntent](./api-1805196-cmgetps2colorrenderingintent.md)
  Obtains the rendering intent element data in text format usable as the parameter to the PostScript `findRenderingIntent` operator, which specifies the color-matching option for subsequent graphics data.
- [CMGetPS2ColorRendering](./api-1805202-cmgetps2colorrendering.md)
  Obtains the color rendering dictionary (CRD) element data usable as the parameter to the PostScript `setColorRendering` operator, which specifies the PostScript color rendering dictionary to use for the following graphics data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805206-cmgetps2colorrenderingvmsize)*