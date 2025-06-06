# formIntersection(_:)

**Framework**: AccessorySetupKit  
**Kind**: method

Removes all elements of this option set that are not also present in the given set.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
mutating func formIntersection(_ other: Self)
```

#### Discussion

This method is implemented as a `&` (bitwise AND) operation on the two sets’ raw values.

## Parameters

- `other`: An option set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorysetupkit/asaccessory/supportoptions/formintersection(_:))*