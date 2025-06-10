# deactivateAudioControls

**Framework**: Kernel  
**Kind**: instm

Called to shut down all of the audio controls for this port.

## Declaration

```swift
virtual void deactivateAudioControls();
```

#### Overview

This will stop all of the audio controls and release them so that the instances may be freed. This is called from the free() method.

## See Also

- [addAudioControl](ioaudioport/1811855-addaudiocontrol.md)
  Adds a newly created IOAudioControl instance to the port.
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

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioaudioport/1811875-deactivateaudiocontrols)*