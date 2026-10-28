# addFlags(_:toParameter:)

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Add new parameter flags to the current flags for a parameter.

**Availability**:
- FxPlug 4.2.2+

## Declaration

```swift
func addFlags(_ flags: FxParameterFlags, toParameter parameterID: UInt32) -> Bool
```

```objc
- (BOOL) addFlags:(FxParameterFlags) flags toParameter:(UInt32) parameterID;
```

## Return Value

Returns `YES` if the method successfully adds the flags; otherwise, `NO`.

## Discussion

Use this method to set one or more parameter flags without changing the value of other flags.

## Parameters

- `flags`: The flags to add.
- `parameterID`: The ID of the parameter whose flags this method appends.

## See Also

### Instance Methods
- [func removeFlags(FxParameterFlags, fromParameter: UInt32) -> Bool](./removeflags%28_,fromparameter%29.md)
  Remove parameter flags from the current flags for a parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxparametersettingapi_v6/addflags(_:toparameter:))*