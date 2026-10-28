# projectedValue

**Framework**: HomeExtensions  
**Kind**: property  
**Role**: Instance Property

The setting itself, which you access with a dollar sign prefix.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
final var projectedValue: HomeAccessoryToggleSetting { get }
```

## Discussion

Use it to list the setting in [`availableSettings`](../homeaccessorysettingscontainer/availablesettings.md) or to customize its appearance.

## See Also

### Accessing the value
- [var wrappedValue: Bool?](./wrappedvalue.md)
  The setting’s current value, or its default value if it has none.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homeextensions/homeaccessorytogglesetting/projectedvalue)*