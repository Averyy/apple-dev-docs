# os_block_t

**Framework**: os  
**Kind**: typealias  
**Role**: Type Alias

A block that takes no arguments and returns no value.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```c
typedef void (^)(void) os_block_t;
```

## Discussion

When not building with Objective-C ARC, a block object allocated on or copied to the heap must be released with a [`release`](../ObjectiveC/nsobject-c.protocol/release.md) message or the `Block_release` function.

The declaration of a block literal allocates storage on the stack.

## See Also

### Memory
- [os_proc_available_memory](./os_proc_available_memory.md)
  Determines the amount of memory available to the current app.
- [os_function_t](./os_function_t.md)
  A pointer to a function.
- [os_release](./os_release-c.func.md)
- [os_retain](./os_retain-c.func.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/os_block_t)*