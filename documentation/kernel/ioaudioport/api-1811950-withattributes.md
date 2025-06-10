# withAttributes

**Framework**: Kernel  
**Kind**: instm

Allocates a new IOAudioPort instance with the given attributes

## Declaration

```swift
static IOAudioPort *withAttributes(
 UInt32 portType,
 const char *portName = 0,
 UInt32 subType = 0,
 OSDictionary *properties = 0);
```

#### Return_value

Returns the newly allocated and initialized IOAudioPort instance.

#### Overview

This static method allocates a new IOAudioPort and calls initWithAttributes() on it with the parameters passed in to it.

## Parameters

- `portType`: A readable string representing the type of port. Common port types are defined in IOAudioTypes.h and are prefixed with 'kIOAudioPortType'. Please provide feedback if there are other common port types that should be included.
- `portName`: A readable string representing the name of the port. For example: 'Internal Speaker', 'Line Out'. This field is optional, but useful for providing information to the application/user.
- `subType`: Developer defined readable string representing a subtype for the port. (optional)
- `properties`: Standard property list passed to the init of any new IOService. This dictionary gets stored in the registry for this instance. (optional)

## See Also

- [addAudioControl](ioaudioport/1811855-addaudiocontrol.md)
  Adds a newly created IOAudioControl instance to the port.
- [deactivateAudioControls](ioaudioport/1811875-deactivateaudiocontrols.md)
  Called to shut down all of the audio controls for this port.
- [free](ioaudioport/1811888-free.md)
  Frees all of the resources allocated by the IOAudioPort.
- [initWithAttributes](ioaudioport/1811904-initwithattributes.md)
  Initializes a newly allocated IOAudioPort instance with the given attributes
- [start](ioaudioport/1811924-start.md)
  Called to start a newly created IOAudioPort.
- [stop](ioaudioport/1811938-stop.md)
  Called when the IOAudioDevice is stopping when it is no longer available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioaudioport/1811950-withattributes)*