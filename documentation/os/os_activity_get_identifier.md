# os_activity_get_identifier

**Framework**: os  
**Kind**: func  
**Role**: Function

Retrieves the identifier for a given activity object.

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
extern os_activity_id_t os_activity_get_identifier(os_activity_t activity, os_activity_id_t *parent_id);
```

## Return Value

The current activity identifier.

## Parameters

- `activity`: The activity to be identified.
- `parent_id`: On return, contains the identifier of the parent of the activity object, if any. Pass `NULL` if you don’t need this identifier.

## See Also

### Retrieving an Activity Identifier
- [os_activity_id_t](./os_activity_id_t.md)
  A number that uniquely identifies an activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/os_activity_get_identifier)*