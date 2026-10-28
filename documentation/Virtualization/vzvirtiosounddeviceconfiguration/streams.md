# streams

**Framework**: Virtualization  
**Kind**: property  
**Role**: Instance Property

List of audio streams exposed by this device.

**Availability**:
- macOS 12.0+

## Declaration

```swift
var streams: [VZVirtioSoundDeviceStreamConfiguration] { get set }
```

```objc
@property (copy) NSArray<VZVirtioSoundDeviceStreamConfiguration *> * streams;
```

## Discussion

Empty by default.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtiosounddeviceconfiguration/streams)*