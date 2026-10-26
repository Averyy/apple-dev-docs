# OS_ACTIVITY_FLAG_IF_NONE_PRESENT

**Framework**: os  
**Kind**: case  
**Role**: Enumeration Case

Creates a new activity only if one is not already present.

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
OS_ACTIVITY_FLAG_IF_NONE_PRESENT
```

#### Discussion

When you include this flag when calling a function that creates an activity, if an activity already exists, the function returns that activity. Otherwise, the function creates and returns a new activity.

Don’t pass [`OS_ACTIVITY_FLAG_DETACHED`](./os_activity_flag_detached.md) and [`OS_ACTIVITY_FLAG_IF_NONE_PRESENT`](./os_activity_flag_if_none_present.md) at the same time.

## See Also

### Adjusting Activity Creation
- [OS_ACTIVITY_FLAG_DEFAULT](./os_activity_flag_default.md)
  Creates a new activity and associates it as a child of any provided parent activity.
- [OS_ACTIVITY_FLAG_DETACHED](./os_activity_flag_detached.md)
  Creates a new activity that is independent of any provided parent activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/os_activity_flag_t/os_activity_flag_if_none_present)*