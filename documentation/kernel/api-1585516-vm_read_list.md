# vm_read_list

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.0+

## Declaration

```c
kern_return_t vm_read_list(vm_map_read_t target_task, vm_read_entry_t data_list, natural_t count);
```

## See Also

### Reads and Writes
- [vm_read](./api-1585350-vm_read.md)
- [vm_read_overwrite](./api-1585371-vm_read_overwrite.md)
- [vm_write](./api-1585462-vm_write.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1585516-vm_read_list)*