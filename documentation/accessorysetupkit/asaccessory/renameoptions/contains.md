# contains(_:)

**Framework**: AccessorySetupKit  
**Kind**: method

Returns a Boolean value that indicates whether a given element is a member of the option set.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
func contains(_ member: Self) -> Bool
```

#### Return Value

`true` if the option set contains `member`; otherwise, `false`.

#### Discussion

This example uses the `contains(_:)` method to check whether next-day shipping is in the `availableOptions` instance.

```None
let availableOptions = ShippingOptions.express
if availableOptions.contains(.nextDay) {
    print("Next day shipping available")
}
// Prints "Next day shipping available"
```

## Parameters

- `member`: The element to look for in the option set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorysetupkit/asaccessory/renameoptions/contains(_:))*