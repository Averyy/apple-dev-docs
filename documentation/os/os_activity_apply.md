# os_activity_apply

**Framework**: os  
**Kind**: func  
**Role**: Function

Execute a block using a given activity object.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```c
extern void os_activity_apply(os_activity_t activity, os_block_t block);
```

## Mentions

- [Collecting Log Messages in Activities](./collecting-log-messages-in-activities.md)

## Parameters

- `activity`: An activity object. You can alternatively pass one of the global activity constants, such as [`OS_ACTIVITY_NONE`](./os_activity_none.md) or [`OS_ACTIVITY_CURRENT`](./os_activity_current.md).
- `block`: The block to be executed within the context of the given activity.

## See Also

### Executing an Activity
- [os_activity_apply_f](./os_activity_apply_f.md)
  Execute a function using a given activity object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/os_activity_apply)*