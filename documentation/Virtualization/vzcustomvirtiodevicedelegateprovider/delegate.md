# delegate

**Framework**: Virtualization  
**Kind**: property  
**Role**: Instance Property

The delegate object that implements the device.

**Availability**:
- macOS 27.0+

## Declaration

```swift
weak var delegate: (any VZCustomVirtioDeviceConfigurationDelegate)? { get }
```

```objc
@property (weak, readonly) id<VZCustomVirtioDeviceConfigurationDelegate> delegate;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzcustomvirtiodevicedelegateprovider/delegate)*