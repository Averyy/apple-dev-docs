# mach_vm_range_create

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 14.0+

## Declaration

```swift
kern_return_t mach_vm_range_create(vm_map_t target_task, mach_vm_range_flavor_t flavor, mach_vm_range_recipes_raw_t recipes, mach_msg_type_number_t recipesCnt);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/4168415-mach_vm_range_create)*