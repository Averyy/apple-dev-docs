# Platform Expert

**Framework**: Kernel

## Topics

### Setup and Initialization
- [PE_init_cpu](3081668-pe_init_cpu.md)
- [PE_init_iokit](1553713-pe_init_iokit.md)
- [PE_init_panicheader](2915275-pe_init_panicheader.md)
- [PE_init_platform](1553616-pe_init_platform.md)
- [PE_init_printf](1553650-pe_init_printf.md)
- [PE_init_taproot](1553711-pe_init_taproot.md)
- [PE_boot_args](1553674-pe_boot_args.md)
- [PE_parse_boot_argn](1553680-pe_parse_boot_argn.md)
- [PE_initialize_console](1553621-pe_initialize_console.md)
- [PE_install_interrupt_handler](1553624-pe_install_interrupt_handler.md)
- [PE_create_console](1553641-pe_create_console.md)
- [PE_current_console](1553642-pe_current_console.md)
### CPU
- [PE_cpu_halt](1553664-pe_cpu_halt.md)
- [PE_cpu_machine_init](1553675-pe_cpu_machine_init.md)
- [PE_cpu_machine_quiesce](1553608-pe_cpu_machine_quiesce.md)
- [PE_cpu_signal](1553636-pe_cpu_signal.md)
- [PE_cpu_signal_cancel](1553700-pe_cpu_signal_cancel.md)
- [PE_cpu_signal_deferred](1553622-pe_cpu_signal_deferred.md)
- [PE_cpu_start](1553604-pe_cpu_start.md)
### Debugging
- [PE_i_can_has_debugger](1553651-pe_i_can_has_debugger.md)
- [PE_enter_debugger](1553661-pe_enter_debugger.md)
- [PESavePanicInfo](1451658-pesavepanicinfo.md)
- [PESavePanicInfoAction](2915256-pesavepanicinfoaction.md)
- [PE_panic_hook](3081669-pe_panic_hook.md)
- [PE_update_panicheader_nestedpanic](2915277-pe_update_panicheader_nestedpani.md)
- [PE_get_offset_into_panic_region](2915276-pe_get_offset_into_panic_region.md)
- [PEHaltRestart](1451718-pehaltrestart.md)
### Configuration Details
- [PEGetCoprocessorVersion](2936918-pegetcoprocessorversion.md)
- [PEGetGMTTimeOfDay](1451653-pegetgmttimeofday.md)
- [PEGetMachineName](1451550-pegetmachinename.md)
- [PEGetModelName](1451697-pegetmodelname.md)
- [PEGetPlatformEpoch](1451600-pegetplatformepoch.md)
- [PEGetUTCTimeOfDay](1451638-pegetutctimeofday.md)
- [PESetGMTTimeOfDay](1451645-pesetgmttimeofday.md)
- [PESetUTCTimeOfDay](1451543-pesetutctimeofday.md)
- [PE_get_default](1553618-pe_get_default.md)
- [PE_get_hotkey](1553677-pe_get_hotkey.md)
- [PE_get_random_seed](1553647-pe_get_random_seed.md)
- [PE_register_timebase_callback](1553611-pe_register_timebase_callback.md)
- [PE_call_timebase_callback](1553652-pe_call_timebase_callback.md)
- [PE_display_icon](1553658-pe_display_icon.md)
- [PE_imgsrc_mount_supported](1553644-pe_imgsrc_mount_supported.md)
- [PE_stub_poll_input](3075349-pe_stub_poll_input.md)
### NVRAM
- [PEReadNVRAMProperty](1451596-pereadnvramproperty.md)
- [PERemoveNVRAMProperty](1451580-peremovenvramproperty.md)
- [PEWriteNVRAMBooleanProperty](1451625-pewritenvrambooleanproperty.md)
- [PEWriteNVRAMProperty](1451578-pewritenvramproperty.md)
- [PEWriteNVRAMPropertyWithCopy](3151873-pewritenvrampropertywithcopy.md)

## See Also

- [IOPlatformExpertDevice](ioplatformexpertdevice.md)
- [IOPlatformDevice](ioplatformdevice.md)
- [Device Tree](driver_support/device_tree.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/driver_support/platform_expert)*