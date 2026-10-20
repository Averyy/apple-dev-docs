# IODestroyPlugInInterface(_:)

**Framework**: IOKit  
**Kind**: func  
**Role**: Function

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func IODestroyPlugInInterface(_ interface: UnsafeMutablePointer<UnsafeMutablePointer<IOCFPlugInInterface>?>!) -> kern_return_t
```

```c
kern_return_t IODestroyPlugInInterface(IOCFPlugInInterface **interface);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/1412425-iodestroyplugininterface)*