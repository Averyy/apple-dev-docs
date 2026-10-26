# lightInfo(_:forLight:at:)

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Provides information about a light at a particular time.

**Availability**:
- FxPlug 4.0+

## Declaration

```swift
func lightInfo(_ light: UnsafeMutablePointer<FxLight>!, forLight lightIndex: Int, at time: CMTime) throws
```

```objc
- (BOOL) lightInfo:(FxLight *) light forLight:(NSUInteger) lightIndex atTime:(CMTime) time error:(NSError * *) error;
```

## Parameters

- `light`: A pointer to an FxLight structure to receive information about a particular light in the scene.
- `lightIndex`: The index of the light whose information you wish to retrieve.
- `time`: The time for which you want lighting information.

## See Also

### Getting Lighting Information
- [func numberOfLights(at: CMTime) -> Int](./numberoflights%28at%29.md)
  Retrieves the number of lights at the passed-in time.
- [struct FxLight](../fxlight.md)
  A structure that contains lighting information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxlightingapi_v3/lightinfo(_:forlight:at:))*