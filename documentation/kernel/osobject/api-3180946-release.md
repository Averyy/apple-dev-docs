# release

**Framework**: Kernel  
**Kind**: instm  
**Role**: Instance Method

Releases the OSObject instance

**Availability**:
- DriverKit 19.0+
- macOS 10.15+

## Declaration

```cpp
virtual void release(void);
```

## Discussion

Decreases the retain count of the instance by one. If the count is then zero, frees the object.

## See Also

### Managing the Object Lifecycle
- [- init](./api-3180945-init.md)
- [- retain](./api-3180947-retain.md)
  Retains the OSObject instance
- [- free](./api-3180944-free.md)
- [OSObjectPtr](../../DriverKit/osobjectptr.md)
- [OSObjectRef](../../DriverKit/osobjectref.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osobject/3180946-release)*