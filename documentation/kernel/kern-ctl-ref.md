# kern_ctl_ref

**Framework**: Kernel  
**Kind**: tdef

**Availability**:
- macOS 10.13+

## Declaration

```swift
typedef void *kern_ctl_ref;
```

#### Discussion

A control reference is used to track an attached kernel control. Registering a kernel control will create a kernel control reference. This reference is required for sending data or removing the kernel control. This reference will be passed to callbacks for that kernel control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/kern_ctl_ref)*