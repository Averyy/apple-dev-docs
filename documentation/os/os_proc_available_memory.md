# os_proc_available_memory

**Framework**: os  
**Kind**: func  
**Role**: Function

Determines the amount of memory available to the current app.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```c
extern size_t os_proc_available_memory();
```

#### Return Value

The number of bytes the app may allocate before it hits its memory limit. If the calling process isn’t an app, or if the process has already exceeded its memory limit, this function returns `0`.

#### Discussion

Call this function to determine the amount of memory available to your app. The returned value corresponds to the current memory limit minus the memory footprint of your app at the time of the function call. Your app’s memory footprint consists of the data that you allocated in RAM, and that must stay in RAM (or the equivalent) at all times. Memory limits can change during the app life cycle and don’t necessarily correspond to the amount of physical memory available on the device.

Use the returned value as advisory information only and don’t cache it. The precise value changes when your app does any work that affects memory, which can happen frequently.

Although this function lets you determine the amount of memory your app may safely consume, don’t use it to maximize your app’s memory usage. Significant memory use, even when under the current memory limit, affects system performance. For example, when your app consumes all of its available memory, the system may need to terminate other apps and system processes to accommodate your app’s requests. Instead, always consume the smallest amount of memory you need to be responsive to the user’s needs.

If you need more detailed information about the available memory resources, you can call [`task_info`](../kernel/api-1537934-task_info.md). However, be aware that [`task_info`](../kernel/api-1537934-task_info.md) is an expensive call, whereas this function is much more efficient.

## See Also

### Memory
- [os_block_t](./os_block_t.md)
  A block that takes no arguments and returns no value.
- [os_function_t](./os_function_t.md)
  A pointer to a function.
- [os_release](./os_release-c.func.md)
- [os_retain](./os_retain-c.func.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/os_proc_available_memory)*