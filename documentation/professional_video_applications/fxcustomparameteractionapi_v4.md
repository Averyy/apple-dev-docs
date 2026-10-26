# FxCustomParameterActionAPI_v4

**Framework**: Professional Video Applications  
**Kind**: protocol  
**Role**: Protocol

Defines the methods the host application provides to support a custom parameter view.

**Availability**:
- FxPlug 4.0+

## Declaration

```swift
protocol FxCustomParameterActionAPI_v4
```

```objc
@protocol FxCustomParameterActionAPI_v4
```

## Mentions

- [Adding parameters to plug-ins](../Professional-Video-Applications/adding-parameters-to-plug-ins.md)
- [Understanding time in FxPlug](../Professional-Video-Applications/understanding-time-in-fxplug.md)

#### Overview

Because custom parameter views can get user events at any time, this protocol provides methods to prepare the host application for parameter changes or other actions at arbitrary times.

Use the [`startAction(_:)`](./fxcustomparameteractionapi_v4/startaction%28_%29.md) and [`endAction(_:)`](./fxcustomparameteractionapi_v4/endaction%28_%29.md) commands only when the host application didn’t call your code. For example, in a custom view, the OS directly asks your view to redraw when it needs updating. At this point, the application has no point of reference for interacting with your plug-in, so you must tell it to start the communication by calling [`startAction(_:)`](./fxcustomparameteractionapi_v4/startaction%28_%29.md). In the past, if you called [`startAction(_:)`](./fxcustomparameteractionapi_v4/startaction%28_%29.md) when the host called your plug-in, there were no harmful side effects. Starting with FxPlug 4, calling [`startAction(_:)`](./fxcustomparameteractionapi_v4/startaction%28_%29.md) when the host calls your plug-in can cause hangs in the host application. Call [`startAction(_:)`](./fxcustomparameteractionapi_v4/startaction%28_%29.md) if you’re executing any code in a block that you created, such as calling [`dispatch_async`](../Dispatch/dispatch_async.md).

You mainly need to use [`startAction(_:)`](./fxcustomparameteractionapi_v4/startaction%28_%29.md) and [`endAction(_:)`](./fxcustomparameteractionapi_v4/endaction%28_%29.md) when handling custom [`NSView`](../AppKit/nsview.md) events for custom parameters or when running code in a dispatch block that your plug-in created.

It is NOT safe to set or get parameter values at arbitrary times outside of a [`startAction(_:)`](./fxcustomparameteractionapi_v4/startaction%28_%29.md) and [`endAction(_:)`](./fxcustomparameteractionapi_v4/endaction%28_%29.md) pair. For example, when a custom parameter view receives a `keyDown:positionY:keyPressed:modifiers:forceUpdate:didHandle:time:` event, it may want to change its parameter value. It then calls the following sequence:

**Swift**:

```swift
let actionAPI = _apiManager!.api(for: FxCustomParameterActionAPI_v4.self) as! FxCustomParameterActionAPI_v4
let time = actionAPI.currentTime

actionAPI.startAction(_:self)
let settingAPI = _apiManager!.api(for: FxParameterSettingAPI_v5.self) as! FxParameterSettingAPI_v5
settingAPI.setCustomParameterValue(myObject, toParameter: myParameterID, at: time)
actionAPI.endAction(_:self)
```

**Objective-C**:

```objc
id <FxCustomParameterActionAPI_v4> actionAPI = [apiManager apiForProtocol:FxCustomParameterActionAPI_v4];
CMTime time = [actionAPI currentTime];
 
[actionAPI startAction:self];
id <FxParameterSettingAPI_v5> settingAPI = [apiManager apiForProtocol:FxParameterSettingAPI_v5];
[settingAPI setCustomParameterValue:myObject toParameter:myParameterID atTime:time];
[actionAPI endAction:self];
```

## Topics

### Instance Methods
- [func currentTime() -> CMTime](./fxcustomparameteractionapi_v4/currenttime%28%29.md)
  Returns the current time, expressed as a rational time.
- [func startAction(Any!)](./fxcustomparameteractionapi_v4/startaction%28_%29.md)
  Prepares the host to access parameters.
- [func endAction(Any!)](./fxcustomparameteractionapi_v4/endaction%28_%29.md)
  Tells the host application that the plug-in is done accessing parameters.

## See Also

### Custom Parameter APIs
- [protocol FxCustomParameterViewHost_v2](./fxcustomparameterviewhost_v2.md)
  Defines the methods a plug-in needs to implement to associate a custom NSView with one of its parameters.
- [protocol FxCustomParameterInterpolation_v2](./fxcustomparameterinterpolation_v2.md)
  Defines the methods a plug-in needs to implement to support keyframing custom parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxcustomparameteractionapi_v4)*