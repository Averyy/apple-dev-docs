# kernel_thread_start

**Framework**: Kernel  
**Kind**: func

Create a kernel thread.

**Availability**:
- macOS 10.4+

## Declaration

```swift
kern_return_t kernel_thread_start(thread_continue_t continuation, void *parameter, thread_t *new_thread);
```

#### Return_value

Returns KERN_SUCCESS on success or an appropriate kernel code type.

#### Discussion

This function takes three input parameters, namely reference to the function that the thread should execute, caller specified data and a reference which is used to return the newly created kernel thread. The function returns KERN_SUCCESS on success or an appropriate kernel code type indicating the error. It may be noted that the caller is responsible for explicitly releasing the reference to the created thread when no longer needed. This should be done by calling thread_deallocate(new_thread).

## Parameters

- `continuation`: A C-function pointer where the thread will begin execution.
- `parameter`: Caller specified data to be passed to the new thread.
- `new_thread`: Reference to the new thread is returned in this parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1429094-kernel_thread_start)*