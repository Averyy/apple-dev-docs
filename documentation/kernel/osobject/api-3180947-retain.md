# retain

**Framework**: Kernel  
**Kind**: instm  
**Role**: Instance Method

Retains the OSObject instance

**Availability**:
- DriverKit 19.0+
- macOS 10.15+

## Declaration

```cpp
virtual void retain(void);
```

## Discussion

Increases the retain count of the instance by one.

## See Also

### Managing the Object Lifecycle
- [- init](./api-3180945-init.md)
- [- release](./api-3180946-release.md)
  Releases the OSObject instance
- [- free](./api-3180944-free.md)
- [OSObjectPtr](../../DriverKit/osobjectptr.md)
- [OSObjectRef](../../DriverKit/osobjectref.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osobject/3180947-retain)*