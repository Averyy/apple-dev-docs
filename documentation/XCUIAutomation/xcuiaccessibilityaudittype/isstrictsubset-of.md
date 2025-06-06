# isStrictSubset(of:)

**Framework**: Xcuiautomation  
**Kind**: method

Returns a Boolean value that indicates whether this set is a strict subset of the given set.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+
- Xcode 16.3+

## Declaration

```swift
func isStrictSubset(of other: Self) -> Bool
```

#### Return Value

`true` if the set is a strict subset of `other`; otherwise, `false`.

#### Discussion

Set  is a strict subset of another set  if every member of  is also a member of  and  contains at least one element that is not a member of .

```None
let employees: Set = ["Alicia", "Bethany", "Chris", "Diana", "Eric"]
let attendees: Set = ["Alicia", "Bethany", "Diana"]
print(attendees.isStrictSubset(of: employees))
// Prints "true"

// A set is never a strict subset of itself:
print(attendees.isStrictSubset(of: attendees))
// Prints "false"
```

## Parameters

- `other`: A set of the same type as the current set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuiaccessibilityaudittype/isstrictsubset(of:))*