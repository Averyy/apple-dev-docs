# createView(forParameterID:)

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Provides an NSView to be associated with the given parameter.

**Availability**:
- FxPlug 4.0+

## Declaration

```swift
func createView(forParameterID parameterID: UInt32) -> NSView!
```

```objc
- (NSView *) createViewForParameterID:(UInt32) parameterID;
```

## Mentions

- [Adding parameters to plug-ins](../../Professional-Video-Applications/adding-parameters-to-plug-ins.md)

## Return Value

An NSView or subclass of NSView.

## Discussion

The host application calls this plug-in method during the parameter-list setup sequence, once for each plug-in parameter that has the `kFxParameterFlag_CUSTOM_UI` parameter flag set. The view may be created dynamically, or, more commonly, retrieved from a NIB file in the plug-in’s resources directory.

The object returned by this method should not be autoreleased. It should be allocated by the method, and will be released by the caller. The implementation may look something like this:

```objc
if ( parmId == kMyViewParmID )
return [[MyView alloc] init];
```

## Parameters

- `parameterID`: The ID of the parameter to be associated with the custom UI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxcustomparameterviewhost_v2/createview(forparameterid:))*