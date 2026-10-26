# endAction(_:)

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Tells the host application that the plug-in is done accessing parameters.

**Availability**:
- FxPlug 4.0+

## Declaration

```swift
func endAction(_ sender: Any!)
```

```objc
- (void) endAction:(id) sender;
```

## Mentions

- [Adding parameters to plug-ins](../../Professional-Video-Applications/adding-parameters-to-plug-ins.md)

#### Discussion

It is important to note that OSC plug-ins (implementing [`FxOnScreenControl_v4`](../fxonscreencontrol_v4.md)) should not use [`startAction(_:)`](./startaction%28_%29.md) and [`endAction(_:)`](./endaction%28_%29.md), as the host is already aware that parameters are likely to change.

## Parameters

- `sender`: The view class that implements this protocol. Typically passed as self.

## See Also

### Instance Methods
- [func currentTime() -> CMTime](./currenttime%28%29.md)
  Returns the current time, expressed as a rational time.
- [func startAction(Any!)](./startaction%28_%29.md)
  Prepares the host to access parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxcustomparameteractionapi_v4/endaction(_:))*