# CMGetPS2ColorRendering

**Framework**: Application Services  
**Kind**: func

Obtains the color rendering dictionary (CRD) element data usable as the parameter to the PostScript `setColorRendering` operator, which specifies the PostScript color rendering dictionary to use for the following graphics data.

## Declaration

```c
CMError CMGetPS2ColorRendering (
   CMProfileRef srcProf,
   CMProfileRef dstProf,
   UInt32 flags,
   CMFlattenUPP proc,
   void *refCon,
   Boolean *preferredCMMnotfound
);
```

#### Return Value

A `CMError` value. See [Result Codes](../colorsync_manager.md#1670295).

#### Overview

The `CMGetPS2ColorRendering` function obtains CRD data from the profile specified by the `dstProf` parameter. To be valid, the parameter must specify an output profile with at most four components. The CMM uses the rendering intent from the profile specified by the `srcProf` parameter to determine which of the PostScript tags (`ps2CR0Tag`, `ps2CR1Tag`, `ps2CR2Tag`, or `ps2CR3Tag`) to use in creating the CRD. If none of these tags exists in the profile, the CMM creates the CRD from one of the multidimensional table tags (`cmAToB0`, `cmAToB1`, or `cmAToB2`), again chosen according to the rendering intent of the profile specified by the `srcProf` parameter.

This function is dispatched to the CMM component specified by the destination profile. If the designated CMM is not available or the CMM does not implement this function, the ColorSync Manager dispatches this function to the default CMM. 

The CMM obtains the PostScript data and passes it to your low-level data transfer procedure, specified by the `proc` parameter. The CMM converts the data into a PostScript stream and calls your procedure as many times as necessary to transfer the data to it. Typically, the low-level data transfer function returns this data to the calling application or device driver to pass to a PostScript printer.

Before your application or device driver sends the CRD to the printer, it can call the function [CMGetPS2ColorRenderingVMSize](./api-1805206-cmgetps2colorrenderingvmsize.md) to determine the virtual memory size of the CRD. 

## Parameters

- `srcProf`: A profile reference to a profile that supplies the rendering intent for the CRD. 
- `dstProf`: A profile reference to a profile from which to extract the CRD data.
- `flags`: If the value of `flags` is equal to `cmPS8bit`, the generated PostScript will utilize 8-bit encoding whenever possible to achieve higher data compaction. If the value of `flags` is not equal to `cmPS8bit`, the generated data will be 7-bit safe, in either ASCII or ASCII base-85 encoding. 
- `proc`: A pointer to a callback flatten function to perform the data transfer. For information, see the function [`CMFlattenProcPtr`](../cmflattenprocptr.md). 
- `refCon`: An untyped pointer to arbitrary data supplied by your application. `CMGetPS2ColorSpace` passes this data in calls to your [`CMFlattenProcPtr`](../cmflattenprocptr.md) function. 
- `preferredCMMnotfound`: A pointer to a flag for whether the preferred CMM was found. On return, has the value `true` if the CMM corresponding to profile was not available or if it was unable to perform the function and the default CMM was used. Otherwise, has the value `false`. 

## See Also

### Working With PostScript
- [CMGetPS2ColorSpace](./api-1805191-cmgetps2colorspace.md)
  Obtains color space element data in text format usable as the parameter to the PostScript `setColorSpace` operator, which characterizes the color space of subsequent graphics data. 
- [CMGetPS2ColorRenderingIntent](./api-1805196-cmgetps2colorrenderingintent.md)
  Obtains the rendering intent element data in text format usable as the parameter to the PostScript `findRenderingIntent` operator, which specifies the color-matching option for subsequent graphics data.
- [CMGetPS2ColorRenderingVMSize](./api-1805206-cmgetps2colorrenderingvmsize.md)
  Determines the virtual memory size of the color rendering dictionary (CRD) for a printer profile before your application or driver obtains the CRD and sends it to the printer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805202-cmgetps2colorrendering)*