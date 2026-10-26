# backingScaleFactor()

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns the scale factor for drawing the on-screen control to the current screen.

**Availability**:
- FxPlug 3.1+

## Declaration

```swift
func backingScaleFactor() -> Double
```

```objc
- (double) backingScaleFactor;
```

#### Return Value

The scale factor.

#### Discussion

Vertex coordinates already scale properly, but this method can be used for other types of drawings. For example, if you are preparing a texture on the CPU and uploading it, this can tell you how large to make the texture before uploading it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxonscreencontrolapi_v3/backingscalefactor())*