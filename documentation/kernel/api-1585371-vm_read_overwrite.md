# vm_read_overwrite

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.0+

## Declaration

```c
kern_return_t vm_read_overwrite(vm_map_read_t target_task, vm_address_t address, vm_size_t size, vm_address_t data, vm_size_t *outsize);
```

## See Also

### Reads and Writes
- [vm_read](./api-1585350-vm_read.md)
- [vm_read_list](./api-1585516-vm_read_list.md)
- [vm_write](./api-1585462-vm_write.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1585371-vm_read_overwrite)*