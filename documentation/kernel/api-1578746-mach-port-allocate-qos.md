# mach_port_allocate_qos

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.0+

## Declaration

```swift
kern_return_t mach_port_allocate_qos(ipc_space_t task, mach_port_right_t right, mach_port_qos_t *qos, mach_port_name_t *name);
```

## See Also

- [mem_entry_name_port_t](mem_entry_name_port_t.md)
- [mach_port_array_t](mach_port_array_t.md)
- [mach_port_context_t](mach_port_context_t.md)
- [mach_port_delta_t](mach_port_delta_t.md)
- [mach_port_flavor_t](mach_port_flavor_t.md)
- [mach_port_guard_exception_codes](mach_port_guard_exception_codes.md)
- [mach_port_info_t](mach_port_info_t.md)
- [mach_port_mscount_t](mach_port_mscount_t.md)
- [mach_port_msgcount_t](mach_port_msgcount_t.md)
- [mach_port_name_array_t](mach_port_name_array_t.md)
- [mach_port_name_t](mach_port_name_t.md)
- [mach_port_options_ptr_t](mach_port_options_ptr_t.md)
- [mach_port_right_t](mach_port_right_t.md)
- [mach_port_rights_t](mach_port_rights_t.md)
- [mach_port_seqno_t](mach_port_seqno_t.md)
- [mach_port_srights_t](mach_port_srights_t.md)
- [mach_port_t](mach_port_t.md)
- [mach_port_type_array_t](mach_port_type_array_t.md)
- [mach_port_type_t](mach_port_type_t.md)
- [mach_port_urefs_t](mach_port_urefs_t.md)
- [mach_port_allocate](1578704-mach_port_allocate.md)
- [mach_port_allocate_full](1578763-mach_port_allocate_full.md)
- [mach_port_allocate_name](1578657-mach_port_allocate_name.md)
- [mach_port_construct](1578687-mach_port_construct.md)
- [mach_port_deallocate](1578777-mach_port_deallocate.md)
- [mach_port_destroy](1578817-mach_port_destroy.md)
- [mach_port_destruct](1578881-mach_port_destruct.md)
- [mach_port_dnrequest_info](1578613-mach_port_dnrequest_info.md)
- [mach_port_extract_member](1578633-mach_port_extract_member.md)
- [mach_port_extract_right](1578688-mach_port_extract_right.md)
- [mach_port_get_attributes](1578800-mach_port_get_attributes.md)
- [mach_port_get_context](1578930-mach_port_get_context.md)
- [mach_port_get_refs](1578946-mach_port_get_refs.md)
- [mach_port_get_set_status](1578936-mach_port_get_set_status.md)
- [mach_port_get_srights](1578818-mach_port_get_srights.md)
- [mach_port_guard](1578772-mach_port_guard.md)
- [mach_port_guard_with_flags](3181823-mach_port_guard_with_flags.md)
- [mach_port_insert_member](1578885-mach_port_insert_member.md)
- [mach_port_insert_right](1578739-mach_port_insert_right.md)
- [mach_port_kernel_object](1578723-mach_port_kernel_object.md)
- [mach_port_kobject](1578702-mach_port_kobject.md)
- [mach_port_kobject_description](3516847-mach_port_kobject_description.md)
- [mach_port_mod_refs](1578894-mach_port_mod_refs.md)
- [mach_port_move_member](1578673-mach_port_move_member.md)
- [mach_port_names](1578814-mach_port_names.md)
- [mach_port_peek](1578839-mach_port_peek.md)
- [mach_port_rename](1578909-mach_port_rename.md)
- [mach_port_request_notification](1578734-mach_port_request_notification.md)
- [mach_port_set_attributes](1578964-mach_port_set_attributes.md)
- [mach_port_set_context](1578733-mach_port_set_context.md)
- [mach_port_set_mscount](1578719-mach_port_set_mscount.md)
- [mach_port_set_seqno](1578744-mach_port_set_seqno.md)
- [mach_port_space_basic_info](1578841-mach_port_space_basic_info.md)
- [mach_port_space_info](1578884-mach_port_space_info.md)
- [mach_port_special_reply_port_reset_link](3013817-mach_port_special_reply_port_res.md)
- [mach_port_swap_guard](3181824-mach_port_swap_guard.md)
- [mach_port_type](1578714-mach_port_type.md)
- [mach_port_unguard](1578951-mach_port_unguard.md)
- [mach_eventlink_t](mach_eventlink_t.md)
- [audit_triggers](1574078-audit_triggers.md)
- [mach_port_deleted_notification_t](mach_port_deleted_notification_t.md)
- [mach_port_destroyed_notification_t](mach_port_destroyed_notification_t.md)
- [mach_port_info_ext_t](mach_port_info_ext_t.md)
- [mach_port_limits_t](mach_port_limits_t.md)
- [mach_port_options_t](mach_port_options_t.md)
- [mach_port_qos_t](mach_port_qos_t.md)
- [mach_port_status_t](mach_port_status_t.md)
- [ipc_info_name_array_t](ipc_info_name_array_t.md)
- [ipc_info_tree_name_array_t](ipc_info_tree_name_array_t.md)
- [ipc_object_t](ipc_object_t.md)
- [ipc_perm](ipc_perm.md)
- [ipc_port_t](ipc_port_t.md)
- [ipc_pthread_priority_value_t](ipc_pthread_priority_value_t.md)
- [ipc_space_inspect_t](ipc_space_inspect_t.md)
- [ipc_space_port_t](ipc_space_port_t.md)
- [ipc_space_t](ipc_space_t.md)
- [ipc_voucher_attr_control_t](ipc_voucher_attr_control_t.md)
- [ipc_voucher_attr_manager_t](ipc_voucher_attr_manager_t.md)
- [ipc_voucher_t](ipc_voucher_t.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1578746-mach_port_allocate_qos)*