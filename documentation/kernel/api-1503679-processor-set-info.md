# processor_set_info

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.0+

## Declaration

```swift
kern_return_t processor_set_info(processor_set_name_t set_name, int flavor, host_t *host, processor_set_info_t info_out, mach_msg_type_number_t *info_outCnt);
```

## See Also

- [processor_assign](1409351-processor_assign.md)
- [processor_control](1409386-processor_control.md)
- [processor_exit](1409353-processor_exit.md)
- [processor_get_assignment](1409365-processor_get_assignment.md)
- [processor_info](1409385-processor_info.md)
- [processor_set_create](1502809-processor_set_create.md)
- [processor_set_default](1502766-processor_set_default.md)
- [processor_set_destroy](1503645-processor_set_destroy.md)
- [processor_set_max_priority](1503640-processor_set_max_priority.md)
- [processor_set_policy_control](1503688-processor_set_policy_control.md)
- [processor_set_policy_disable](1503665-processor_set_policy_disable.md)
- [processor_set_policy_enable](1503657-processor_set_policy_enable.md)
- [processor_set_stack_usage](1503624-processor_set_stack_usage.md)
- [processor_set_statistics](1503608-processor_set_statistics.md)
- [processor_set_tasks](1503628-processor_set_tasks.md)
- [processor_set_threads](1503576-processor_set_threads.md)
- [processor_start](1409392-processor_start.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1503679-processor_set_info)*