# vm_write

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.0+

## Declaration

```c
kern_return_t vm_write(vm_map_t target_task, vm_address_t address, vm_offset_t data, mach_msg_type_number_t dataCnt);
```

## See Also

### Reads and Writes
- [vm_read](./api-1585350-vm_read.md)
- [vm_read_list](./api-1585516-vm_read_list.md)
- [vm_read_overwrite](./api-1585371-vm_read_overwrite.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1585462-vm_write)*