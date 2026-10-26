# class(forCustomParameterID:)

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method

Returns the class of the object contained in the custom parameter with the given ID.

**Availability**:
- FxPlug 4.0+

## Declaration

```swift
optional func `class`(forCustomParameterID parameterID: UInt32) -> AnyClass
```

```objc
- (Class) classForCustomParameterID:(UInt32) parameterID;
```

## Mentions

- [Analyzing media](https://developer.apple.com/documentation/professional-video-applications/analyzing-media)

#### Return Value

An Objective-C class of the specified parameterID.

#### Discussion

When you make custom parameters and the host stores them for you, it needs to know the class of the parameters to unarchive them from disk. This method returns the Objective-C class of which they are members.

## Parameters

- `parameterID`: The parameter ID of the class to be determined.

## See Also

### Adding and setting parameters
- [func addParameters() throws](./addparameters%28%29.md)
  Tells the host application what parameters your plug-in requires.
- [func classes(forCustomParameterID: UInt32) -> Set<AnyHashable>](./classes%28forcustomparameterid%29.md)
  Returns the classes of the objects contained in the custom parameter with the given ID.
- [func parameterChanged(UInt32, at: CMTime) throws](./parameterchanged%28_,at%29.md)
  Executes when the host detects that a parameter has changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxtileableeffect/class(forcustomparameterid:))*