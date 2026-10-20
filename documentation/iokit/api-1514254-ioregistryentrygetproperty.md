# IORegistryEntryGetProperty(_:_:_:_:)

**Framework**: IOKit  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.0+

## Declaration

```swift
func IORegistryEntryGetProperty(_ entry: io_registry_entry_t, _ propertyName: UnsafePointer<CChar>!, _ buffer: UnsafeMutablePointer<CChar>!, _ size: UnsafeMutablePointer<UInt32>!) -> kern_return_t
```

```c
kern_return_t IORegistryEntryGetProperty(io_registry_entry_t entry, const io_name_t propertyName, io_struct_inband_t buffer, uint32_t *size);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/1514254-ioregistryentrygetproperty)*