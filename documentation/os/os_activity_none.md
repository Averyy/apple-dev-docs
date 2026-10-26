# OS_ACTIVITY_NONE

**Framework**: os  
**Kind**: macro  
**Role**: Macro

A special value that indicates a nonexistent activity.

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
#define OS_ACTIVITY_NONE
```

#### Discussion

When creating a new activity, pass this value as the activity’s parent to create the new activity as a top-level activity without a parent.

## See Also

### Choosing a Special Activity
- [OS_ACTIVITY_CURRENT](./os_activity_current.md)
  A special value that selects the current activity, if there is one.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/os_activity_none)*