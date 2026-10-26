# os_workgroup_attr_t

**Framework**: os  
**Kind**: typealias  
**Role**: Type Alias

An opaque structure for storing workgroup-related attributes.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```c
typedef struct os_workgroup_attr_opaque_s * os_workgroup_attr_t;
```

## See Also

### Common Utilities
- [os_workgroup_create_with_workgroup](./os_workgroup_create_with_workgroup.md)
  Create a new workgroup that is bound to the specified workgroup.
- [os_workgroup_create_with_port](./os_workgroup_create_with_port.md)
  Creates a new workgroup that is bound to the workgroup with the specified Mach port.
- [os_workgroup_copy_port](./os_workgroup_copy_port.md)
  Returns the Mach port associated with the workgroup.
- [os_workgroup_t](./os_workgroup_t.md)
  An opaque object representing a default workgroup in the current process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/os_workgroup_attr_t)*