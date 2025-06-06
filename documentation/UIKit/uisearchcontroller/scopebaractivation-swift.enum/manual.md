# UISearchController.ScopeBarActivation.manual

**Framework**: UIKit  
**Kind**: case

A mode that gives you manual control over when to show and hide the scope bar.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
case manual
```

#### Discussion

When you use this mode, you control when to show and hide the scope bar through the [`showsScopeBar`](uisearchbar/showsscopebar.md) property on the [`searchBar`](uisearchcontroller/searchbar.md) of the [`UISearchController`](uisearchcontroller.md).

## See Also

- [UISearchController.ScopeBarActivation.automatic](uisearchcontroller/scopebaractivation-swift.enum/automatic.md)
  A mode in which the system automatically determines when to show and hide the scope bar.
- [UISearchController.ScopeBarActivation.onTextEntry](uisearchcontroller/scopebaractivation-swift.enum/ontextentry.md)
  A mode in which the search controller shows the scope bar when typing begins in the search field, and hides it after search cancellation.
- [UISearchController.ScopeBarActivation.onSearchActivation](uisearchcontroller/scopebaractivation-swift.enum/onsearchactivation.md)
  A mode in which the search controller shows the scope bar when search becomes active, and hides it after search cancellation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchcontroller/scopebaractivation-swift.enum/manual)*