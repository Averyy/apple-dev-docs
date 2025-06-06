# beginState(id:)

**Framework**: os  
**Kind**: method

Recreates interval state from the specified signpost ID.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- tvOS 15.0+
- visionOS ?+
- watchOS 8.0+

## Declaration

```swift
static func beginState(id: OSSignpostID) -> OSSignpostIntervalState
```

#### Return Value

The recreated interval state.

#### Discussion

> ❗ **Important**:  Recreating interval state to end a signposted interval bypasses runtime assertions that check for consistency between the beginning and the end of the interval.

 Recreating interval state to end a signposted interval bypasses runtime assertions that check for consistency between the beginning and the end of the interval.

## Parameters

- `id`: The signpost ID you use to begin the signposted interval.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/ossignpostintervalstate/beginstate(id:))*