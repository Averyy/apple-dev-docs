# sysctlbyname

**Framework**: Kernel  
**Kind**: func

Gets or sets information about the system and environment.

**Availability**:
- macOS 10.0+

## Declaration

```swift
int sysctlbyname(const char *, void *, size_t *, void *, size_t);
```

#### Return_value

0 on success, or an error code that indicates a problem occurred. Possible error codes include `EFAULT`, `EINVAL`, `ENOMEM`, `ENOTDIR`, `EISDIR`, `ENOENT`, and `EPERM`.

#### Discussion

This function offers a programmatic alternative to the sysctl command-line tool. Use it to get or set relevant system information, and to make decisions dynamically based on the current system information. For example, you might use the `hw.cachelinesize` attribute to align data in your data structures. Making decisions dynamically is especially important for universal binaries that run on Apple silicon or Intel-based Mac computers. 

The following example shows how to retrieve the cache line size using this function.

```occ
int64_t cacheLineSize() {
    int64_t ret = 0;
    size_t size = sizeof(ret);
    
    if (sysctlbyname("hw.cachelinesize", &ret, &size, NULL, 0) == -1) {
        NSLog(@"cacheLineSize failed with error: %d", errno);
        
        return -1;
    }
    
    return ret;
}
```

## Parameters

- `name`: The ASCII name of the requested attribute. To obtain a list of attribute names for the current system, run `sysctl -a` from Terminal. 
- `oldp`: A pointer to a buffer that receives the requested data. Specify the size of this buffer using the `oldlenp` parameter. The function copies the requested data into this buffer as space allows. If the buffer is too small to hold all the data, the function updates the `oldlenp` parameter with the required size. Specify `NULL` if you don’t want to get the attribute’s value. For example, set this parameter to `NULL` and specify a valid parameter in `oldlenp` to get the size of the data. 
- `oldlenp`: A variable that contains the number of bytes in the buffer in the `oldp` parameter. If the amount of data is greater than the value in this parameter, the function updates this parameter to the required size and returns `ENOMEM`. (The function doesn’t modify the value if it’s larger than or equal to the amount of available data). Specify `NULL` if you don’t want to get the attribute’s value. 
- `newp`: A pointer to a buffer that contains new data to assign to the attribute. The function copies the data from this buffer to the attribute. You must specify the size of this buffer using the `newlen` parameter. Specify `NULL` if you don’t want to set the attribute’s value. A process must have the root-level privileges to set system information.
- `newlen`: A variable that contains the size of the buffer in the `newp` parameter, in bytes. Specify `0` if you don’t want to set the attribute’s value.

## Topics

### Parameters
- [Determining system capabilities](1387446-sysctlbyname/determining_system_capabilities.md)
  Interrogate the system for processor, cache, and topology information.
- [Determining Instruction Set Characteristics](1387446-sysctlbyname/determining_instruction_set_characteristics.md)
  Interrogate the system for details about the instruction set.

## See Also

- [sysctl_handle_int](1404317-sysctl_handle_int.md)
- [sysctl_handle_int2quad](1404249-sysctl_handle_int2quad.md)
- [sysctl_handle_long](1404379-sysctl_handle_long.md)
- [sysctl_handle_opaque](1404289-sysctl_handle_opaque.md)
- [sysctl_handle_quad](1404243-sysctl_handle_quad.md)
- [sysctl_handle_string](1404297-sysctl_handle_string.md)
- [sysctl_io_number](1404223-sysctl_io_number.md)
- [sysctl_io_opaque](1404235-sysctl_io_opaque.md)
- [sysctl_io_string](1404325-sysctl_io_string.md)
- [sysctl_register_oid](1404241-sysctl_register_oid.md)
- [sysctl_unregister_oid](1404403-sysctl_unregister_oid.md)
- [sysctl__children](sysctl_children.md)
- [sysctl__debug_children](sysctl_debug_children.md)
- [sysctl__hw_children](sysctl_hw_children.md)
- [sysctl__kern_children](sysctl_kern_children.md)
- [sysctl__machdep_children](sysctl_machdep_children.md)
- [sysctl__net_children](sysctl_net_children.md)
- [sysctl__sysctl_children](sysctl_sysctl_children.md)
- [sysctl__user_children](sysctl_user_children.md)
- [sysctl__vfs_children](sysctl_vfs_children.md)
- [sysctl__vm_children](sysctl_vm_children.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1387446-sysctlbyname)*