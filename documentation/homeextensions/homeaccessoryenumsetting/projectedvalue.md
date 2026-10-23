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
final var projectedValue: HomeAccessoryEnumSetting<Value> { get }
```

#### Discussion

Use it to list the setting in [`availableSettings`](../homeaccessorysettingscontainer/availablesettings.md) or to customize its appearance.

## See Also

### Accessing the selection
- [var wrappedValue: Value?](./wrappedvalue.md)
  The selected option, or the default option if nothing is selected.
- [var selectedValues: Set<Value>?](./selectedvalues.md)
  The selected options, for a setting that supports multiple selection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homeextensions/homeaccessoryenumsetting/projectedvalue)*