# CMConvertRGBToHLS

**Framework**: Application Services  
**Kind**: func

Converts colors specified in the RGB color space to equivalent colors defined in the HLS color space. 

## Declaration

```c
CMError CMConvertRGBToHLS (
   const CMColor *src,
   CMColor *dst,
   size_t count
);
```

#### Return Value

A `CMError` value. See [Result Codes](../colorsync_manager.md#1670295).

#### Overview

The `CMConvertRGBToHLS` function converts one or more colors defined in the RGB color space to equivalent colors defined in the HLS color space. Both color spaces are device dependent.

If your application does not require that you preserve the source color list, you can pass the pointer to the same color list array as the `src` and `dst` parameters and allow the `CMConvertRGBToHLS` function to overwrite the source colors with the resulting converted color specifications. 

## Parameters

- `src`: A pointer to an array containing the list of RGB colors to convert to HLS colors. 
- `dst`: A pointer to an array containing the list of colors, resulting from the conversion, as specified in the HLS color space.
- `count`: The number of colors to convert. 

## See Also

### Converting Colors
- [CMConvertXYZToLab](./api-1805133-cmconvertxyztolab.md)
  Converts colors specified in the XYZ color space to the L*a*b* color space. 
- [CMConvertLabToXYZ](./api-1805134-cmconvertlabtoxyz.md)
  Converts colors specified in the L*a*b* color space to the XYZ color space. 
- [CMConvertXYZToLuv](./api-1805137-cmconvertxyztoluv.md)
  Converts colors specified in the XYZ color space to the L*u*v* color space. 
- [CMConvertLuvToXYZ](./api-1805140-cmconvertluvtoxyz.md)
  Converts colors specified in the L*u*v* color space to the XYZ color space. 
- [CMConvertXYZToYxy](./api-1805142-cmconvertxyztoyxy.md)
  Converts colors specified in the XYZ color space to the Yxy color space. 
- [CMConvertYxyToXYZ](./api-1805146-cmconvertyxytoxyz.md)
  Converts colors specified in the Yxy color space to the XYZ color space. 
- [CMConvertHLSToRGB](./api-1805152-cmconverthlstorgb.md)
  Converts colors specified in the HLS color space to equivalent colors defined in the RGB color space. 
- [CMConvertRGBToHSV](./api-1805155-cmconvertrgbtohsv.md)
  Converts colors specified in the RGB color space to equivalent colors defined in the HSV color space when the device types are the same. 
- [CMConvertHSVToRGB](./api-1805160-cmconverthsvtorgb.md)
  Converts colors specified in the HSV color space to equivalent colors defined in the RGB color space. 
- [CMConvertRGBToGray](./api-1805164-cmconvertrgbtogray.md)
  Converts colors specified in the RGB color space to equivalent colors defined in the Gray color space. 
- [CMConvertXYZToFixedXYZ](./api-1805169-cmconvertxyztofixedxyz.md)
  Converts colors specified in the XYZ color space whose components are expressed as XYZ 16-bit unsigned values of type `CMXYZColor` to equivalent colors expressed as 32-bit signed values of type `CMFixedXYZColor`.
- [CMConvertFixedXYZToXYZ](./api-1805174-cmconvertfixedxyztoxyz.md)
  Converts colors specified in XYZ color space whose components are expressed as Fixed XYZ 32-bit signed values of type `CMFixedXYZColor` to equivalent colors expressed as XYZ 16-bit unsigned values of type `CMXYZColor`.
- [CMConvertXYZToXYZ](./api-1805177-cmconvertxyztoxyz.md)
  Converts a source color to a destination color using the specified chromatic adaptation method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805149-cmconvertrgbtohls)*