# OS_ACTIVITY_CURRENT

**Framework**: os  
**Kind**: macro  
**Role**: Macro

A special value that selects the current activity, if there is one.

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
#define OS_ACTIVITY_CURRENT
```

#### Discussion

When creating a new activity, pass this value as the activity’s parent to create the new activity with the current activity as its parent. If there is no active activity, the creation function returns the new activity as a top-level activity without a parent.

## See Also

### Choosing a Special Activity
- [OS_ACTIVITY_NONE](./os_activity_none.md)
  A special value that indicates a nonexistent activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/os_activity_current)*