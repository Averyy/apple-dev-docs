# task_zone_info_t

**Framework**: Kernel  
**Kind**: struct

**Availability**:
- macOS 10.7+

## Declaration

```swift
typedef struct task_zone_info_data {
    ...
} task_zone_info_t;
```

## Topics

### Instance Properties
- [tzi_alloc_size](task_zone_info_t/1569559-tzi_alloc_size.md)
- [tzi_caller_acct](task_zone_info_t/1569590-tzi_caller_acct.md)
- [tzi_collectable](task_zone_info_t/1569601-tzi_collectable.md)
- [tzi_count](task_zone_info_t/1569585-tzi_count.md)
- [tzi_cur_size](task_zone_info_t/1569560-tzi_cur_size.md)
- [tzi_elem_size](task_zone_info_t/1569577-tzi_elem_size.md)
- [tzi_exhaustible](task_zone_info_t/1569568-tzi_exhaustible.md)
- [tzi_max_size](task_zone_info_t/1569576-tzi_max_size.md)
- [tzi_sum_size](task_zone_info_t/1569602-tzi_sum_size.md)
- [tzi_task_alloc](task_zone_info_t/1569588-tzi_task_alloc.md)
- [tzi_task_free](task_zone_info_t/1569563-tzi_task_free.md)

## See Also

- [mach_task_flavor_t](mach_task_flavor_t.md)
- [task_absolutetime_info_t](task_absolutetime_info_t.md)
- [task_access_subsystem](task_access_subsystem.md)
- [task_affinity_tag_info_t](task_affinity_tag_info_t.md)
- [task_array_t](task_array_t.md)
- [task_basic_info_32_t](task_basic_info_32_t.md)
- [task_basic_info_64_t](task_basic_info_64_t.md)
- [task_basic_info_t](task_basic_info_t.md)
- [task_category_policy_t](task_category_policy_t.md)
- [task_delta_snapshot_v2](task_delta_snapshot_v2.md)
- [task_dyld_info_t](task_dyld_info_t.md)
- [task_events_info_t](task_events_info_t.md)
- [task_exc_guard_behavior_t](task_exc_guard_behavior_t.md)
- [task_extmod_info_t](task_extmod_info_t.md)
- [task_flags_info_t](task_flags_info_t.md)
- [task_flavor_t](task_flavor_t.md)
- [task_info_data_t](task_info_data_t.md)
- [task_info_t](task_info_t.md)
- [task_inspect_basic_counts_t](task_inspect_basic_counts_t.md)
- [task_inspect_flavor](task_inspect_flavor.md)
- [task_inspect_flavor_t](task_inspect_flavor_t.md)
- [task_inspect_info_t](task_inspect_info_t.md)
- [task_inspect_t](task_inspect_t.md)
- [task_kernelmemory_info_t](task_kernelmemory_info_t.md)
- [task_latency_qos](task_latency_qos.md)
- [task_latency_qos_t](task_latency_qos_t.md)
- [task_name_t](task_name_t.md)
- [task_policy_flavor_t](task_policy_flavor_t.md)
- [task_policy_t](task_policy_t.md)
- [task_port_array_t](task_port_array_t.md)
- [task_port_t](task_port_t.md)
- [task_power_info_t](task_power_info_t.md)
- [task_power_info_v2_t](task_power_info_v2_t.md)
- [task_purgable_info_t](task_purgable_info_t.md)
- [task_restartable_range_array_t](task_restartable_range_array_t.md)
- [task_snapshot](task_snapshot.md)
- [task_snapshot_flags](task_snapshot_flags.md)
- [task_snapshot_v2](task_snapshot_v2.md)
- [task_special_port_t](task_special_port_t.md)
- [task_suspension_token_t](task_suspension_token_t.md)
- [task_t](task_t.md)
- [task_thread_times_info_t](task_thread_times_info_t.md)
- [task_throughput_qos](task_throughput_qos.md)
- [task_throughput_qos_t](task_throughput_qos_t.md)
- [task_trace_memory_info_t](task_trace_memory_info_t.md)
- [task_vm_info_t](task_vm_info_t.md)
- [task_wait_state_info_t](task_wait_state_info_t.md)
- [task_zone_info_array_t](task_zone_info_array_t.md)
- [mach_task_basic_info_t](mach_task_basic_info_t.md)
- [mach_task_basic_info_data_t](mach_task_basic_info_data_t.md)
- [task_absolutetime_info_data_t](task_absolutetime_info_data_t.md)
- [task_affinity_tag_info_data_t](task_affinity_tag_info_data_t.md)
- [task_basic_info_32_data_t](task_basic_info_32_data_t.md)
- [task_basic_info_64_data_t](task_basic_info_64_data_t.md)
- [task_basic_info_data_t](task_basic_info_data_t.md)
- [task_category_policy_data_t](task_category_policy_data_t.md)
- [task_crashinfo_item_t](task_crashinfo_item_t.md)
- [task_dyld_info_data_t](task_dyld_info_data_t.md)
- [task_events_info_data_t](task_events_info_data_t.md)
- [task_extmod_info_data_t](task_extmod_info_data_t.md)
- [task_flags_info_data_t](task_flags_info_data_t.md)
- [task_gate_t](task_gate_t.md)
- [task_inspect_basic_counts_data_t](task_inspect_basic_counts_data_t.md)
- [task_kernelmemory_info_data_t](task_kernelmemory_info_data_t.md)
- [task_power_info_data_t](task_power_info_data_t.md)
- [task_power_info_v2_data_t](task_power_info_v2_data_t.md)
- [task_qos_policy_t](task_qos_policy_t.md)
- [task_restartable_range_t](task_restartable_range_t.md)
- [task_thread_times_info_data_t](task_thread_times_info_data_t.md)
- [task_trace_memory_info_data_t](task_trace_memory_info_data_t.md)
- [task_vm_info_data_t](task_vm_info_data_t.md)
- [task_wait_state_info_data_t](task_wait_state_info_data_t.md)
- [check_task_access](1495471-check_task_access.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/task_zone_info_t)*