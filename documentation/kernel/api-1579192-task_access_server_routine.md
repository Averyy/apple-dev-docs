# task_access_server_routine

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.5+

## Declaration

```swift
mig_routine_t task_access_server_routine(mach_msg_header_t *InHeadP);
```

## See Also

- [current_task](1574414-current_task.md)
- [task_access_server](1579197-task_access_server.md)
- [task_assign](1537803-task_assign.md)
- [task_assign_default](1537916-task_assign_default.md)
- [task_create](1538088-task_create.md)
- [task_deallocate](1574412-task_deallocate.md)
- [task_generate_corpse](1646547-task_generate_corpse.md)
- [task_get_assignment](1537882-task_get_assignment.md)
- [task_get_dyld_image_infos](1646553-task_get_dyld_image_infos.md)
- [task_get_emulation_vector](1537831-task_get_emulation_vector.md)
- [task_get_exc_guard_behavior](3197704-task_get_exc_guard_behavior.md)
- [task_get_exception_ports](1537860-task_get_exception_ports.md)
- [task_get_mach_voucher](1537867-task_get_mach_voucher.md)
- [task_get_special_port](1537682-task_get_special_port.md)
- [task_get_state](1537707-task_get_state.md)
- [task_info](1537934-task_info.md)
- [task_inspect](2876476-task_inspect.md)
- [task_is_driver](3181819-task_is_driver.md)
- [task_ledgers_footprint](3181820-task_ledgers_footprint.md)
- [task_map_corpse_info](1646533-task_map_corpse_info.md)
- [task_map_corpse_info_64](1911639-task_map_corpse_info_64.md)
- [task_policy](1537990-task_policy.md)
- [task_policy_get](1537778-task_policy_get.md)
- [task_policy_set](1537790-task_policy_set.md)
- [task_purgable_info](1538155-task_purgable_info.md)
- [task_reference](1574413-task_reference.md)
- [task_register_dyld_get_process_state](1646549-task_register_dyld_get_process_s.md)
- [task_register_dyld_image_infos](1646550-task_register_dyld_image_infos.md)
- [task_register_dyld_set_dyld_state](1646572-task_register_dyld_set_dyld_stat.md)
- [task_register_dyld_shared_cache_image_info](1646581-task_register_dyld_shared_cache_.md)
- [task_restartable_ranges_register](3143268-task_restartable_ranges_register.md)
- [task_restartable_ranges_synchronize](3143269-task_restartable_ranges_synchron.md)
- [task_resume](1537977-task_resume.md)
- [task_resume2](1537653-task_resume2.md)
- [task_sample](1537655-task_sample.md)
- [task_self_region_footprint](2937634-task_self_region_footprint.md)
- [task_self_region_footprint_set](2937633-task_self_region_footprint_set.md)
- [task_set_emulation](1537794-task_set_emulation.md)
- [task_set_emulation_vector](1537907-task_set_emulation_vector.md)
- [task_set_exc_guard_behavior](3197705-task_set_exc_guard_behavior.md)
- [task_set_exception_ports](1538049-task_set_exception_ports.md)
- [task_set_info](1537704-task_set_info.md)
- [task_set_mach_voucher](1538121-task_set_mach_voucher.md)
- [task_set_memory_ownership_transfer](3194340-task_set_memory_ownership_transf.md)
- [task_set_phys_footprint_limit](1538131-task_set_phys_footprint_limit.md)
- [task_set_policy](1537717-task_set_policy.md)
- [task_set_port_space](1578836-task_set_port_space.md)
- [task_set_ras_pc](1537742-task_set_ras_pc.md)
- [task_set_special_port](1537676-task_set_special_port.md)
- [task_set_state](1537962-task_set_state.md)
- [task_suspend](1538100-task_suspend.md)
- [task_suspend2](1538207-task_suspend2.md)
- [task_suspension_token_deallocate](1574411-task_suspension_token_deallocate.md)
- [task_swap_exception_ports](1537854-task_swap_exception_ports.md)
- [task_swap_mach_voucher](1537722-task_swap_mach_voucher.md)
- [task_terminate](1537817-task_terminate.md)
- [task_threads](1537751-task_threads.md)
- [task_unregister_dyld_image_infos](1646587-task_unregister_dyld_image_infos.md)
- [task_wire](1585470-task_wire.md)
- [task_zone_info](1537645-task_zone_info.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1579192-task_access_server_routine)*