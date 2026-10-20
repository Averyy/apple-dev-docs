# mach_memory_entry_ownership

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.15+

## Declaration

```c
kern_return_t mach_memory_entry_ownership(mem_entry_name_port_t mem_entry, task_t owner, int ledger_tag, int ledger_flags);
```

## See Also

### Memory Mapping
- [vm_map](./api-1585510-vm_map.md)
- [vm_map_64](./api-1585418-vm_map_64.md)
- [vm_map_exec_lockdown](./api-2937355-vm_map_exec_lockdown.md)
- [vm_map_page_query](./api-1585356-vm_map_page_query.md)
- [vm_mapped_pages_info](./api-1585469-vm_mapped_pages_info.md)
- [vm_remap](./api-1585336-vm_remap.md)
- [mach_make_memory_entry](./api-1585446-mach_make_memory_entry.md)
- [mach_make_memory_entry_64](./api-1585405-mach_make_memory_entry_64.md)
- [mach_memory_entry_access_tracking](./api-2967371-mach_memory_entry_access_trackin.md)
- [mach_memory_entry_purgable_control](./api-2967372-mach_memory_entry_purgable_contr.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/3143277-mach_memory_entry_ownership)*