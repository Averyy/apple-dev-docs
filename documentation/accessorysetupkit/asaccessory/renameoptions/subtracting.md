# subtracting(_:)

**Framework**: AccessorySetupKit  
**Kind**: method

Returns a new set containing the elements of this set that do not occur in the given set.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
func subtracting(_ other: Self) -> Self
```

#### Return Value

A new set.

#### Discussion

In the following example, the `nonNeighbors` set is made up of the elements of the `employees` set that are not elements of `neighbors`:

```None
let employees: Set = ["Alicia", "Bethany", "Chris", "Diana", "Eric"]
let neighbors: Set = ["Bethany", "Eric", "Forlani", "Greta"]
let nonNeighbors = employees.subtracting(neighbors)
print(nonNeighbors)
// Prints "["Diana", "Chris", "Alicia"]"
```

## Parameters

- `other`: A set of the same type as the current set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorysetupkit/asaccessory/renameoptions/subtracting(_:))*