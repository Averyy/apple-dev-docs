# processor_set_tasks_with_flavor

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 11.0+

## Declaration

```swift
kern_return_t processor_set_tasks_with_flavor(processor_set_t processor_set, mach_task_flavor_t flavor, task_array_t *task_list, mach_msg_type_number_t *task_listCnt);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/3553717-processor_set_tasks_with_flavor)*