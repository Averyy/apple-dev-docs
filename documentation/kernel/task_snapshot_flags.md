# task_snapshot_flags

**Framework**: Kernel  
**Kind**: tag

**Availability**:
- macOS 10.9+

## Declaration

```swift
enum task_snapshot_flags : unsigned long {
    ...
};
```

## Topics

### Constants
- [kFrozen](task_snapshot_flags/kfrozen.md)
- [kPidSuspended](task_snapshot_flags/kpidsuspended.md)
- [kTaskDarwinBG](task_snapshot_flags/ktaskdarwinbg.md)
- [kTaskExtDarwinBG](task_snapshot_flags/ktaskextdarwinbg.md)
- [kTaskIsBoosted](task_snapshot_flags/ktaskisboosted.md)
- [kTaskIsForeground](task_snapshot_flags/ktaskisforeground.md)
- [kTaskIsImpDonor](task_snapshot_flags/ktaskisimpdonor.md)
- [kTaskIsLiveImpDonor](task_snapshot_flags/ktaskisliveimpdonor.md)
- [kTaskIsSuppressed](task_snapshot_flags/ktaskissuppressed.md)
- [kTaskIsTimerThrottled](task_snapshot_flags/ktaskistimerthrottled.md)
- [kTaskRsrcFlagged](task_snapshot_flags/ktaskrsrcflagged.md)
- [kTaskVisNonvisible](task_snapshot_flags/ktaskvisnonvisible.md)
- [kTaskVisVisible](task_snapshot_flags/ktaskvisvisible.md)
- [kTerminatedSnapshot](task_snapshot_flags/kterminatedsnapshot.md)
- [kTaskIsDirty](task_snapshot_flags/ktaskisdirty.md)
- [kTaskSharedRegionInfoUnavailable](task_snapshot_flags/ktasksharedregioninfounavailable.md)
- [kTaskUUIDInfoFaultedIn](task_snapshot_flags/ktaskuuidinfofaultedin.md)
- [kTaskUUIDInfoMissing](task_snapshot_flags/ktaskuuidinfomissing.md)
- [kTaskUUIDInfoTriedFault](task_snapshot_flags/ktaskuuidinfotriedfault.md)
- [kTaskWqExceededConstrainedThreadLimit](task_snapshot_flags/ktaskwqexceededconstrainedthreadlimit.md)
- [kTaskWqExceededTotalThreadLimit](task_snapshot_flags/ktaskwqexceededtotalthreadlimit.md)
- [kTaskWqFlagsAvailable](task_snapshot_flags/ktaskwqflagsavailable.md)
- [kTaskAllowIdleExit](task_snapshot_flags/ktaskallowidleexit.md)
- [kTaskDyldCompactInfoFaultedIn](task_snapshot_flags/ktaskdyldcompactinfofaultedin.md)
- [kTaskDyldCompactInfoMissing](task_snapshot_flags/ktaskdyldcompactinfomissing.md)
- [kTaskDyldCompactInfoNone](task_snapshot_flags/ktaskdyldcompactinfonone.md)
- [kTaskDyldCompactInfoTooBig](task_snapshot_flags/ktaskdyldcompactinfotoobig.md)
- [kTaskDyldCompactInfoTriedFault](task_snapshot_flags/ktaskdyldcompactinfotriedfault.md)
- [kTaskIsDirtyTracked](task_snapshot_flags/ktaskisdirtytracked.md)
- [kTaskIsTranslated](task_snapshot_flags/ktaskistranslated.md)
- [kTaskSharedRegionNone](task_snapshot_flags/ktasksharedregionnone.md)
- [kTaskSharedRegionOther](task_snapshot_flags/ktasksharedregionother.md)
- [kTaskSharedRegionSystem](task_snapshot_flags/ktasksharedregionsystem.md)
- [kTaskTALEngaged](task_snapshot_flags/ktasktalengaged.md)
- [kTaskWqExceededActiveConstrainedThreadLimit](task_snapshot_flags/ktaskwqexceededactiveconstrainedthreadlimit.md)
- [kTaskWqExceededCooperativeThreadLimit](task_snapshot_flags/ktaskwqexceededcooperativethreadlimit.md)

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
- [task_zone_info_t](task_zone_info_t.md)
- [check_task_access](1495471-check_task_access.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/task_snapshot_flags)*