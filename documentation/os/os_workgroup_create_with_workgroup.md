# os_workgroup_create_with_workgroup

**Framework**: os  
**Kind**: func  
**Role**: Function

Create a new workgroup that is bound to the specified workgroup.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```c
extern os_workgroup_tos_workgroup_create_with_workgroup(const char *name, os_workgroup_t wg);
```

## Return Value

A new workgroup of the same type, and with the same attributes, as the provided workgroup.

## Discussion

Use this function to create new references to an existing workgroup in your app. You might create an original workgroup from one thread and create copies of that workgroup for additional threads. The system manages threads from the original workgroup and threads from any copied workgroups as if they belonged to the same group. The use of separate groups avoids the need for multiple threads to coordinate access to a shared data structure.

The new workgroup doesn’t contain any joined threads initially, and it doesn’t contain any context data. This function sets the name of the new workgroup to the value in the `name` property and configures a reference to the original group in the `wg` parameter.

You cannot use the returned workgroup object to make configuration changes to the original workgroup. You also cannot call any scheduling functions for the workgroup. For example, attempts to start, stop, or update the deadlines for an interval workgroup return an error when you use the returned workgroup object. Instead, make all configuration and scheduling calls using only the original workgroup object.

## Parameters

- `name`: An optional name for the new workgroup. Use this name to identify the workgroups you create. You may specify `NULL` for this parameter.
- `wg`: An existing workgroup object.

## See Also

### Common Utilities
- [os_workgroup_create_with_port](./os_workgroup_create_with_port.md)
  Creates a new workgroup that is bound to the workgroup with the specified Mach port.
- [os_workgroup_copy_port](./os_workgroup_copy_port.md)
  Returns the Mach port associated with the workgroup.
- [os_workgroup_t](./os_workgroup_t.md)
  An opaque object representing a default workgroup in the current process.
- [os_workgroup_attr_t](./os_workgroup_attr_t.md)
  An opaque structure for storing workgroup-related attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/os_workgroup_create_with_workgroup)*