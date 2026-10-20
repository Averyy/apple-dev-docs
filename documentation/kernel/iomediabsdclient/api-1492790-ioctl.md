# ioctl

**Framework**: Kernel  
**Kind**: instm  
**Role**: Instance Method

**Availability**:
- macOS 10.11.4+

## Declaration

```cpp
virtual int ioctl(dev_t dev, u_long cmd, caddr_t data, int flags, proc_t proc);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iomediabsdclient/1492790-ioctl)*