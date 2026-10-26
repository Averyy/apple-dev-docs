# numberOfLights(at:)

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Retrieves the number of lights at the passed-in time.

**Availability**:
- FxPlug 4.0+

## Declaration

```swift
func numberOfLights(at time: CMTime) -> Int
```

```objc
- (NSUInteger) numberOfLightsAtTime:(CMTime) time;
```

## Parameters

- `time`: The time at which you wish to obtain the number of lights.

## See Also

### Getting Lighting Information
- [func lightInfo(UnsafeMutablePointer<FxLight>!, forLight: Int, at: CMTime) throws](./lightinfo%28_,forlight,at%29.md)
  Provides information about a light at a particular time.
- [struct FxLight](../fxlight.md)
  A structure that contains lighting information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxlightingapi_v3/numberoflights(at:))*