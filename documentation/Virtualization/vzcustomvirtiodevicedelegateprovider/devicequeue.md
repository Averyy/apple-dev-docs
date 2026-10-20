# deviceQueue

**Framework**: Virtualization  
**Kind**: property  
**Role**: Instance Property

The queue the framework uses to synchronize operations for this device.

**Availability**:
- macOS 27.0+

## Declaration

```swift
var deviceQueue: dispatch_queue_t { get }
```

```objc
@property (readonly) dispatch_queue_t deviceQueue;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzcustomvirtiodevicedelegateprovider/devicequeue)*