# architecture

**Framework**: Kernel

Access machine-level and architectural information about the current platform.

## Topics

### i386
- [hlt](2870529-hlt.md)
- [inb](1537072-inb.md)
- [do_cpuid](1580421-do_cpuid.md)
- [get_cr0](1571251-get_cr0.md)
- [get_cr2](1571176-get_cr2.md)
- [get_cr3_base](1571286-get_cr3_base.md)
- [get_cr3_raw](1571283-get_cr3_raw.md)
- [get_cr4](1571378-get_cr4.md)
- [get_crc_table](1546895-get_crc_table.md)
- [get_ds](1571328-get_ds.md)
- [get_es](1571424-get_es.md)
- [get_fs](1571293-get_fs.md)
- [get_gs](1571339-get_gs.md)
- [get_ss](1571429-get_ss.md)
- [get_tr](1571379-get_tr.md)
- [cpuid](1580486-cpuid.md)
- [cpuid_cpu_display](1580592-cpuid_cpu_display.md)
- [cpuid_cpufamily](1580564-cpuid_cpufamily.md)
- [cpuid_cpusubtype](1580514-cpuid_cpusubtype.md)
- [cpuid_cputype](1580625-cpuid_cputype.md)
- [cpuid_extfeature_display](1580551-cpuid_extfeature_display.md)
- [cpuid_extfeatures](1580645-cpuid_extfeatures.md)
- [cpuid_family](1580535-cpuid_family.md)
- [cpuid_feature_display](1580655-cpuid_feature_display.md)
- [cpuid_features](1580435-cpuid_features.md)
- [cpuid_get_extfeature_names](1580527-cpuid_get_extfeature_names.md)
- [cpuid_get_feature_names](1580651-cpuid_get_feature_names.md)
- [cpuid_get_leaf7_extfeature_names](3203729-cpuid_get_leaf7_extfeature_names.md)
- [cpuid_get_leaf7_feature_names](1580541-cpuid_get_leaf7_feature_names.md)
- [cpuid_info](1580462-cpuid_info.md)
- [cpuid_leaf7_extfeatures](3203730-cpuid_leaf7_extfeatures.md)
- [cpuid_leaf7_features](1580437-cpuid_leaf7_features.md)
- [cpuid_set_info](1580542-cpuid_set_info.md)
- [clac](1571382-clac.md)
- [clz](1441034-clz.md)
- [clear_ts](1571249-clear_ts.md)
- [cninit](1537074-cninit.md)
- [cpuid_arch_perf_leaf_t](cpuid_arch_perf_leaf_t.md)
- [cpuid_cache_desc_t](cpuid_cache_desc_t.md)
- [cpuid_mwait_leaf_t](cpuid_mwait_leaf_t.md)
- [cpuid_thermal_leaf_t](cpuid_thermal_leaf_t.md)
- [cpuid_tsc_leaf_t](cpuid_tsc_leaf_t.md)
- [cpuid_xsave_leaf_t](cpuid_xsave_leaf_t.md)
- [i386_cpu_info_t](i386_cpu_info_t.md)
- [i386_exception_state_t](i386_exception_state_t.md)
- [i386_float_state_t](i386_float_state_t.md)
- [i386_thread_state_t](i386_thread_state_t.md)
### EFI
- [EFI_CONFIGURATION_TABLE_32](efi_configuration_table_32.md)
- [EFI_CONFIGURATION_TABLE_64](efi_configuration_table_64.md)
- [EFI_GUID](efi_guid.md)
- [EFI_MEMORY_DESCRIPTOR](efi_memory_descriptor.md)
- [EFI_RUNTIME_SERVICES_32](efi_runtime_services_32.md)
- [EFI_RUNTIME_SERVICES_64](efi_runtime_services_64.md)
- [EFI_SYSTEM_TABLE_32](efi_system_table_32.md)
- [EFI_SYSTEM_TABLE_64](efi_system_table_64.md)
- [EFI_TABLE_HEADER](efi_table_header.md)
- [EFI_TIME](efi_time.md)
- [EFI_TIME_CAPABILITIES](efi_time_capabilities.md)
- [EfiMemoryRange](efimemoryrange.md)
- [EFI_BOOLEAN](efi_boolean.md)
- [EFI_CHAR16](efi_char16.md)
- [EFI_CHAR32](efi_char32.md)
- [EFI_CHAR64](efi_char64.md)
- [EFI_CHAR8](efi_char8.md)
- [EFI_CONVERT_POINTER](efi_convert_pointer.md)
- [EFI_GET_NEXT_HIGH_MONO_COUNT](efi_get_next_high_mono_count.md)
- [EFI_GET_NEXT_VARIABLE_NAME](efi_get_next_variable_name.md)
- [EFI_GET_TIME](efi_get_time.md)
- [EFI_GET_VARIABLE](efi_get_variable.md)
- [EFI_GET_WAKEUP_TIME](efi_get_wakeup_time.md)
- [EFI_HANDLE32](efi_handle32.md)
- [EFI_HANDLE64](efi_handle64.md)
- [EFI_INT16](efi_int16.md)
- [EFI_INT32](efi_int32.md)
- [EFI_INT64](efi_int64.md)
- [EFI_INT8](efi_int8.md)
- [EFI_PHYSICAL_ADDRESS](efi_physical_address.md)
- [EFI_PTR32](efi_ptr32.md)
- [EFI_PTR64](efi_ptr64.md)
- [EFI_RESET_SYSTEM](efi_reset_system.md)
- [EFI_SET_TIME](efi_set_time.md)
- [EFI_SET_VARIABLE](efi_set_variable.md)
- [EFI_SET_VIRTUAL_ADDRESS_MAP](efi_set_virtual_address_map.md)
- [EFI_SET_WAKEUP_TIME](efi_set_wakeup_time.md)
- [EFI_STATUS](efi_status.md)
- [EFI_UINT16](efi_uint16.md)
- [EFI_UINT32](efi_uint32.md)
- [EFI_UINT64](efi_uint64.md)
- [EFI_UINT8](efi_uint8.md)
- [EFI_UINTN](efi_uintn.md)
- [EFI_VIRTUAL_ADDRESS](efi_virtual_address.md)

## See Also

- [bsm](bsm.md)
  Audit resource usage on the system.
- [hfs](hfs.md)
  Access HFS file-system data structures. 
- [kern](kern.md)
  Access kernel-level interfaces including clock, task, kernel extension, lock, and compression utilities.  
- [Math](math.md)
  Perform mathematical operations and manipulate integer, float, and double values.  
- [miscfs](miscfs.md)
  Access device nodes and other file-system entities.
- [net](net.md)
  Access network-related utilities.
- [Strings](strings.md)
  Compare, convert, and catenate strings and access the resulting content of those strings.
- [sys](sys.md)
  Access general system utilities for time, file systems, and system information.
- [vfs](vfs.md)
  Access the virtual file-system interfaces.
- [vm](vm.md)
  Interact with the virtual memory system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/architecture)*