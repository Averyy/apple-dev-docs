# CMGetPS2ColorSpace

**Framework**: Application Services  
**Kind**: func

Obtains color space element data in text format usable as the parameter to the PostScript `setColorSpace` operator, which characterizes the color space of subsequent graphics data. 

## Declaration

```c
CMError CMGetPS2ColorSpace (
   CMProfileRef srcProf,
   UInt32 flags,
   CMFlattenUPP proc,
   void *refCon,
   Boolean *preferredCMMnotfound
);
```

#### Return Value

A `CMError` value. See [Result Codes](../colorsync_manager.md#1670295).

#### Overview

The `CMGetPS2ColorSpace` function obtains PostScript color space data from the source profile. The valid profile classes for the `CMGetPS2ColorSpace` function are display, input, and output profiles with at most four components.

To determine which profile elements to use to generate the PostScript color space data, the CMM:

-  uses the PostScript `cmPS2CSATag`, if it exists 
-  otherwise, uses the multidimensional table tag (`cmAToB0`, `cmAToB1`, or `cmAToB2`), if it exists, for the rendering intent currently specified by the profile 
-  otherwise, uses the multidimensional table tag `cmAToB0`, if it exists 
-  otherwise, for display profiles only, uses the tristimulus tags (`cmRedColorantTag`, `cmGreenColorantTag`, `cmBlueColorantTag`) and the tonal curve tags (`cmRedTRCTag`, `cmGreenTRCTag`, and `cmBlueTRCTag`) 

The CMM obtains the PostScript data from the profile and calls your low-level data transfer procedure passing the PostScript data to it. The CMM converts the data into a PostScript stream and calls your procedure as many times as necessary to transfer the data to it. 

Typically, the low-level data transfer function returns this data to the calling application or device driver to pass to a PostScript printer as an operand to the PostScript `setcolorspace` operator, which defines the color space of graphics data to follow. 

The `CMGetPS2ColorSpace` function is dispatched to the CMM component specified by the source profile. If the designated CMM is not available or the CMM does not implement this function, then the ColorSync Manager dispatches the function to the default CMM. 

## Parameters

- `srcProf`: A profile reference to the source profile that defines the data color space and identifies the preferred CMM. 
- `flags`: If the value of `flags` is equal to `cmPS8bit`, the generated PostScript will utilize 8-bit encoding whenever possible to achieve higher data compaction. If the value of `flags` is not equal to `cmPS8bit`, the generated data will be 7-bit safe, in either ASCII or ASCII base-85 encoding. 
- `proc`: A pointer to a callback flatten function to receive the PostScript data from the CMM. For information, see the function [`CMFlattenProcPtr`](../cmflattenprocptr.md). 
- `refCon`: An untyped pointer to arbitrary data supplied by your application. `CMGetPS2ColorSpace` passes this data in calls to your [`CMFlattenProcPtr`](../cmflattenprocptr.md) function. 
- `preferredCMMnotfound`: A pointer to a flag for whether the preferred CMM was found. On return, has the value `true` if the CMM corresponding to profile was not available or if it was unable to perform the function and the default CMM was used. Otherwise, has the value `false`. 

## See Also

### Working With PostScript
- [CMGetPS2ColorRenderingIntent](./api-1805196-cmgetps2colorrenderingintent.md)
  Obtains the rendering intent element data in text format usable as the parameter to the PostScript `findRenderingIntent` operator, which specifies the color-matching option for subsequent graphics data.
- [CMGetPS2ColorRendering](./api-1805202-cmgetps2colorrendering.md)
  Obtains the color rendering dictionary (CRD) element data usable as the parameter to the PostScript `setColorRendering` operator, which specifies the PostScript color rendering dictionary to use for the following graphics data.
- [CMGetPS2ColorRenderingVMSize](./api-1805206-cmgetps2colorrenderingvmsize.md)
  Determines the virtual memory size of the color rendering dictionary (CRD) for a printer profile before your application or driver obtains the CRD and sends it to the printer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805191-cmgetps2colorspace)*