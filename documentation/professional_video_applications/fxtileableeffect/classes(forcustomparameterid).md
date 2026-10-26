# classes(forCustomParameterID:)

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method

Returns the classes of the objects contained in the custom parameter with the given ID.

**Availability**:
- FxPlug 4.2.1+

## Declaration

```swift
optional func classes(forCustomParameterID parameterID: UInt32) -> Set<AnyHashable>
```

```objc
- (NSSet<Class> *) classesForCustomParameterID:(UInt32) parameterID;
```

#### Return Value

An NSSet of classes of the specified parameter ID.

#### Discussion

When you make custom parameters, the host needs to know the classes of the parameters to store and unarchive them from disk. This method returns the Objective-C set of classes that the parameters are members of.

## Parameters

- `parameterID`: The parameter ID of the classes to be determined.

## See Also

### Adding and setting parameters
- [func addParameters() throws](./addparameters%28%29.md)
  Tells the host application what parameters your plug-in requires.
- [func `class`(forCustomParameterID: UInt32) -> AnyClass](./class%28forcustomparameterid%29.md)
  Returns the class of the object contained in the custom parameter with the given ID.
- [func parameterChanged(UInt32, at: CMTime) throws](./parameterchanged%28_,at%29.md)
  Executes when the host detects that a parameter has changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxtileableeffect/classes(forcustomparameterid:))*