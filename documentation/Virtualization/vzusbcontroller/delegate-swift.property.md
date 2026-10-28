# delegate

**Framework**: Virtualization  
**Kind**: property  
**Role**: Instance Property

**Availability**:
- macOS 27.0+

## Declaration

```swift
weak var delegate: (any VZUSBController.Delegate)? { get set }
```

```objc
@property (weak, nullable) id<VZUSBControllerDelegate> delegate;
```

## Discussion

The controller’s delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzusbcontroller/delegate-swift.property)*