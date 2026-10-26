# startAction(_:)

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Prepares the host to access parameters.

**Availability**:
- FxPlug 4.0+

## Declaration

```swift
func startAction(_ sender: Any!)
```

```objc
- (void) startAction:(id) sender;
```

## Mentions

- [Adding parameters to plug-ins](https://developer.apple.com/documentation/professional-video-applications/adding-parameters-to-plug-ins)

#### Discussion

OSC plug-ins (implementing [`FxOnScreenControl_v4`](../fxonscreencontrol_v4.md)) should not use [`startAction(_:)`](./startaction%28_%29.md) and [`endAction(_:)`](./endaction%28_%29.md), as the host is already aware that parameters are likely to change.

Starting with FxPlug 4, the [`startAction(_:)`](./startaction%28_%29.md) function is more heavyweight than in the past. Calling [`startAction(_:)`](./startaction%28_%29.md) will cause the host application to gather up the value of all parameters in the plug-in and send them to the XPC service. Any calls to the [`FxUndoAPI`](../fxundoapi.md), [`FxParameterSettingAPI_v6`](../fxparametersettingapi_v6.md), [`FxParameterRetrievalAPI_v7`](../fxparameterretrievalapi_v7.md), or [`FxKeyframeAPI_v3`](../fxkeyframeapi_v3.md) will be queued up and sent to the host in bulk once you call [`endAction(_:)`](./endaction%28_%29.md). Therefore you should avoid making calls like this:

**Swift**:

```swift
let customParameterActionAPI = _apiManager.api(for: FxCustomParameterActionAPI_v4.self) as? FxCustomParameterActionAPI_v4
customParameterActionAPI.startAction(_:self)
let undoAPI = _apiManager.api(for: FxUndoAPI.self) as? FxUndoAPI
undoAPI.startUndoGroup(_, name: "Change Parameter");
customParamActionAPI.endAction()
       
// … later in the same function…
customParameterActionAPI.startAction(_:self)
let paramSetAPI = _apiManager.api(for: FxParameterSettingAPI_v6.self) as? FxParameterSettingAPI_v6
paramSetAPI.setFloatValue(1.0, toParameter: 5, at: customParameterActionAPI.currentTime)
customParamActionAPI.endAction()
       
// … later in the same function…
customParameterActionAPI.startAction(_:self)
let undoAPI = _apiManager.api(for: FxUndoAPI.self) as? FxUndoAPI
undoAPI.endUndoGroup();
customParamActionAPI.endAction(_:self)
```

**Objective-C**:

```objc
id<FxCustomParameterActionAPI_v4> customParameterActionAPI = [_apiManager apiForProtocol:@protocol(FxCustomParameterActionAPI_v4)];
[customParameterActionAPI startAction:self];
id<FxUndoAPI> undoAPI = [_apiManager apiForProtocol:@protocol(FxUndoAPI)];
[undoAPI startUndoGroup:@”Change Parameter”];
[customParameterActionAPI endAction:self];

// … later in the same function…
[customParameterActionAPI startAction:self];
id<FxParameterSettingAPI_v6> paramSetAPI = [_apiManager apiForProtocol:@protocol(FxParameterSettingAPI_v6)];
[paramSetAPI setFloatValue:1.0 toParameterID:5 atTime:[customParameterActionAPI currentTime]];
[customParameterActionAPI endAction:self];

// … later in the same function…
[customParameterActionAPI startAction:self];
id<FxUndoAPI> undoAPI = [_apiManager apiForProtocol:@protocol(FxUndoAPI)];
[undoAPI endUndoGroup:];
[customParameterActionAPI endAction:self];

```

This code will not work properly. The calls to [`startAction(_:)`](./startaction%28_%29.md) and [`endAction(_:)`](./endaction%28_%29.md) in the first block will cause the host app to start an undo group without closing it in the same run loop. The calls to set the parameter will not be enclosed in an undo group and will be executed in a different run loop occurrence than the call to [`startUndoGroup(_:)`](../fxundoapi/startundogroup%28_%29.md) in the host application. The call to end the undo group will occur in a third run loop in the host app and will be unbalanced.

Instead you should call [`startAction(_:)`](./startaction%28_%29.md) before all actions you want to perform, and call [`endAction(_:)`](./endaction%28_%29.md) after all actions have been completed, like this:

**Swift**:

```swift
let customParameterActionAPI = _apiManager.api(for: FxCustomParameterActionAPI_v4.self) as? FxCustomParameterActionAPI_v4
customParameterActionAPI.startAction(_:self)
let undoAPI = _apiManager.api(for: FxUndoAPI.self) as? FxUndoAPI
undoAPI.startUndoGroup(_, name: "Change Parameter");

// … later in the same function…
let paramSetAPI = _apiManager.api(for: FxParameterSettingAPI_v6.self) as? FxParameterSettingAPI_v6
paramSetAPI.setFloatValue(1.0, toParameter: 5, at: customParameterActionAPI.currentTime)

// … later in the same function…
undoAPI.endUndoGroup();
customParamActionAPI.endAction(_:self)
```

**Objective-C**:

```objc
id<FxCustomParameterActionAPI_v4> customParameterActionAPI = [_apiManager apiForProtocol:@protocol(FxCustomParameterActionAPI_v4)];
[customParameterActionAPI startAction:self];
id<FxUndoAPI> undoAPI = [_apiManager apiForProtocol:@protocol(FxUndoAPI)];
[undoAPI startUndoGroup:@”Change Parameter”];

// … later in the same function…
id<FxParameterSettingAPI_v6> paramSetAPI = [_apiManager apiForProtocol:@protocol(FxParameterSettingAPI_v6)];
[paramSetAPI setFloatValue:1 toParameterID:5 atTime:[customParameterActionAPI currentTime]];

// … later in the same function…
[undoAPI endUndoGroup:];
[customParameterActionAPI endAction:self];

```

This will work as intended and start a single undo group that contains the parameter change.

## Parameters

- `sender`: The view class that implements this protocol. Typically passed as self.

## See Also

### Instance Methods
- [func currentTime() -> CMTime](./currenttime%28%29.md)
  Returns the current time, expressed as a rational time.
- [func endAction(Any!)](./endaction%28_%29.md)
  Tells the host application that the plug-in is done accessing parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxcustomparameteractionapi_v4/startaction(_:))*