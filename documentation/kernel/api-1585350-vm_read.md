# vm_read

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.0+

## Declaration

```c
kern_return_t vm_read(vm_map_read_t target_task, vm_address_t address, vm_size_t size, vm_offset_t *data, mach_msg_type_number_t *dataCnt);
```

## See Also

### Reads and Writes
- [vm_read_list](./api-1585516-vm_read_list.md)
- [vm_read_overwrite](./api-1585371-vm_read_overwrite.md)
- [vm_write](./api-1585462-vm_write.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1585350-vm_read)*