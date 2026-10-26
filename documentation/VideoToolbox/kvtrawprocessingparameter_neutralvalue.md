# kVTRAWProcessingParameter_NeutralValue

**Framework**: Video Toolbox  
**Kind**: var  
**Role**: Global Variable

The value corresponding to this key is a neutral setting for the processor.

**Availability**:
- macOS 15.0+

## Declaration

```c
extern CFStringRef const kVTRAWProcessingParameter_NeutralValue;
```

#### Discussion

For List types, this is the ListElementID for the List element.

## See Also

### Parameters
- [kVTRAWProcessingParameter_Key](./kvtrawprocessingparameter_key.md)
  The value corresponding to this key must match the identifier for one of the permitted processing parameters.
- [kVTRAWProcessingParameterListElement_Description](./kvtrawprocessingparameterlistelement_description.md)
  The value corresponding to this key is a human-readable description for the element, suitable for displaying in a tooltip or other descriptive UI.
- [kVTRAWProcessingParameterListElement_Label](./kvtrawprocessingparameterlistelement_label.md)
  The value corresponding to this key is a human-readable label for the element, suitable for displaying in a list of options.
- [kVTRAWProcessingParameterListElement_ListElementID](./kvtrawprocessingparameterlistelement_listelementid.md)
  The value corresponding to this key is a number indicating the index of a list element parameter in a list in the processing parameters dictionary.
- [kVTRAWProcessingParameterValueType_Boolean](./kvtrawprocessingparametervaluetype_boolean.md)
  The value corresponding to this key is a string that indicates a Boolean parameter type.
- [kVTRAWProcessingParameterValueType_Float](./kvtrawprocessingparametervaluetype_float.md)
  The value corresponding to this key is a string that indicates a floating-point parameter type.
- [kVTRAWProcessingParameterValueType_Integer](./kvtrawprocessingparametervaluetype_integer.md)
  The value corresponding to this key is a string that indicates an integer parameter type.
- [kVTRAWProcessingParameterValueType_List](./kvtrawprocessingparametervaluetype_list.md)
  The value corresponding to this key is a string that indicates a list parameter type.
- [kVTRAWProcessingParameterValueType_SubGroup](./kvtrawprocessingparametervaluetype_subgroup.md)
  The value corresponding to this key is a string that indicates a subgroup parameter type.
- [kVTRAWProcessingParameter_CameraValue](./kvtrawprocessingparameter_cameravalue.md)
  The value corresponding to this key is the “As Shot” value for this parameter as originally captured by the camera.
- [kVTRAWProcessingParameter_CurrentValue](./kvtrawprocessingparameter_currentvalue.md)
  The value corresponding to this key is the currently configured value for this parameter.
- [kVTRAWProcessingParameter_Description](./kvtrawprocessingparameter_description.md)
  The value corresponding to this key is a localized string with a description of the parameter suitable for display in a tooltip or other descriptive UI.
- [kVTRAWProcessingParameter_Enabled](./kvtrawprocessingparameter_enabled.md)
  The value corresponding to this key is Boolean indicating whether the parameter is enabled and can be modified.
- [kVTRAWProcessingParameter_InitialValue](./kvtrawprocessingparameter_initialvalue.md)
  The value corresponding to this key is the initial value for this parameter as defined by the container and metadata provided at creation time.
- [kVTRAWProcessingParameter_ListArray](./kvtrawprocessingparameter_listarray.md)
  The value corresponding to this key is an array of dictionaries describing each element in the list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/kvtrawprocessingparameter_neutralvalue)*