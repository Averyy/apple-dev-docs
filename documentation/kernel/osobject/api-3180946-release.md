# release

**Framework**: Kernel  
**Kind**: instm

Releases the OSObject instance

**Availability**:
- DriverKit 19.0+
- macOS 10.15+

## Declaration

```swift
virtual void release(void);
```

#### Discussion

Decreases the retain count of the instance by one. If the count is then zero, frees the object.

## See Also

- [- init](osobject/3180945-init.md)
- [- retain](osobject/3180947-retain.md)
  Retains the OSObject instance
- [- free](osobject/3180944-free.md)
- [OSObjectPtr](../driverkit/osobjectptr.md)
- [OSObjectRef](../driverkit/osobjectref.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osobject/3180946-release)*