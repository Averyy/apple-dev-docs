# addAudioControl

**Framework**: Kernel  
**Kind**: instm

Adds a newly created IOAudioControl instance to the port.

## Declaration

```swift
virtual IOReturn addAudioControl(
 IOAudioControl *control);
```

#### Return_value

Returns true on successfully staring the IOAudioControl.

#### Overview

This method is responsible for starting the new IOAudioControl and adding it to the internal audioControls array.

## Parameters

- `control`: A newly created IOAudioControl instance that should belong to this port.

## See Also

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
- [withAttributes](ioaudioport/1811950-withattributes.md)
  Allocates a new IOAudioPort instance with the given attributes


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioaudioport/1811855-addaudiocontrol)*