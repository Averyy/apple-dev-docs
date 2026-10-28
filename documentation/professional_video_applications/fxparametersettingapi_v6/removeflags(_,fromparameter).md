# removeFlags(_:fromParameter:)

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Remove parameter flags from the current flags for a parameter.

**Availability**:
- FxPlug 4.2.2+

## Declaration

```swift
func removeFlags(_ flags: FxParameterFlags, fromParameter parameterID: UInt32) -> Bool
```

```objc
- (BOOL) removeFlags:(FxParameterFlags) flags fromParameter:(UInt32) parameterID;
```

## Return Value

Returns `YES` if the method successfully removes the flags; otherwise, `NO`.

## Discussion

Use this method to remove one or more parameter flags without changing the value of other flags.

## Parameters

- `flags`: The flags to remove.
- `parameterID`: The ID of the parameter whose flags this method clears.

## See Also

### Instance Methods
- [func addFlags(FxParameterFlags, toParameter: UInt32) -> Bool](./addflags%28_,toparameter%29.md)
  Add new parameter flags to the current flags for a parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxparametersettingapi_v6/removeflags(_:fromparameter:))*