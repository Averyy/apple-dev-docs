# Tag Constants

**Framework**: Application Services  
**Kind**: tdef

Constants that specify values, such as minimum and maximum values, that your application can pass to or obtain from printing functions.

## Declaration

```c
typedef UInt32 PMTag;
enum {
   kPMCurrentValue = 'curr',
   kPMDefaultValue = 'dflt',
   kPMMinimumValue = 'minv',
   kPMMaximumValue = 'maxv',
   kPMSourceProfile = 'srcp',
   kPMMinRange = 'mnrg',
   kPMMaxRange = 'mxrg',
   kPMMinSquareResolution = 'mins',
   kPMMaxSquareResolution = 'maxs',
   kPMDefaultResolution = 'dftr'
};
```

## Topics

### Constants
- [kPMCurrentValue](./tag_constants/kpmcurrentvalue.md)
  Specifies the current setting or value.
- [kPMDefaultValue](./tag_constants/kpmdefaultvalue.md)
  Specifies the default setting or value.
- [kPMMinimumValue](./tag_constants/kpmminimumvalue.md)
  Specifies the minimum setting or value.
- [kPMMaximumValue](./tag_constants/kpmmaximumvalue.md)
  Specifies the maximum setting or value.
- [kPMSourceProfile](./tag_constants/kpmsourceprofile.md)
  Specifies a ColorSync source profile.
- [kPMMinRange](./tag_constants/kpmminrange.md)
  Specifies the minimum resolution supported by the printer.
- [kPMMaxRange](./tag_constants/kpmmaxrange.md)
  Specifies the maximum resolution supported by the printer.
- [kPMMinSquareResolution](./tag_constants/kpmminsquareresolution.md)
  Specifies the minimum resolution setting for which the horizontal and vertical resolutions are equal.
- [kPMMaxSquareResolution](./tag_constants/kpmmaxsquareresolution.md)
  Specifies the maximum resolution setting for which the horizontal and vertical resolutions are equal.
- [kPMDefaultResolution](./tag_constants/kpmdefaultresolution.md)
  Specifies the default resolution setting for the printer (typically 72 dots per inch).


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/core_printing/tag_constants)*