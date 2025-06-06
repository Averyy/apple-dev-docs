# thread_snapshot

**Framework**: Kernel  
**Kind**: tag

**Availability**:
- macOS 10.6+

## Declaration

```swift
struct thread_snapshot {
    ...
};
```

## Topics

### Instance Properties
- [continuation](thread_snapshot/1551671-continuation.md)
- [data_count](thread_snapshot/1551790-data_count.md)
- [data_size](thread_snapshot/1551857-data_size.md)
- [disk_reads_count](thread_snapshot/1551744-disk_reads_count.md)
- [disk_reads_size](thread_snapshot/1551844-disk_reads_size.md)
- [disk_writes_count](thread_snapshot/1551735-disk_writes_count.md)
- [disk_writes_size](thread_snapshot/1551728-disk_writes_size.md)
- [io_priority_count](thread_snapshot/1551812-io_priority_count.md)
- [io_priority_size](thread_snapshot/1551707-io_priority_size.md)
- [io_tier](thread_snapshot/1551855-io_tier.md)
- [metadata_count](thread_snapshot/1551718-metadata_count.md)
- [metadata_size](thread_snapshot/1551827-metadata_size.md)
- [nkern_frames](thread_snapshot/1551775-nkern_frames.md)
- [non_paging_count](thread_snapshot/1551875-non_paging_count.md)
- [non_paging_size](thread_snapshot/1551749-non_paging_size.md)
- [nuser_frames](thread_snapshot/1551809-nuser_frames.md)
- [paging_count](thread_snapshot/1551702-paging_count.md)
- [paging_size](thread_snapshot/1551792-paging_size.md)
- [priority](thread_snapshot/1551791-priority.md)
- [pth_name](thread_snapshot/1551805-pth_name.md)
- [sched_flags](thread_snapshot/1551748-sched_flags.md)
- [sched_pri](thread_snapshot/1551780-sched_pri.md)
- [snapshot_magic](thread_snapshot/1551842-snapshot_magic.md)
- [ss_flags](thread_snapshot/1551650-ss_flags.md)
- [state](thread_snapshot/1551836-state.md)
- [system_time](thread_snapshot/1551782-system_time.md)
- [thread_id](thread_snapshot/1551862-thread_id.md)
- [total_syscalls](thread_snapshot/1551730-total_syscalls.md)
- [ts_qos](thread_snapshot/1551727-ts_qos.md)
- [ts_rqos](thread_snapshot/1551736-ts_rqos.md)
- [ts_rqos_override](thread_snapshot/1551781-ts_rqos_override.md)
- [user_time](thread_snapshot/1551767-user_time.md)
- [voucher_identifier](thread_snapshot/1551865-voucher_identifier.md)
- [wait_event](thread_snapshot/1551636-wait_event.md)

## See Also

- [current_thread](1429092-current_thread.md)
- [thread_abort](1418578-thread_abort.md)
- [thread_abort_safely](1418913-thread_abort_safely.md)
- [thread_assign](1418581-thread_assign.md)
- [thread_assign_default](1418700-thread_assign_default.md)
- [thread_block](1524368-thread_block.md)
- [thread_block_parameter](1524369-thread_block_parameter.md)
- [thread_call_allocate](1444263-thread_call_allocate.md)
  Allocate a thread call to execute with default (high) priority.
- [thread_call_allocate_with_options](2869840-thread_call_allocate_with_option.md)
- [thread_call_allocate_with_priority](1444267-thread_call_allocate_with_priori.md)
  Allocate a thread call to execute with a specified priority.
- [thread_call_cancel](1444264-thread_call_cancel.md)
  Attempt to cancel a pending invocation of a thread call.
- [thread_call_cancel_wait](1444261-thread_call_cancel_wait.md)
  Attempt to cancel a pending invocation of a thread call. If unable to cancel, wait for current invocation to finish.
- [thread_call_enter](1444247-thread_call_enter.md)
  Submit a thread call work item for immediate execution.
- [thread_call_enter1](1444257-thread_call_enter1.md)
  Submit a thread call work item for immediate execution, with an extra parameter.
- [thread_call_enter1_delayed](1444249-thread_call_enter1_delayed.md)
  Submit a thread call to be executed at some point in the future, with an extra parameter.
- [thread_call_enter_delayed](1444259-thread_call_enter_delayed.md)
  Submit a thread call to be executed at some point in the future.
- [thread_call_free](1444245-thread_call_free.md)
  Release a thread call.
- [thread_call_isactive](1444253-thread_call_isactive.md)
  Determine whether a thread call is pending or currently executing.
- [thread_create](1538152-thread_create.md)
- [thread_create_running](1537886-thread_create_running.md)
- [thread_deallocate](1429095-thread_deallocate.md)
- [thread_depress_abort](1418712-thread_depress_abort.md)
- [thread_get_assignment](1418698-thread_get_assignment.md)
- [thread_get_exception_ports](1418945-thread_get_exception_ports.md)
- [thread_get_mach_voucher](1418540-thread_get_mach_voucher.md)
- [thread_get_special_port](1418728-thread_get_special_port.md)
- [thread_get_state](1418576-thread_get_state.md)
- [thread_has_thread_name](3075293-thread_has_thread_name.md)
- [thread_info](1418630-thread_info.md)
- [thread_policy](1418640-thread_policy.md)
- [thread_policy_get](1418518-thread_policy_get.md)
- [thread_policy_set](1418892-thread_policy_set.md)
- [thread_reference](1429093-thread_reference.md)
- [thread_resume](1418926-thread_resume.md)
- [thread_sample](1418814-thread_sample.md)
- [thread_set_exception_ports](1418619-thread_set_exception_ports.md)
- [thread_set_mach_voucher](1418834-thread_set_mach_voucher.md)
- [thread_set_policy](1418608-thread_set_policy.md)
- [thread_set_special_port](1418995-thread_set_special_port.md)
- [thread_set_state](1418827-thread_set_state.md)
- [thread_set_thread_name](3075294-thread_set_thread_name.md)
- [thread_suspend](1418833-thread_suspend.md)
- [thread_swap_exception_ports](1418969-thread_swap_exception_ports.md)
- [thread_swap_mach_voucher](1418678-thread_swap_mach_voucher.md)
- [thread_terminate](1418708-thread_terminate.md)
- [thread_tid](1429091-thread_tid.md)
- [thread_wakeup_prim](1524383-thread_wakeup_prim.md)
- [thread_wakeup_thread](1646218-thread_wakeup_thread.md)
- [thread_wire](1588756-thread_wire.md)
- [thread_act_array_t](thread_act_array_t.md)
- [thread_act_port_array_t](thread_act_port_array_t.md)
- [thread_act_port_t](thread_act_port_t.md)
- [thread_act_t](thread_act_t.md)
- [thread_affinity_policy_t](thread_affinity_policy_t.md)
- [thread_array_t](thread_array_t.md)
- [thread_background_policy_t](thread_background_policy_t.md)
- [thread_basic_info_t](thread_basic_info_t.md)
- [thread_call_func_t](thread_call_func_t.md)
- [thread_call_options_t](thread_call_options_t.md)
- [thread_call_param_t](thread_call_param_t.md)
- [thread_call_t](thread_call_t.md)
- [thread_command](thread_command.md)
- [thread_continue_t](thread_continue_t.md)
- [thread_delta_snapshot_v2](thread_delta_snapshot_v2.md)
- [thread_delta_snapshot_v3](thread_delta_snapshot_v3.md)
- [thread_extended_info_t](thread_extended_info_t.md)
- [thread_extended_policy_t](thread_extended_policy_t.md)
- [thread_flavor_t](thread_flavor_t.md)
- [mach_thread_flavor_t](mach_thread_flavor_t.md)
- [thread_group_flags](thread_group_flags.md)
- [thread_group_snapshot](thread_group_snapshot.md)
- [thread_group_snapshot_v2](thread_group_snapshot_v2.md)
- [thread_identifier_info_t](thread_identifier_info_t.md)
- [thread_info_data_t](thread_info_data_t.md)
- [thread_info_t](thread_info_t.md)
- [thread_inspect_t](thread_inspect_t.md)
- [thread_latency_qos_policy_t](thread_latency_qos_policy_t.md)
- [thread_latency_qos_t](thread_latency_qos_t.md)
- [thread_policy_flavor_t](thread_policy_flavor_t.md)
- [thread_policy_t](thread_policy_t.md)
- [thread_port_array_t](thread_port_array_t.md)
- [thread_port_t](thread_port_t.md)
- [thread_precedence_policy_t](thread_precedence_policy_t.md)
- [thread_snapshot_flags](thread_snapshot_flags.md)
- [thread_snapshot_v2](thread_snapshot_v2.md)
- [thread_snapshot_v3](thread_snapshot_v3.md)
- [thread_snapshot_v4](thread_snapshot_v4.md)
- [thread_standard_policy_t](thread_standard_policy_t.md)
- [thread_state_data_t](thread_state_data_t.md)
- [thread_state_flavor_array_t](thread_state_flavor_array_t.md)
- [thread_state_flavor_t](thread_state_flavor_t.md)
- [thread_state_t](thread_state_t.md)
- [thread_t](thread_t.md)
- [thread_throughput_qos_policy_t](thread_throughput_qos_policy_t.md)
- [thread_throughput_qos_t](thread_throughput_qos_t.md)
- [thread_time_constraint_policy_t](thread_time_constraint_policy_t.md)
- [thread_affinity_policy_data_t](thread_affinity_policy_data_t.md)
- [thread_background_policy_data_t](thread_background_policy_data_t.md)
- [thread_basic_info_data_t](thread_basic_info_data_t.md)
- [thread_extended_info_data_t](thread_extended_info_data_t.md)
- [thread_extended_policy_data_t](thread_extended_policy_data_t.md)
- [thread_identifier_info_data_t](thread_identifier_info_data_t.md)
- [thread_latency_qos_policy_data_t](thread_latency_qos_policy_data_t.md)
- [thread_precedence_policy_data_t](thread_precedence_policy_data_t.md)
- [thread_standard_policy_data_t](thread_standard_policy_data_t.md)
- [thread_throughput_qos_policy_data_t](thread_throughput_qos_policy_data_t.md)
- [thread_time_constraint_policy_data_t](thread_time_constraint_policy_data_t.md)
- [thread_turnstileinfo_t](thread_turnstileinfo_t.md)
- [thread_waitinfo_t](thread_waitinfo_t.md)
- [act_get_state](1418936-act_get_state.md)
- [act_set_state](1418961-act_set_state.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/thread_snapshot)*