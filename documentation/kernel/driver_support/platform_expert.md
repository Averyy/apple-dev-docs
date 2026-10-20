# Platform Expert

**Framework**: Kernel  
**Role**: API Collection

## Topics

### Setup and Initialization
- [PE_init_cpu](../api-3081668-pe_init_cpu.md)
- [PE_init_iokit](../api-1553713-pe_init_iokit.md)
- [PE_init_panicheader](../api-2915275-pe_init_panicheader.md)
- [PE_init_platform](../api-1553616-pe_init_platform.md)
- [PE_init_printf](../api-1553650-pe_init_printf.md)
- [PE_init_taproot](../api-1553711-pe_init_taproot.md)
- [PE_boot_args](../api-1553674-pe_boot_args.md)
- [PE_parse_boot_argn](../api-1553680-pe_parse_boot_argn.md)
- [PE_initialize_console](../api-1553621-pe_initialize_console.md)
- [PE_install_interrupt_handler](../api-1553624-pe_install_interrupt_handler.md)
- [PE_create_console](../api-1553641-pe_create_console.md)
- [PE_current_console](../api-1553642-pe_current_console.md)
### CPU
- [PE_cpu_halt](../api-1553664-pe_cpu_halt.md)
- [PE_cpu_machine_init](../api-1553675-pe_cpu_machine_init.md)
- [PE_cpu_machine_quiesce](../api-1553608-pe_cpu_machine_quiesce.md)
- [PE_cpu_signal](../api-1553636-pe_cpu_signal.md)
- [PE_cpu_signal_cancel](../api-1553700-pe_cpu_signal_cancel.md)
- [PE_cpu_signal_deferred](../api-1553622-pe_cpu_signal_deferred.md)
- [PE_cpu_start](../api-1553604-pe_cpu_start.md)
### Debugging
- [PE_i_can_has_debugger](../api-1553651-pe_i_can_has_debugger.md)
- [PE_enter_debugger](../api-1553661-pe_enter_debugger.md)
- [PESavePanicInfo](../api-1451658-pesavepanicinfo.md)
- [PESavePanicInfoAction](../api-2915256-pesavepanicinfoaction.md)
- [PE_panic_hook](../api-3081669-pe_panic_hook.md)
- [PE_update_panicheader_nestedpanic](../api-2915277-pe_update_panicheader_nestedpani.md)
- [PE_get_offset_into_panic_region](../api-2915276-pe_get_offset_into_panic_region.md)
- [PEHaltRestart](../api-1451718-pehaltrestart.md)
### Configuration Details
- [PEGetCoprocessorVersion](../api-2936918-pegetcoprocessorversion.md)
- [PEGetGMTTimeOfDay](../api-1451653-pegetgmttimeofday.md)
- [PEGetMachineName](../api-1451550-pegetmachinename.md)
- [PEGetModelName](../api-1451697-pegetmodelname.md)
- [PEGetPlatformEpoch](../api-1451600-pegetplatformepoch.md)
- [PEGetUTCTimeOfDay](../api-1451638-pegetutctimeofday.md)
- [PESetGMTTimeOfDay](../api-1451645-pesetgmttimeofday.md)
- [PESetUTCTimeOfDay](../api-1451543-pesetutctimeofday.md)
- [PE_get_default](../api-1553618-pe_get_default.md)
- [PE_get_hotkey](../api-1553677-pe_get_hotkey.md)
- [PE_get_random_seed](../api-1553647-pe_get_random_seed.md)
- [PE_register_timebase_callback](../api-1553611-pe_register_timebase_callback.md)
- [PE_call_timebase_callback](../api-1553652-pe_call_timebase_callback.md)
- [PE_display_icon](../api-1553658-pe_display_icon.md)
- [PE_imgsrc_mount_supported](../api-1553644-pe_imgsrc_mount_supported.md)
- [PE_stub_poll_input](../api-3075349-pe_stub_poll_input.md)
### NVRAM
- [PEReadNVRAMProperty](../api-1451596-pereadnvramproperty.md)
- [PERemoveNVRAMProperty](../api-1451580-peremovenvramproperty.md)
- [PEWriteNVRAMBooleanProperty](../api-1451625-pewritenvrambooleanproperty.md)
- [PEWriteNVRAMProperty](../api-1451578-pewritenvramproperty.md)
- [PEWriteNVRAMPropertyWithCopy](../api-3151873-pewritenvrampropertywithcopy.md)

## See Also

### Default Devices
- [IOPlatformExpertDevice](../ioplatformexpertdevice.md)
- [IOPlatformDevice](../ioplatformdevice.md)
- [Device Tree](./device_tree.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/driver_support/platform_expert)*